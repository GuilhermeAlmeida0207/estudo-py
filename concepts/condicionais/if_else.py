valor_quilo = 80.0
print(f"Nossos clientes aqui pagam R${valor_quilo} o quilo")
peso_prato = float(input("Qual o peso do prato do cliente em kg?: "))
valor_final = float(valor_quilo * peso_prato)

#O if, else e elif servem para impor condições no código
if peso_prato > 1:
    print(f"Como o peso do prato do seu cliente ultrapassou 1kg, o valor final cobrado será acima disso. Por isso, o valor final do cliente é igual a R${valor_final}")
elif peso_prato == 1:
    print(f"Como o peso do prato do seu foi igual a 1kg, o valor final cobrado será exatamente esse. Por isso, o valor final do cliente é igual a R${valor_final}")
else:
    print(f"Como o peso do prato do seu cliente não ultrapassou 1kg, o valor final cobrado será abaixo disso. Por isso, o valor final do cliente é igual a R${valor_final}")
