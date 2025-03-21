import secrets
import string 

# size = int(input("Escolha o tamanho da senha: "))

# letras = string.ascii_letters
# numeros = string.digits 
# especial = string.punctuation

# itens = letras + numeros + especial
# senha = [secrets.choice(itens)
#         for i in range (size)]
# senha = ''.join(senha)
# print(senha)


while True:
    print("\nGerador de senha")
    print("1 - Gerar senha")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        size = int(input("Escolha o tamanho da senha: "))

        letras = string.ascii_letters
        numeros = string.digits 
        especial = string.punctuation

        itens = letras + numeros + especial
        senha = [secrets.choice(itens)
                for i in range (size)]
        senha = ''.join(senha)
        print(senha)
    elif opcao == "0":
        print("")
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida, tente novamente!")