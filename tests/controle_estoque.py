#Sistema de controle de estoque de uma pequena loja de tecnologia.
# O programa reúne vários conceitos fundamentais de Python: listas, dicionários, funções, condicionais, repetições, entrada de dados e tratamento de erros

#Lista de dicionários
#Lista = Armazena vários produtos
#Dicionários = chave : valor | Chamar informação: produto["preco"] 
estoque = [
    {
        "nome": "Teclado", 
        "categoria": "Periféricos", 
        "preco": 120.50, 
        "quantidade": 10
    }
]

# def = Cria uma função, que organiza o código 
# for = Percorre cada produto da lista
# return = devolve um resultado ao usuário: Se encontrar, devolve um item do dicionário, caso não encontre, devolve None.

#Antes de exibir o menu, vou definir as funções para cada tópico dele.
# Encontrar Produto, Cadastrar Produto, Listar Produtos, Buscas Produtos, Adicionar Estoque, Remover Estoque, Exibir Resumo

#Função para encontrar produtos
def encontrar_produto(nome): 
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return produto

    return None

# Cadastro de produtos
#strip() = remove os espaços extras no começo e no final.
def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    elif encontrar_produto(nome) is not None:
        print("Esse produto já está cadastrado.")
        return

    categoria = input("Categoria: ").strip()

    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade inicial: "))
    except ValueError:
        print("Preço deve ser decimal e quantidade deve ser inteira.")
        return
    
    if preco <= 0:
        print("O preço deve ser maior que zero.")
        return

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso!")

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("O nome não pode ficar vazio.")
        return

    if encontrar_produto(nome) is not None:
        print("Esse produto já está cadastrado.")
        return

    categoria = input("Categoria: ").strip()

    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade inicial: "))
    except ValueError:
        print("Preço deve ser decimal e quantidade deve ser inteira.")
        return

    if preco <= 0:
        print("O preço deve ser maior que zero.")
        return

    if quantidade < 0:
        print("A quantidade não pode ser negativa.")
        return

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso.")


def listar_produtos():
    if len(estoque) == 0:
        print("O estoque está vazio.")
        return

    for produto in estoque:
        quantidade = produto["quantidade"]

        if quantidade == 0:
            status = "Esgotado"
        elif quantidade < 5:
            status = "Estoque baixo"
        else:
            status = "Disponível"

        print("\nNome:", produto["nome"])
        print("Categoria:", produto["categoria"])
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("Quantidade:", quantidade)
        print("Status:", status)


def buscar_produto():
    nome = input("Nome do produto: ").strip()
    produto = encontrar_produto(nome)

    if produto is None:
        print("Produto não encontrado.")
    else:
        print("Produto encontrado:", produto["nome"])
        print("Categoria:", produto["categoria"])
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("Quantidade:", produto["quantidade"])


def adicionar_estoque():
    nome = input("Nome do produto: ").strip()
    produto = encontrar_produto(nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade a adicionar: "))
    except ValueError:
        print("Digite uma quantidade inteira.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    produto["quantidade"] += quantidade
    print("Estoque atualizado com sucesso.")


def remover_estoque():
    nome = input("Nome do produto: ").strip()
    produto = encontrar_produto(nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade a remover: "))
    except ValueError:
        print("Digite uma quantidade inteira.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
    elif quantidade > produto["quantidade"]:
        print("Não há estoque suficiente.")
    else:
        produto["quantidade"] -= quantidade
        print("Saída registrada com sucesso.")


def exibir_resumo():
    if len(estoque) == 0:
        print("O estoque está vazio.")
        return

    total_itens = 0
    valor_total = 0
    produto_maior_estoque = estoque[0]

    for produto in estoque:
        total_itens += produto["quantidade"]
        valor_total += produto["preco"] * produto["quantidade"]

        if produto["quantidade"] > produto_maior_estoque["quantidade"]:
            produto_maior_estoque = produto

    print("\n========== RESUMO ==========")
    print("Produtos diferentes:", len(estoque))
    print("Total de itens:", total_itens)
    print("Produto com maior estoque:", produto_maior_estoque["nome"])
    print(f"Valor total do estoque: R$ {valor_total:.2f}")


while True:
    print("\n========== CONTROLE DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Adicionar estoque")
    print("5 - Remover estoque")
    print("6 - Exibir resumo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        adicionar_estoque()
    elif opcao == "5":
        remover_estoque()
    elif opcao == "6":
        exibir_resumo()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")