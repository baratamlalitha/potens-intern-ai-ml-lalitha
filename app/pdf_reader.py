from PyPDF2 import PdfReader
import os

def load_pdfs(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, file)

            reader = PdfReader(pdf_path)

            for page_num, page in enumerate(reader.pages):

                text = page.extract_text()

                if text:

                    documents.append({
                        "source": file,
                        "page": page_num + 1,
                        "text": text
                    })

    return documents