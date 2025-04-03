import secrets
import string 

letras = string.ascii_letters
numbers = string.digits 
especial = string.punctuation

while True:
    
    print("\nGerador de senha" )
    print("1 - Gerar senha")
    print("0 - Sair")

    option_one = input("Escolha uma opção: ")

    if option_one == "1":
        size = int(input("Escolha o tamanho da senha: "))

        option_two = input("Escolha caracteristicas para sua senha\n" 
                    "1-Digitos + Letras\n"
                    "2-Letras + Caractere Especial\n"
                    "3-Todos os caracteres\n"
                    "\nOpção: ")
        if option_two == "1":
            one_items = letras + numbers
            one_senha = [secrets.choice(one_items)
                for i in range (size)]
            one_senha = ''.join(one_senha)
            print(f"Sua senha gerada:\n{one_senha}")
        
        elif option_two == "2":
            two_items = letras + especial
            two_senha = [secrets.choice(two_items)
                for i in range (size)]
            two_senha = ''.join(two_senha)
            print(f"Sua senha gerada:\n{two_senha}")
        
        elif option_two == "3":
            three_items = letras + numbers + especial
            three_senha = [secrets.choice(three_items)
                for i in range (size)]
            three_senha = ''.join(three_senha)
            print(f"Sua senha gerada:\n{three_senha}")
        else:
            print("Opção inválida, tente novamente!")
        

    elif option_one == "0":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida, tente novamente!")