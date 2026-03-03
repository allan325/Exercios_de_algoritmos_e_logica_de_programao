
while True:
    print("Sistema de login simples")

    usuario = input("Digite o usuário: ")
    senha = int(input("Digite a senha: "))
    
    if usuario == "admin" and senha == 1234:
        print("Login bem-sucedido!")
        break 
    else:
        print("Usuário ou senha errados. Tente novamente!")
        