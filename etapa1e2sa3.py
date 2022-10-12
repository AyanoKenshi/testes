clientes = []

#cadastrar clientes
def cadastro():
  
  while True:
    
    
    print("digite os dados do cliente: ")

    dados = {}
    dados["nome_do_cliente"] = input("Nome: ")
    dados["idade"] = int(input("Idade: "))

    clientes.append(dados)
    
    print("cadastro concluido")
    opção = input("deseja cadastrar outro cliente? S/N?: ")
    if(opção == "n"):
      menu()
      break
#mostrar os clientes
def mostrar_clientes_cadastrados():

    while True:
      print("")
      print("clientes cadastrados: ")
      print("")

      for i in clientes:
        print("nome:", i["nome_do_cliente"])
        print("idade:", i["idade"], "anos")
      
      print("")
      opção = input("deseja conferir novamente? S/N: ")
      if(opção == "n"):
        menu()
        break
#menu de seleção
def menu():
  print("1-Cadastrar clientes")
  print("2-ver clientes cadastrados")
  print("3-Sair")
menu()
while True:

  opc = int(input("selecione uma opção: "))
  while opc > 4 or opc < 0:
    opc = int(input("opção invalida!!! Digite novamente: "))

  if opc == 1:
    cadastro()
  elif opc == 2:
    mostrar_clientes_cadastrados()
  else:
    print("Programa Finalizado :D")
    break