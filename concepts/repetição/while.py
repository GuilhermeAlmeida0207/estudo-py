senha = ""
tentativa = 0 

while senha.upper() != "PYTHON": #Colocamos o upper() para que o usuário possa digitar a senha em maiúsculo ou minúsculo, e ainda assim o programa aceitará, pois transformará a senha digitada em maiúsculo e comparará com a senha correta, que está em maiúsculo.
    senha = input("\nDigite a senha secreta: ")
    tentativa += 1
    if senha.upper() != "PYTHON":
        print(f"Senha incorreta! Não é {senha}, você nunca vai acertar muhahaha! Tente novamente!")

print(f"\nSenha correta! Você acertou, a senha era {senha}!")
print(f"\nForam necessárias {tentativa} tentativas para o acerto!")