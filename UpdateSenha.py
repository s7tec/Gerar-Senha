import secrets
import string 

letrasMi = string.ascii_lowercase
letrasMa = string.ascii_uppercase
numbers = string.digits 
especial = string.punctuation
letras = letrasMi + letrasMa
while True:
    
    print("\nGerador de senha" )
    print("1 - Gerar senha")
    print("0 - Sair")

    option_one = input("Escolha uma opção: ")

    if option_one == "1":
        size = int(input("Escolha o tamanho da senha: "))

        option_two = input("Escolha caracteristicas para sua senha\n"
                    "Exemplo:24"
                    "1-Todos os caracteres\n"
                    "2-Letras\n"
                    "3-Números\n"
                    "4-Caractere Especial\n"
                    "5-Letras Maiusculas\n"
                    "6-Letras Minusculas\n"
                    "\nOpção: ")
        
        if option_two == "1":
            items = numbers + letras + especial
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")
        
        elif option_two == "23" or option_two == "32":
            items =  numbers + letras
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        elif option_two == "24" or option_two == "42":
            items =  numbers + especial
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        elif option_two == "35" or option_two == "53":
            items =  numbers + letrasMa
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        elif option_two == "36" or option_two == "63":
            items =  numbers + letrasMi
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        elif option_two == "46" or option_two == "64":
            items =  especial + letrasMi
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        elif option_two == "46" or option_two == "64":
            items =  numbers + letrasMi
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")
        
        elif option_two == "345" or option_two == "435" or option_two == "435":
            items =  numbers + letrasMa + especial
            senha = [secrets.choice(items)
                for i in range (size)]
            senha = ''.join(senha)
            print(f"Sua senha gerada:\n{senha}")

        else:
            print("Opção inválida, tente novamente!")
        

    elif option_one == "0":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida, tente novamente!")