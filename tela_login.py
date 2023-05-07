from tkinter import *

class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Tela de Login")

        # cria o rótulo para o campo de nome de usuário
        username_label = Label(master, text="Nome de Usuário:")
        username_label.pack(side=TOP, pady=10)
        
        # cria a entrada para o campo de nome de usuário
        self.username_entry = Entry(master)
        self.username_entry.pack(side=TOP, padx=20, pady=5, ipadx=30)

        # cria o rótulo para o campo de senha
        password_label = Label(master, text="Senha:")
        password_label.pack(side=TOP, pady=10)

        # cria a entrada para o campo de senha
        self.password_entry = Entry(master, show="*")
        self.password_entry.pack(side=TOP, padx=20, pady=5, ipadx=30)

        # cria o botão de login
        login_button = Button(master, text="Login", command=self.login)
        login_button.pack(side=TOP, pady=20)

        # centraliza os objetos na tela
        for child in master.winfo_children():
            child.pack_configure(anchor="center")

    def login(self):
        # implemente aqui a lógica de login
        pass


root = Tk()
login_screen = LoginScreen(root)
root.mainloop()