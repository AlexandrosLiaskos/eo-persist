from docling.document_converter import DocumentConverter
import os

def convert_pdfs():
    converter = DocumentConverter()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(current_dir, 'markdown_output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all PDF files in the current directory
    pdf_files = [f for f in os.listdir(current_dir) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        try:
            print(f"Converting {pdf_file}...")
            pdf_path = os.path.join(current_dir, pdf_file)
            result = converter.convert(pdf_path)
            
            # Save markdown output
            output_file = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.document.export_to_markdown())
            print(f"Successfully converted {pdf_file} to {output_file}")
            
        except Exception as e:
            print(f"Error converting {pdf_file}: {str(e)}")

if __name__ == "__main__":
    convert_pdfs()
