import os
import glob
from pypdf import PdfReader
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def get_pdf_info(filepath):
    print(f"--- Processing PDF: {filepath} ---")
    try:
        reader = PdfReader(filepath)
        info = reader.metadata
        print(f"Title: {info.title if info else 'Unknown'}")
        
        # First page text for ID
        if len(reader.pages) > 0:
            first_page_text = reader.pages[0].extract_text()
            print(f"First Page Snippet: {first_page_text[:200].replace(chr(10), ' ')}...")
        
        # Outline
        outline = reader.outline
        if outline:
            print("Outline found:")
            count = 0
            for item in outline:
                if count > 5:
                    print("... (more chapters)")
                    break
                if isinstance(item, list):
                    continue # Skip nested for brief checking
                try:
                    print(f"- {item.title}")
                    count += 1
                except:
                    pass
        else:
            print("No Outline found.")
            
    except Exception as e:
        print(f"Error reading PDF: {e}")

def get_epub_info(filepath):
    print(f"--- Processing EPUB: {filepath} ---")
    try:
        book = epub.read_epub(filepath)
        print(f"Title: {book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else 'Unknown'}")
        
        # Spine
        print(f"Spine length: {len(book.spine)}")
        # Check TOC
        print("TOC sample:")
        count = 0
        for item in book.toc:
            if count > 5:
                print("... (more chapters)")
                break
            if isinstance(item, tuple): # Section
                 print(f"- {item[0].title}")
            elif isinstance(item, epub.Link):
                 print(f"- {item.title}")
            count += 1
            
    except Exception as e:
        print(f"Error reading EPUB: {e}")

def main():
    pdfs = glob.glob("*.pdf")
    epubs = glob.glob("*.epub")
    
    for pdf in pdfs:
        get_pdf_info(pdf)
    
    for ep in epubs:
        get_epub_info(ep)

if __name__ == "__main__":
    main()
