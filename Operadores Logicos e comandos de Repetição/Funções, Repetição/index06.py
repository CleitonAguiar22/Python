usuario = "Admin"
senha = "12345"
digitUsuario = input("Digite seu usuario: ")
digitSenha = input("Digite sua senha: ")
while digitUsuario != usuario and digitSenha != senha:
    print("Usuário ou senha incorreta")
    digitUsuario = input("Digite seu usuario: ")
    digitSenha = input("Digite sua senha: ")
print("Seja bem vindo usuário administrador")
    