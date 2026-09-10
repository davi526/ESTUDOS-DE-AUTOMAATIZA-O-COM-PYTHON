import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Python Deck")
app.geometry("300x200")

def mostrar_nome():
    nome = input_nome.get()
    resultado.configure(
        text=f"Nome: {nome}!"
    )

titulo = ctk.CTkLabel(app, text="Python Deck")
titulo.pack(pady=10)

input_nome = ctk.CTkEntry(app, placeholder_text="Digite seu nome")
input_nome.pack(pady=10)

botao = ctk.CTkButton(app, text="Mostrar Nome", command=mostrar_nome)
botao.pack(pady=10)

resultado = ctk.CTkLabel(app, text="Aqui aparecerá o nome digitado")
resultado.pack(pady=10)

app.mainloop()
