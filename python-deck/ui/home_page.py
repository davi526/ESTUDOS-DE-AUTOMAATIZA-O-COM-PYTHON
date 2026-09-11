import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Python Deck")
app.geometry("400x500")

def mostrar_nome():
    # Captura o nome digitado e converte para letras maiúsculas
    nome = input_nome.get().upper()

    # Captura o sobrenome digitado e converte para letras maiúsculas
    sobrenome = input_sobrenome.get().upper()

    # Verifica se algum dos dois campos está vazio
    if not nome or not sobrenome:
        resultado.configure(text="Preencha o nome e o sobrenome.")
        numero_caracteres_label.configure(text="Número de caracteres: 0")
    else:
        # Junta nome e sobrenome, colocando um espaço entre eles
        nome_completo = nome + " " + sobrenome

        # Conta somente as letras, ignorando o espaço entre os dois campos
        numero_caracteres = len(nome + sobrenome)

        resultado.configure(text=f"Olá, {nome_completo}!")
        numero_caracteres_label.configure(
            text=f"Número de caracteres: {numero_caracteres}"
        )


titulo = ctk.CTkLabel(app, text="Python Deck")
titulo.pack(pady=10)

input_nome = ctk.CTkEntry(app, placeholder_text="Digite seu nome")
input_nome.pack(pady=10)

input_sobrenome = ctk.CTkEntry(app, placeholder_text="Digite seu sobrenome")
input_sobrenome.pack(pady=10)

botao = ctk.CTkButton(app, text="Mostrar Nome", command=mostrar_nome)
botao.pack(pady=10)

limpar_campo = ctk.CTkButton(
    app,
    text="Limpar Campo",
    command=lambda: [
        input_nome.delete(0, ctk.END),
        input_sobrenome.delete(0, ctk.END),
    ],
)
limpar_campo.pack(pady=10)

botao_sair = ctk.CTkButton(app, text="Sair", command=app.quit)
botao_sair.pack(pady=10)

resultado = ctk.CTkLabel(app, text="Aqui aparecerá o nome digitado")
resultado.pack(pady=10)
resultado.configure(font=("Arial", 12, "bold"))

numero_caracteres_label = ctk.CTkLabel(app, text="Número de caracteres: 0")
numero_caracteres_label.pack(pady=10)

app.mainloop()
