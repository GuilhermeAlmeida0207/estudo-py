#Projeto para treinar comandos de entrada e saída + funções de texto e f-string

print("\n============= CADASTRO DE DOADORES DE SANGUE =============")

nome = input("Digite seu nome: ")
idade = int(input(f"{nome}, informe a sua idade: "))
altura = int(input(f"{nome}, por gentileza, digite sua altura em centímetros: "))
peso = float(input(f"Por fim, {nome}, insira seu peso em kg: "))


print(f"""
Nome: {nome.capitalize()}
Idade: {idade}
Altura: {altura}cm
Peso: {peso:.2f}kg
""") 
