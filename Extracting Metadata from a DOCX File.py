import docx
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def get_docx_metadata(docx_path):
    doc = docx.Document(docx_path)
    core_properties = doc.core_properties

    # Print core properties
    print("Core Properties:")
    print(f"Title: {core_properties.title}")
    print(f"Author: {core_properties.author}")
    print(f"Subject: {core_properties.subject}")
    print(f"Keywords: {core_properties.keywords}")
    print(f"Last Modified By: {core_properties.last_modified_by}")
    print(f"Created: {core_properties.created}")
    print(f"Last Printed: {core_properties.last_printed}")
    print(f"Modified: {core_properties.modified}")
    print(f"Category: {core_properties.category}")
    print(f"Comments: {core_properties.comments}")
    
    # Retrieve hyperlinks if available
    hyperlinks = []
    for rel in doc.part.rels:
        if rel.startswith(RT.HYPERLINK):
            hyperlinks.append(doc.part.rels[rel].target_ref)

    if hyperlinks:
        print("\nHyperlinks:")
        for link in hyperlinks:
            print(link)

# Example usage
docx_path = 'example.docx'
get_docx_metadata(docx_path)
