

#definir as nossas funcoes e seus respectivos parametros
#oque fica dentro da funcao e uma variavel que e passada como parametro
#a lista e o conjunto das nossas funcoes
def cadastrar_missao(lista):
    print("\n--- Cadastro de Missão ---")
    nave = input("Nome da nave: ")
    destino = input("Destino: ")
    tripulantes = int(input("Nº de tripulantes: "))
    combustivel = float(input("Combustível disponível (litros): "))
    duracao = int(input("Duração da missão (dias): "))
    
    #nosso objeto missao que ira armazenar as seguintes variaveis e seus valores
    missao = {
        "nave": nave,
        "destino": destino,
        "tripulantes": tripulantes,
        "combustivel": combustivel,
        "duracao": duracao
    }

    #nossa lista vai armazenar as missoes que criamos
    lista.append(missao)
    print("Missão cadastrada com sucesso!")

#funcao que vai listar nossas funcoes
#recebe tambem uma lista como parametro
def listar_missoes(lista):
    print("\n--- Missões Cadastradas ---")
    #se o comprimento da lista for igual a zero mostramos que nenhuma missao foi encontrado
    if len(lista) == 0:
        print("Nenhuma missão cadastrada.")
    else:
        #se nao,nos iremos percorrer nossa lista,procurando o indice da missao e a missao
        #cada missao tem seu propio indice
        #pra cada missao na lista,nos iremos mostrar as informacoes da nossa missao

        for indice, missao in enumerate(lista):
            print(f"\nMissão {i+1}")
            print(f"Nave: {missao['nave']}")
            print(f"Destino: {missao['destino']}")
            print(f"Tripulantes: {missao['tripulantes']}")
            print(f"Combustível: {missao['combustivel']} L")
            print(f"Duração: {missao['duracao']} dias")

def simular_lancamento(lista):
    print("\n--- Simulação de Lançamento ---")
    if len(lista) == 0:
        print("Nenhuma missão cadastrada.")
        return
    #novamente percorreremos a nossa lista:
    for indice, missao in enumerate(lista):
        print(f"{indice+1} - {missao['nave']} (Destino: {missao['destino']})")
    
    #escolhemos a missao que queremos lancar
    escolha = int(input("Escolha a missão: ")) - 1

    if 0 <= escolha < len(lista):
        missao = lista[escolha]
        #aqui calculamos o consumo que e a quantidade de tripulantes vezes 500
        consumo = missao['tripulantes'] * 500

        print(f"\nSimulando a missão da nave {missao['nave']}")
        print(f"Combustível necessário: {consumo} L")
        print(f"Disponível: {missao['com[bustivel']} L")
        
        #verifica se o combustivel e maior ou igual ao consumo exigido
        if missao['combustivel'] >= consumo:
            print("Missão aprovada! Lançamento autorizado.")
        #se nao,mostrara que o combustivel e insuficiente
        else:
            print("Combustível insuficiente.")
    else:
        print("Missão inválida.")
