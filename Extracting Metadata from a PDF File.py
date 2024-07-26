import PyPDF2

def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        metadata = reader.getDocumentInfo()
        
        if metadata:
            print("PDF Metadata:")
            for key, value in metadata.items():
                # Removing the leading '/' from keys
                print(f"{key[1:]}: {value}")  
            
            print("\nAdditional Information:")
            print(f"Number of Pages: {reader.getNumPages()}")
            if reader.isEncrypted:
                print("The PDF is encrypted.")
            else:
                print("The PDF is not encrypted.")
        else:
            print("No metadata found in the PDF file.")

# Example usage
pdf_path = 'example.pdf'
get_pdf_metadata(pdf_path)
