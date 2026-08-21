#----  Criação da lista  ----
lista = [10, 20, "textos"] #String precisa de "", numeros não. | 0, 1, 2...
# print(type(lista)) #Imprime type list

#----  Inserindo novos elementos  ----
lista.insert(0, "Oi") #Inserção de elemento na lista
# print(lista)

lista.append(30) #Inserção de elemento no final da lista
# print(lista)

#----  Imprimindo apenas itens específicos da lista  ----
# print(lista[2]) #Colocar o item entre colchetes, vai mostrar o 3 item da lista

# print(lista[-1]) #O -1 imprime o último valor, o -2 o penúltimo...

# print(lista[0:4]) #Mesma coisa que falar: Imprima do item 0 até o 4 -1

#----  Exibindo com loop  ----
for valor in lista:
    print(valor)

#----  Remover  ----
lista.pop() #Removendo último item da lista
# print(lista)

lista.remove(20) #Removendo item específico
# print(lista)

#Tamanho da lista
# print(len(lista))