import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

lista_arquivos = os.listdir(caminho)

locais = {
    'imagens': {".png", ".jpg"},
    "planilhas":{'.xlsx'},
    "pdfs": {".pdf"},
    "csv": {".csv"},
    "word": {".docx"},
    "powerBI": {".pbix"}
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:#pasta referente a locais exem: imagens,planilhas,pdfs,csv
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f'{caminho}/{pasta}/{arquivo}')
