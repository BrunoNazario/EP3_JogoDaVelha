# -*- coding: utf-8 -*-

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        
        
        self.player = 0
        
        
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
        
        #Combinações ganhadoras
#        self.combinaçoes_ganhadoras = [{self.button1,self.button2, self.button3}, {self.button4, self.button5, self.button6},
#                                       {self.button7, self.button8, self.button9}, {self.button1, self.button5, self.button9},
#                                       {self.button3, self.button5, self.button7}, {self.button1, self.button4, self.button7},
#                                       {self.button2, self.button5, self.button8}, {self.button3, self.button6, self.button9}]
#                                       
                                       
    def iniciar(self):
        self.window.mainloop()
        
    def Vitoria(self):
        return self.combinaçoes_ganhadoras
        
        
     
    #Botões pressionados
           
    def button1_clicado(self):
        if self.player == 0:
            self.button1.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button1.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
  
    def button2_clicado(self):
        if self.player == 0:
            self.button2.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button2.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")

    def button3_clicado(self):
        if self.player == 0:
            self.button3.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button3.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
                
    def button4_clicado(self):
        if self.player == 0:
            self.button4.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button4.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
            
    def button5_clicado(self):
        if self.player == 0:
            self.button5.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button5.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
                
    def button6_clicado(self):
        if self.player == 0:
            self.button6.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button6.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
                
    def button7_clicado(self):
        if self.player == 0:
            self.button7.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button7.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
                
    def button8_clicado(self):
        if self.player == 0:
            self.button8.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button8.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
                
    def button9_clicado(self):
        if self.player == 0:
            self.button9.configure(text="X", state="disabled")
            self.player += 1
            self.mostra_jogador.set("Jogador: O")
        else:
            self.button9.configure(text="O", state="disabled")
            self.player -=1
            self.mostra_jogador.set("Jogador: X")
            
            
#class Jogo:
#    
#    def __init__ (self):
#        
#        #Combinações ganhadoras
#        self.combinaçoes_ganhadoras = [{1,2,3}, {4,5,6}, {7,8,9}, {1,5,9},
#                                       {3,5,7}, {1,4,7}, {2,5,8}, {3,6,9}]
#                
    
#    def muda_jogador1(self):    
#        if self.button1_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button1_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#    
#    def muda_jogador2(self):
#        if self.button2_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button2_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#   
#    def muda_jogador3(self):
#        if self.button3_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button3_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador4(self):
#        if self.button4_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button4_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador5(self):
#        if self.button5_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button5_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador6(self):
#        if self.button6_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button6_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador7(self):
#        if self.button7_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button7_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador8(self):
#        if self.button8_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button8_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#    def muda_jogador9(self):
#        if self.button9_clicado == True and self.mostra_jogador == "Jogador: X":
#            self.mostra_jogador == "Jogador: O"
#        elif self.button9_clicado == True and self.mostra_jogador == "Jogador: O":
#            self.mostra_jogador == "Jogador: X"
#
#class Jogador:
#    
#    def __init__ (self):
#        self.jogador1= ["X"]
#        self.jogador2=["O"]
#        
#    def Jogador (self):
#        if self.jogador == "X":
#            for i in range (9):
#                self.button_clicado(i)
#                print("X")
#        else:
#            for i in range (9):
#                self.button_clicado(i)
#                print("O")
#                

        
jogo = jogo_da_velha()
jogo.iniciar()