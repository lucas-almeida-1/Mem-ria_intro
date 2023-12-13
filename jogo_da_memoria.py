import random
import tkinter as tk
from tkinter import messagebox


def jogar():
    criar_desenho_cartas()
    janela.mainloop()


def clique(l, c):
    cartao = cartas[l][c]
    cor = cartao["bg"]
    if cor == "#fcafae":
        cartao.config(text=matriz[l][c], bg="#faf0a2")
        reveladas.append(cartao)
        if len(reveladas) == 2:
            equivale()


def equivale():
    c1, c2 = reveladas
    if c1["text"] == c2["text"]:
        atualiza_ponto()
        c1.config(bg="#8ae38f")
        c2.config(bg="#8ae38f")
        match.extend([c1, c2])
        vitoria()
    else:
        c1.after(1000, lambda: c1.config(text="", bg="#fcafae"))
        c2.after(1000, lambda: c2.config(text="", bg="#fcafae"))
        atualiza_ponto(troca=True)
    reveladas.clear()


def atualiza_ponto(troca=False):
    global turno, p1, p2
    if troca:
        turno = 2 ** (2 - turno)
    else:
        if turno == 1:
            p1 += 1
        else:
            p2 += 1
    etiqueta.config(text=f" {p1} : Jogador 1| Vez do Jogador {turno} | Jogador 2 : {p2} ")


def vitoria():
    if len(match) == 28:
        if p1 > p2:
            messagebox.showinfo("Jogador 1 ganhou !         ")
        elif p2 > p1:
            messagebox.showinfo("Jogador 2 ganhou !         ")
        else:
            messagebox.showinfo("Empatou !                  ")
        janela.quit()


def embaralhar():
    lista = ["2", "2", "3", "2", "1", "5", "3", "8", "4", "l", "u", "c", "a", "s"] * 2
    random.shuffle(lista)
    matriz = []
    for k in range(4):
        linha = []
        for valor in range(7):
            elemento = lista.pop()
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def criar_desenho_cartas():
    for l in range(4):
        linha = []
        for co in range(7):
            carta = tk.Button(janela,
                              command=lambda r=l, c=co: clique(r, c),
                              width=9, height=6, bg="#fcafae", relief=tk.RAISED, bd=3)
            carta.grid(row=l, column=co, padx=15, pady=15)
            linha.append(carta)
        cartas.append(linha)

def estilo():
    cb = {"activebackground": "#8ae38f", "font": fonte, "fg": cor_fonte}
    janela.option_add("*Button", cb)


def etiquetas():
    e_jogador = tk.Label(janela, text=" 0 : Jogador 1| Vez do Jogador 1 | Jogador 2 : 0 ", fg=cor_fonte, font=fonte,
                         bg="#9daebf")
    e_jogador.grid(row=4, columnspan=7, padx=10, pady=10)
    return e_jogador


p1 = p2 = 0
turno = 1
reveladas = []
match = []
cartas = []
fonte = ("Arial", 30, "bold")
cor_fonte = "#000000"
matriz = embaralhar()
janela = tk.Tk()
janela.title("Jogo da memória")
janela.configure(bg="#9daebf")
estilo()
etiqueta = etiquetas()

if __name__ == "__main__":
    jogar()
