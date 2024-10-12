import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mesclar PDFs")

        # Botão para inserir PDFs manualmente
        self.btn_inserir = tk.Button(self.root, text="Inserir PDFs", command=self.inserir_pdfs)
        self.btn_inserir.pack(pady=20)

        # Botão para mesclar os PDFs
        self.btn_mesclar = tk.Button(self.root, text="Mesclar PDFs", command=self.mesclar_pdfs)
        self.btn_mesclar.pack(pady=10)

        # Inicializar a lista de PDFs
        self.pdfs = []

    def inserir_pdfs(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if arquivo:
            self.pdfs.append(arquivo)
            messagebox.showinfo("Sucesso", "PDF inserido com sucesso!")

    def mesclar_pdfs(self):
        if not self.pdfs:
            messagebox.showwarning("Aviso", "Nenhum PDF inserido.")
            return
        
        merger = PyPDF2.PdfMerger()
        
        try:
            for pdf in self.pdfs:
                merger.append(pdf)
            
            arquivo_final = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivo PDF", "*.pdf")])
            if arquivo_final:
                merger.write(arquivo_final)
                messagebox.showinfo("Sucesso", "PDFs mesclados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao mesclar os PDFs:\n{str(e)}")
        finally:
            merger.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
