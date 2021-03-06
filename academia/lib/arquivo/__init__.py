from lib.interface import *
from time import sleep


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso")
        a.close()


def adicionarAluno(nome, alunos):
    try:
        a = open(alunos, "at")
    except:
        print("Houve um erro ao abrir o arquivo!")
    else:
        try:
            a.write(f"{nome}\n")
        except:
            print("Houve erro ao escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()


def lerAlunos(alunos):
    try:
        a = open(alunos, "rt")
    except:
        print("Houve erro ao abrir o arquivo")
    else:
        cabecalho("ALUNOS CADASTRADOS")
        for linha in a:
            linha = linha.replace(".txt", "").title()
            print(f"{linha:<60}")
        sleep(5)


def criarTreino(nome, alunos):
    adicionarAluno(nome, alunos)
    criarArquivo(nome)
    treino = ["EXERCICIO", "S", "R", "OBSERVAÇÕES"]
    try:
        a = open(nome, "at")
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f"{treino[0]:<20}{treino[1]:<3}{treino[2]:<3}{treino[3]:<20}\n")
            a.write(f"{linhas()}")
            a.write("\n")
            while True:
                exercicio = str(input("Exercicio: "))
                series = leiaInt("Series: ")
                repet = leiaInt("Repetições: ")
                obs = str(input("Obs: "))
                a.write(f"{exercicio:<20}{series:<3}{repet:<3}{obs:<20}\n")
                a.write("-" * 60)
                a.write("\n\n")
                while True:
                    escolha = str(input("Quer adicionar mais um exercicio? [S/N] ")).strip()[0]
                    if escolha in "SsNn":
                        break
                if escolha in "Nn":
                    a.close()
                    break
        except:
            print("Houve um erro ao escrever os dados!")
        else:
            print("Treino Criado com Sucesso!")


def lerTreino(nome):
    try:
        a = open(nome, "rt")
    except:
        print("TREINO NÃO REGISTRADO!\nPor favor, peça para que um dos treinadores da academia monte seu treino!")
    else:
        cabecalho("TREINO COMPLETO")
        print(a.read())
        sleep(8)
        a.close()
