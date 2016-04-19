# -*- coding: utf-8 -*-

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        #Criando janela e os campos
        self.lastx = 0
        self.lasty = 0
        
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x200+100+100")

