opções = int(input("""Digite um opção: 
1-cadastrar usuario
2-ver lista de usuarios cadastrados
3-sair do programa
"""))
match opções:
        case 1:
                str(input("Digite o nome do cliente: "))
                cadastro = str(input("Cliente cadastrado com sucesso!!! deseja fazer outro cadastro? S/N: "))
                while cadastro == "s":
                        str(input("Digite o nome do cliente: "))
                        str(input("Cliente cadastrado com sucesso!!! deseja fazer outro cadastro? S/N: "))
                while cadastro == "n" and cadastro !="s":
                        print("\nprograma finalizado!!!")
                        break
        case 2:
                print("dia 2")
        case 3:
              while opções == 3:
                print("\nprograma finalizado!!!")
                break  
        
        case _:
                print("opção invalida!!!")
        
       