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

for valor in range(1, numero, 1):
    fat = numero * valor 
    #Por essa estrutura de repetição ir até o ponto anterior do ponto final, ele não multiplicaria por ele mesmo.

print(fat) 
