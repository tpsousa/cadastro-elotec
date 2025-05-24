from funcoes import *

# Lista que armazena as missões
missoes = []

# Menu principal
def menu():
    while True:
        print("\n=== MENU DE MISSÕES ESPACIAIS ===")
        print("1 - Cadastrar missão")
        print("2 - Listar missões")
        print("3 - Simular lançamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_missao(missoes)
        elif opcao == '2':
            listar_missoes(missoes)
        elif opcao == '3':
            simular_lancamento(missoes)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

menu()
