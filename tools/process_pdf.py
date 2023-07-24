import pdfplumber

pdf_path = "OriginalPdf.pdf"

def get_words(path):
    wordlist = ""
    with pdfplumber.open(path) as pdf:
        for i in range(len(pdf.pages)):
            print("Processing page " + str(i))
            clean_text = pdf.pages[i].filter(lambda obj: obj["object_type"] == "char" and obj["fontname"] == "AJMDCE+AkzidenzGroteskBE-XBdCn")
            wordlist += clean_text.extract_text() + "\n"

    with open("../Words.txt", "w") as wfile:
        wfile.write(wordlist)
        wfile.close()

get_words(pdf_path)



