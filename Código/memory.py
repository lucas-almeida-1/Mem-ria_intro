# Equipe:
# Lucas Almeida de Lima
# Raquel Silva Nunes
# Gabriel Chaves Prates
# Giovane Santos de Santana

# Importar biblioteca gráfica
import tkinter as tk

# Definir os dígitos do grupo
digitos = ["2", "2", "3", "2", "1", "5", "3", "8", "4", "L", "u", "c", "a", "s"]

# Criar uma lista de cartas com os dígitos
cartas = []
for d in digitos:
    cartas.append(d)
    cartas.append(d) # duplicar para formar pares

# Embaralhar as cartas
import random
random.shuffle(cartas)

# Criar uma janela para o jogo
janela = tk.Tk()
janela.title("Jogo da Memória")

# Criar um quadro para o tabuleiro
tabuleiro = tk.Frame(janela)
tabuleiro.pack()

# Criar um quadro para o placar
placar = tk.Frame(janela)
placar.pack()

# Criar um dicionário para armazenar os botões das cartas
botoes = {}

# Criar uma função para virar uma carta
def virar_carta(i):
    global primeira, segunda, jogador, pontos
    # Se já houver duas cartas viradas, não fazer nada
    if primeira is not None and segunda is not None:
        return
    # Se a carta já estiver virada, não fazer nada
    if botoes[i]["text"] != "":
        return
    # Virar a carta e mostrar o seu valor
    botoes[i]["text"] = cartas[i]
    botoes[i]["bg"] = "grey"
    # Se for a primeira carta virada, armazenar o seu índice
    if primeira is None:
        primeira = i
    # Se for a segunda carta virada, verificar se forma um par com a primeira
    else:
        segunda = i
        # Se formar um par, incrementar o placar do jogador atual
        if cartas[primeira] == cartas[segunda]:
            pontos[jogador] += 1
            botoes[primeira]["bg"] = "green"
            botoes[segunda]["bg"] = "green"
            # Atualizar o placar na tela
            placar_jogador1["text"] = f"Jogador 1: {pontos[1]}"
            placar_jogador2["text"] = f"Jogador 2: {pontos[2]}"
            # Verificar se o jogo acabou
            if pontos[1] + pontos[2] == 14:
                # Mostrar uma mensagem de parabéns ao vencedor
                if pontos[1] > pontos[2]:
                    vencedor = "Jogador 1"
                elif pontos[1] < pontos[2]:
                    vencedor = "Jogador 2"
                else:
                    vencedor = "Empate"
                vez_jogador["text"] = f"Vencedor: {vencedor}"
                tk.messagebox.showinfo("Fim de jogo", f"Parabéns, {vencedor}!")
                # Fechar a janela
                janela.destroy()
            # Resetar os índices das cartas viradas
            primeira = None
            segunda = None
        # Se não formar um par, trocar o jogador atual
        else:
            botoes[primeira]["bg"] = "red"
            botoes[segunda]["bg"] = "red"
            jogador = 3 - jogador
            # Atualizar o jogador na tela
            vez_jogador["text"] = f"Vez do Jogador {jogador}"
            # Aguardar um segundo e depois esconder as cartas viradas
            janela.after(1000, esconder_cartas)

# Criar uma função para esconder as cartas viradas
def esconder_cartas():
    global primeira, segunda
    # Esconder as cartas viradas
    botoes[primeira]["text"] = ""
    botoes[segunda]["text"] = ""
    botoes[primeira]["bg"] = "white"
    botoes[segunda]["bg"] = "white"
    # Resetar os índices das cartas viradas
    primeira = None
    segunda = None

# Criar uma função para iniciar um novo jogo
def novo_jogo():
    global cartas, jogador, pontos, primeira, segunda
    # Embaralhar as cartas
    random.shuffle(cartas)
    # Resetar o jogador e os pontos
    jogador = 1
    pontos = {1: 0, 2: 0}
    # Atualizar o placar e o jogador na tela
    placar_jogador1["text"] = "Jogador 1: 0"
    placar_jogador2["text"] = "Jogador 2: 0"
    vez_jogador["text"] = "Vez do Jogador 1"
    # Resetar os índices das cartas viradas
    primeira = None
    segunda = None
    # Resetar os botões das cartas
    for i in range(28):
        botoes[i]["text"] = cartas[i]
        botoes[i]["bg"] = "white"
    # Esconder as cartas após 3 segundos
    janela.after(3000, lambda: [botoes[i].config(text="", bg="white") for i in range(28)])

# Criar os botões das cartas e adicioná-los ao tabuleiro
for i in range(28):
    # Criar um botão com texto vazio e cor de fundo branca
    botao = tk.Button(tabuleiro, text=cartas[i], bg="white", width=10, height=5)
    # Posicionar o botão na linha e coluna correspondentes
    botao.grid(row=i//7, column=i%7)
    # Associar o botão ao seu índice na lista de cartas
    botao["command"] = lambda i=i: virar_carta(i)
    # Adicionar o botão ao dicionário de botões
    botoes[i] = botao
    # Adicionar a funcionalidade de mudança de cor ao passar o mouse sobre o botão
    botao.bind("<Enter>", lambda e, i=i: botoes[i].config(bg="lightgrey") if botoes[i]["text"] == "" else None)
    botao.bind("<Leave>", lambda e, i=i: botoes[i].config(bg="white") if botoes[i]["text"] == "" else None)

# Criar as variáveis para armazenar os índices das cartas viradas
primeira = None
segunda = None

# Criar a variável para armazenar o jogador atual
jogador = 1

# Criar a variável para armazenar os pontos de cada jogador
pontos = {1: 0, 2: 0}

# Criar os labels para mostrar o placar e o jogador atual
placar_jogador1 = tk.Label(placar, text="Jogador 1: 0", font=("Arial", 20))
placar_jogador1.pack(side="left")
vez_jogador = tk.Label(placar, text="Vez do Jogador 1", font=("Arial", 20))
vez_jogador.pack(side="left")
placar_jogador2 = tk.Label(placar, text="Jogador 2: 0", font=("Arial", 20))
placar_jogador2.pack(side="right")

# Criar um botão para iniciar um novo jogo
botao_novo_jogo = tk.Button(placar, text="Novo Jogo", command=novo_jogo)
botao_novo_jogo.pack(side="left")

# Iniciar o loop principal da janela
janela.after(3000, lambda: [botoes[i].config(text="", bg="white") for i in range(28)])
janela.mainloop()
