from spire.doc import *
from spire.doc.common import *
        
# Create a Document object
document = Document()
# Load a Word DOCX file
document.LoadFromFile("doc/demo.docx")

# Or load a Word DOC file
#document.LoadFromFile("Sample.doc")

# Save the file to a PDF file
document.SaveToFile("pdf/WordToPdf.pdf", FileFormat.PDF)
document.Close()

