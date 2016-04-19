# -*- coding: utf-8 -*-

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        #Criando janela e os campos
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("450x300+150+150")
       
        #Definindo o tamanha das linhas e colunas da janela.       
        self.window.rowconfigure(0, minsize= 100)
        self.window.rowconfigure(1, minsize= 100)
        self.window.rowconfigure(2, minsize= 100)        
        self.window.rowconfigure(3, minsize= 420)        

        self.window.columnconfigure(0, minsize= 150)
        self.window.columnconfigure(1, minsize= 150)
        self.window.columnconfigure(2, minsize= 150)
 
        #Criando o primeiro botão. 
        self.button1 = tk.Button(self.window)
        self.button1.grid(row=0, column=0, sticky="nsew")

        #Criando o segundo botão.
        self.button2 = tk.Button(self.window)
        self.button2.grid(row=0, column=1, sticky="nsew")
 
        #Criando o terceiro botão.
        self.button3 = tk.Button(self.window)
        self.button3.grid(row=0, column=2, sticky="nsew")

        #Criando o quarto botão.
        self.button4 = tk.Button(self.window)
        self.button4.grid(row=1, column=0, sticky="nsew")

        #Criando o quinto botão.
        self.button5 = tk.Button(self.window)
        self.button5.grid(row=1, column=1, sticky="nsew")

        #Criando o sexto botão.
        self.button6 = tk.Button(self.window)
        self.button6.grid(row=1, column=2, sticky="nsew")

        #Criando o sétimo botão.
        self.button7 = tk.Button(self.window)
        self.button7.grid(row=2, column=0, sticky="nsew")

        #Criando o oitavo botão.
        self.button8 = tk.Button(self.window)
        self.button8.grid(row=2, column=1, sticky="nsew")

        #Criando o nono botão.
        self.button9 = tk.Button(self.window)
        self.button9.grid(row=2, column=2, sticky="nsew")

        self.mostra_jogador = tk.StringVar(self.window)
        self.mostra_jogador.grid(row=3, sticky="nsew")
        
    def iniciar(self):
        self.window.mainloop()
        
jogo = jogo_da_velha()
jogo.iniciar()