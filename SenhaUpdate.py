import secrets
import string 

letras = string.ascii_letters
numeros = string.digits 
especial = string.punctuation

while True:
    
    print("\nGerador de senha" )
    print("1 - Gerar senha")
    print("0 - Sair")

    opcao_one = input("Escolha uma opção: ")

    if opcao_one == "1":
        size = int(input("Escolha o tamanho da senha: "))

        opcao_two = input("Escolha caracteristicas para sua senha\n" 
                    "1-Digitos + Letras\n"
                    "2-Letras + Caractere Especial\n"
                    "3-Digitos + Letras + Caractere Especial\n"
                    "\nOpção: ")
        if opcao_two == "1":
            one_itens = letras + numeros
            one_senha = [secrets.choice(one_itens)
                for i in range (size)]
            one_senha = ''.join(one_senha)
            print(f"Sua senha gerada:\n{one_senha}")
        
        elif opcao_two == "2":
            two_itens = letras + especial
            two_senha = [secrets.choice(two_itens)
                for i in range (size)]
            two_senha = ''.join(two_senha)
            print(f"Sua senha gerada:\n{two_senha}")
        
        elif opcao_two == "3":
            three_itens = letras + numeros + especial
            three_senha = [secrets.choice(three_itens)
                for i in range (size)]
            three_senha = ''.join(three_senha)
            print(f"Sua senha gerada:\n{three_senha}")
        else:
            print("Opção inválida, tente novamente!")
        

    elif opcao_one == "0":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida, tente novamente!")