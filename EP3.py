# -*- coding: utf-8 -*-

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        #Criando janela e os campos
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("450x350+150+150")
       
        #Definindo o tamanha das linhas e colunas da janela.       
        self.window.rowconfigure(0, minsize= 100)
        self.window.rowconfigure(1, minsize= 100)
        self.window.rowconfigure(2, minsize= 100)        
        self.window.rowconfigure(3, minsize= 50)        

        self.window.columnconfigure(0, minsize= 150)
        self.window.columnconfigure(1, minsize= 150)
        self.window.columnconfigure(2, minsize= 150)
        self.window.columnconfigure(3,minsize = 150)
 
        #Criando o primeiro botão. 
        self.button1 = tk.Button(self.window)
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button1.configure(command = self.button1_clicado)

        #Criando o segundo botão.
        self.button2 = tk.Button(self.window)
        self.button2.grid(row=0, column=1, sticky="nsew")
        self.button2.configure(command = self.button2_clicado)
 
        #Criando o terceiro botão.
        self.button3 = tk.Button(self.window)
        self.button3.grid(row=0, column=2, sticky="nsew")
        self.button3.configure(command = self.button3_clicado)

        #Criando o quarto botão.
        self.button4 = tk.Button(self.window)
        self.button4.grid(row=1, column=0, sticky="nsew")
        self.button4.configure(command = self.button4_clicado)

        #Criando o quinto botão.
        self.button5 = tk.Button(self.window)
        self.button5.grid(row=1, column=1, sticky="nsew")
        self.button5.configure(command = self.button5_clicado)

        #Criando o sexto botão.
        self.button6 = tk.Button(self.window)
        self.button6.grid(row=1, column=2, sticky="nsew")
        self.button6.configure(command = self.button6_clicado)

        #Criando o sétimo botão.
        self.button7 = tk.Button(self.window)
        self.button7.grid(row=2, column=0, sticky="nsew")
        self.button7.configure(command = self.button7_clicado)

        #Criando o oitavo botão.
        self.button8 = tk.Button(self.window)
        self.button8.grid(row=2, column=1, sticky="nsew")
        self.button8.configure(command = self.button8_clicado)

        #Criando o nono botão.
        self.button9 = tk.Button(self.window)
        self.button9.grid(row=2, column=2, sticky="nsew")
        self.button9.configure(command = self.button9_clicado)

        self.mostra_jogador = tk.StringVar(self.window)
        self.mostra_jogador.set("Jogador:")
        label = tk.Label(self.window)
        label.grid(row=3, column=0, columnspan=1, sticky="nsew")
        label.config(textvariable = self.mostra_jogador)
        
    def iniciar(self):
        self.window.mainloop()
        
        
    #Botões precionados
           
    def button1_clicado(self):
        print("Botão 1 clicado")
    
    def button2_clicado(self):
        print("Botão 2 clicado")
        
    def button3_clicado(self):
        print("Botão 3 clicado")
        
    def button4_clicado(self):
        print("Botão 4 clicado")
    
    def button5_clicado(self):
        print("Botão 5 clicado")
        
    def button6_clicado(self):
        print("Botão 6 clicado")
        
    def button7_clicado(self):
        print("Botão 7 clicado")
        
    def button8_clicado(self):
        print("Botão 8 clicado")
        
    def button9_clicado(self):
        print("Botão 9 clicado")
        
    
    
        
jogo = jogo_da_velha()
jogo.iniciar()