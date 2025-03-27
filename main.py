from datetime import datetime
import os

def escrever_no_diario():
    """Função para registrar uma nova entrada no diário."""
    entrada = input("Digite sua anotação/pensamento: ")
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Verificando se o arquivo já existe antes de tentar abri-lo
    if not os.path.exists("diario.txt"):
        print("Arquivo 'diario.txt' não encontrado. Ele será criado agora.")

    with open("diario.txt", "a") as arquivo:
        arquivo.write(f"{data_hora} - {entrada}\n")
    print("Anotação registrada com sucesso!")

def ler_entradas():
    """Função para exibir todas as entradas no diário."""
    if os.path.exists("diario.txt"):
        with open("diario.txt", "r") as arquivo:
            print("\nEntradas no Diário:")
            print("-" * 30)
            print(arquivo.read())
    else:
        print("Nenhuma entrada encontrada. O arquivo 'diario.txt' ainda não foi criado.")

def menu():
    """Menu interativo para o usuário."""
    while True:
        print("\n=== Diário Eletrônico ===")
        print("1. Escrever no diário")
        print("2. Ler todas as entradas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        if opcao == "1":
            escrever_no_diario()
        elif opcao == "2":
            ler_entradas()
        elif opcao == "3":
            print("Saindo do Diário Eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()