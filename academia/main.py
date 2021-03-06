from lib.arquivo import *

arqalunos = "alunos.txt"
if not arquivoExiste(arqalunos):
    criarArquivo(arqalunos)

while True:
    resp = menu(["Eu sou professor", "Eu sou aluno", "Sair do sistema"])
    if resp == 1:
        # Entra no painel dos professores
        while True:
            resp1 = menu(["Novo treino", "Voltar"], 1)
            if resp1 == 1:
                nome = str(input("Nome do aluno: ")).strip().lower()
                nome += ".txt"
                criarTreino(nome, arqalunos)
            elif resp1 == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção valida!\033[m")
    elif resp == 2:
        # Entra no painel dos alunos
        while True:
            resp2 = menu(["Alunos cadastrados","Imprimir treino", "Voltar"], 2)
            if resp2 == 1:
                lerAlunos(arqalunos)
            elif resp2 == 2:
                busca = str(input("Qual o seu nome: ")).strip().lower()
                busca += ".txt"
                lerTreino(busca)
            elif resp2 == 3:
                break
            else:
                print("\033[31mERRO! Digite uma opção valida!\033[m")
    elif resp == 3:
        # Sai do sistema
        break
    else:
        # Digitou opção errada no menu princpal
        print("\033[31mERRO! Digite uma opção valida!\033[m")
