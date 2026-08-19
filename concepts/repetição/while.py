senha = ""
tentativa = 0 

while senha.upper() != "PYTHON":
    senha = input("Digite a senha secreta: ")
    tentativa += 1
print(f"Senha correta! Você acertou, a senha era {senha}!")
print(f"Foram necessárias {tentativa} tentativas para o acerto!")