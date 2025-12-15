import sys

def convert(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-16le') as f:
            content = f.read()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        # Try different encoding if utf-16le fails?
        try:
            with open(input_file, 'r', encoding='cp1252') as f:
                content = f.read()
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Converted {input_file} to {output_file} (fallback cp1252)")
        except Exception as e2:
            print(f"Error 2: {e2}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        convert(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python convert_utf8.py <input> <output>")
        # Default fallback for testing
        # convert("book2.txt", "book2_utf8.txt")
