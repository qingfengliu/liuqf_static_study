from docling.document_converter import DocumentConverter

source = "D:\工作\电网公平开放监管办法.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())
