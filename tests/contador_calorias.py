calorias = []
resposta = ""

while resposta.upper() != "NÃO":

    resposta = input("\nVocê deseja adicionar uma refeição? [Digite NÃO para partir ao cálculo]: ")
    if resposta.upper() == "NÃO":
        break
    
    caloria = int(input("Informe quantas calorias você consumiu nesta refeição: "))
    calorias.append(caloria)

numero_calorias = 0
soma = 0

for caloria in calorias:
    numero_calorias = numero_calorias + 1
    print(f"Refeição {numero_calorias}: {caloria}")

    soma = soma + caloria

media = soma / len(calorias)

print(f"A soma das calorias das refeições é igual a: {soma} \nA média é igual a: {media}")