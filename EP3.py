# -*- coding: utf-8 -*-

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        
        
        self.player = 0
        
        
        #Criando janela e os campos
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("450x400+150+150")
       
        #Definindo o tamanha das linhas e colunas da janela.       
        self.window.rowconfigure(0, minsize= 100)
        self.window.rowconfigure(1, minsize= 100)
        self.window.rowconfigure(2, minsize= 100) 
        self.window.rowconfigure(3, minsize= 50)

        self.window.columnconfigure(0, minsize= 150)
        self.window.columnconfigure(1, minsize= 150)
        self.window.columnconfigure(2, minsize= 150)
        self.window.columnconfigure(3,minsize = 150)

        self.mostra_jogador = tk.StringVar(self.window)
        self.mostra_jogador.set("Jogador: X")
        label = tk.Label(self.window)
        label.grid(row=3, column=0, columnspan=1, sticky="nsew")
        label.config(textvariable = self.mostra_jogador)
        
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
        self.button9.configure(command= self.button9_clicado)
        
        self.button_restart=tk.Button(self.window)
        self.button_restart.grid(row=4, column=1, sticky="nsew")
        self.button_restart.configure(text = "Reiniciar")        
        self.button_restart.configure(command= self.button_reinicia)

    #Combinações ganhadoras
        self.combinaçoes_ganhadoras = [{self.button1,self.button2, self.button3}, {self.button4, self.button5, self.button6},
                                       {self.button7, self.button8, self.button9}, {self.button1, self.button5, self.button9},
                                       {self.button3, self.button5, self.button7}, {self.button1, self.button4, self.button7},
                                       {self.button2, self.button5, self.button8}, {self.button3, self.button6, self.button9}]
                                       
                                       
    def iniciar(self):
        self.window.mainloop()
        
    def Vitoria(self):
        if self.combinaçoes_ganhadoras == True:
            self.button1.configure(state = "disabled")
            self.button2.configure(state = "disabled")
            self.button3.configure(state = "disabled")
            self.button4.configure(state = "disabled")
            self.button5.configure(state = "disabled")
            self.button6.configure(state = "disabled")
            self.button7.configure(state = "disabled")
            self.button8.configure(state = "disabled")
            self.button9.configure(state = "disabled")
            
        return self.combinaçoes_ganhadoras

    #Botões pressionados
           
    def button1_clicado(self):
        if self.player == 0:
            self.button1.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button1.configure(text="O", state="disabled")
            self.player -=1
  
    def button2_clicado(self):
        if self.player == 0:
            self.button2.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button2.configure(text="O", state="disabled")
            self.player -=1

    def button3_clicado(self):
        if self.player == 0:
            self.button3.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button3.configure(text="O", state="disabled")
            self.player -=1
                
    def button4_clicado(self):
        if self.player == 0:
            self.button4.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button4.configure(text="O", state="disabled")
            self.player -=1
            
    def button5_clicado(self):
        if self.player == 0:
            self.button5.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button5.configure(text="O", state="disabled")
            self.player -=1
                
    def button6_clicado(self):
        if self.player == 0:
            self.button6.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button6.configure(text="O", state="disabled")
            self.player -=1
                
    def button7_clicado(self):
        if self.player == 0:
            self.button7.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button7.configure(text="O", state="disabled")
            self.player -=1
                
    def button8_clicado(self):
        if self.player == 0:
            self.button8.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button8.configure(text="O", state="disabled")
            self.player -=1
                
    def button9_clicado(self):
        if self.player == 0:
            self.button9.configure(text="X", state="disabled")
            self.player += 1
        else:
            self.button9.configure(text="O", state="disabled")
            self.player -=1
            
                
    def button_reinicia(self):
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
        self.button9.configure(command= self.button9_clicado)
        
        def muda_jogador(self):
            if self.player == 0:
                self.mostra_jogador.set("Jogador: X")
            else:
                self.mostra_jogador.set("Jogador: O")
            
jogo = jogo_da_velha()
jogo.iniciar()