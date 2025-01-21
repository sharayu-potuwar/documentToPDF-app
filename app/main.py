from spire.doc import *
from spire.doc.common import *

import functions_framework

@functions_framework.cloud_event
def convert(cloud_event):        
    # Create a Document object
    document = Document()
    # Load a Word DOCX file
    document.LoadFromFile("doc/${cloud_event.data}")

    # Or load a Word DOC file
    #document.LoadFromFile("Sample.doc")

    # Save the file to a PDF file
    document.SaveToFile("pdf/WordToPdf.pdf", FileFormat.PDF)
    document.Close()
