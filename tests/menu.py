import random

op = 0
animatronic = [
    "Freddy",
    "Chica",
    "Foxy",
    "Bonnie"
]

while op != 3:
    print("\n---------- MENU + FNAF ----------")
    print("""
    1 - Animatronic aleatório
    2 - Calcular um fatorial
    3 - Sair
    """)
    
    op = int(input("Digite uma opção do menu: "))

    if op == 1:
        print("O animatronic escolhido foi:", random.choice(animatronic))

    elif op == 2:
        numero = int(input("Informe um número para descobrir seu fatorial: "))
        fat = numero

        for valor in range(1, numero, 1):
            fat = fat * valor
        print(f"O fatorial de {numero} é igual a {fat}")

    elif op == 3:
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nInsira um valor do menu!")