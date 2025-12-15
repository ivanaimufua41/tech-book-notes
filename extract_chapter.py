import sys
import os
from pypdf import PdfReader
from ebooklib import epub
import ebooklib
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

def list_chapters(filepath):
    print(f"--- Chapters for {os.path.basename(filepath)} ---")
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        outline = reader.outline
        if not outline:
            print("No outline found.")
            return
        
        # Flatten outline for simple indexing
        chapters = []
        def process_outline(items):
            for item in items:
                if isinstance(item, list):
                    process_outline(item)
                else:
                    try:
                        # item.page is a PageObject, need to find its index. 
                        # This can be slow. pypdf outline items usually return PageObject or IndirectObject.
                        # We will skip getting exact page index for LISTING to be fast, 
                        # but we need it for extraction.
                        chapters.append(item.title)
                    except:
                        pass
        process_outline(outline)
        
        for i, title in enumerate(chapters):
            print(f"{i}: {title}")

    elif filepath.endswith('.epub'):
        book = epub.read_epub(filepath)
        # Using exact TOC order
        chapters = []
        def process_toc(items):
             for item in items:
                if isinstance(item, tuple):
                    chapters.append(item[0].title)
                    process_toc(item[1])
                elif isinstance(item, epub.Link):
                    chapters.append(item.title)
        process_toc(book.toc)
        
        for i, title in enumerate(chapters):
            print(f"{i}: {title}")

def extract_chapter(filepath, chapter_index):
    # This function needs to be robust. 
    # For PDF: Find start page of ch_index and start page of ch_index+1.
    # For EPUB: Find the item.
    
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        outline = reader.outline
        
        flat_outline = []
        def flatten(items):
            for item in items:
                if isinstance(item, list):
                    flatten(item)
                else:
                    flat_outline.append(item)
        flatten(outline)
        
        if chapter_index < 0 or chapter_index >= len(flat_outline):
            print("Invalid chapter index")
            return

        current_item = flat_outline[chapter_index]
        next_item = flat_outline[chapter_index+1] if chapter_index+1 < len(flat_outline) else None
        
        start_page = reader.get_page_number(current_item.page)
        end_page = reader.get_page_number(next_item.page) if next_item else len(reader.pages)
        
        print(f"Extracting '{current_item.title}' (Pages {start_page+1}-{end_page})")
        
        text = ""
        for p in range(start_page, end_page):
            page_text = reader.pages[p].extract_text()
            text += f"\n\n[Page {p+1}]\n{page_text}"
            
        print(text)

    elif filepath.endswith('.epub'):
        book = epub.read_epub(filepath)
        
        flat_toc = []
        def flatten_toc(items):
             for item in items:
                if isinstance(item, tuple):
                    flat_toc.append(item[0])
                    flatten_toc(item[1])
                elif isinstance(item, epub.Link):
                    flat_toc.append(item)
        flatten_toc(book.toc)
        
        if chapter_index < 0 or chapter_index >= len(flat_toc):
             print("Invalid chapter index")
             return

        item = flat_toc[chapter_index]
        print(f"Extracting '{item.title}'")
        
        # Find the document content
        # item.href points to the file.
        # We need to find the item in the book by href
        content_item = book.get_item_with_href(item.href)
        if content_item:
            soup = BeautifulSoup(content_item.get_content(), 'xml') # or html.parser
            print(soup.get_text())
        else:
            print("Could not find content for this link.")

def dump_all(filepath):
    print(f"--- Dumping all text for {os.path.basename(filepath)} ---")
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        for i, page in enumerate(reader.pages):
            try:
                text = page.extract_text()
                print(f"\n\n[Page {i+1}]\n{text}")
            except:
                print(f"\n\n[Page {i+1}] (Extraction Failed)")
                
    elif filepath.endswith('.epub'):
        book = epub.read_epub(filepath)
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            try:
                soup = BeautifulSoup(item.get_content(), 'xml')
                print(f"\n\n[Section: {item.get_name()}]\n{soup.get_text()}")
            except:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_chapter.py <file> [list|chapter_index|dump_all]")
        sys.exit(1)
        
    filepath = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "list"
    
    if mode == "list":
        list_chapters(filepath)
    elif mode == "dump_all":
        dump_all(filepath)
    else:
        try:
            idx = int(mode)
            extract_chapter(filepath, idx)
        except ValueError:
            print("Please provide a valid chapter index.")
