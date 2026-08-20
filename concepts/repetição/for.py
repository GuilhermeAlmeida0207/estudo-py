# For = Comando que inicia o laço de repetição | para
# contadora = variável criada
# in = dentro de 
# range() = É a função que gera a sequência de números. Seus 3 argumentos significam:
# 10 = ponto inicial
# 100 = ponto final
# 1 = de quanto em quanto vai pulando

# for contadora in range(10, 100, 1): 
#     print(contadora)

# Caso eu deseje imprimir só valores pares eu mudo o último número para 2

# Exemplo de número fatorial: 
numero = int(input("Informe o número que deseja descobrir o fatorial: "))
fat = numero #Por que o fat é = numero? Pois se mencionassemos o numero naquela conta, o valor de numero seria alterado pelo for e não seria o mesmo valor que o usuário digitou. Então, para manter o valor do número, criamos uma variável fat que recebe o valor de numero.

for valor in range(1, numero, 1):
    fat = fat * valor 
    #Por essa estrutura de repetição ir até o ponto anterior do ponto final, ele não multiplicaria por ele mesmo.
    print(valor) #Aqui colocamos o print dentro do for, pois queremos que ele imprima o valor a cada repetição. Se colocássemos fora, ele só imprimiria o último valor do for, que seria o penúltimo número do range.

print(f"\nFatorial de {numero} é igual a {fat}.") #Aqui colocamos o print fora do for, pois se colocássemos dentro, ele iria imprimir o valor do fatorial a cada repetição, e não no final.


