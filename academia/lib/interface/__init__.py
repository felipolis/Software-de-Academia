from lib.entradaDados import *


def linhas(tam=60):
    return "-" * tam


def cabecalho(txt):
    print(linhas())
    print(txt.center(60))
    print(linhas())


def menu(lista, n=0):
    if n == 0:
        cabecalho("MENU PRINCIPAL")
    elif n == 1:
        cabecalho("MENU DO PROFESSOR")
    elif n == 2:
        cabecalho("MENU DO ALUNO")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linhas())
    opc = leiaInt("Sua opção: ")
    return opc
