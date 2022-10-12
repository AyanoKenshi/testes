digite_a_idade = int(input("Usuario insira sua idade: "))
acompanhado = str(input("você está acompanhado? "))
idade = 18
#verificar a idade do visitante ou se ele está com um acompanhante
if digite_a_idade >= 18 or acompanhado == "sim":
    print("bem-vindo ao bostil")
else:
    acompanhado == "não"
    print("seja feliz longe do bostil")