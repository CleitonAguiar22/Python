# Questão 01

pessoa = {
    "aluno":  "aluno",
    "nota01": 0,
    "nota02": 0,
    "nota03": 0,
    "media": 0,
    }

for i in range(1):
    pessoa["aluno"] = input("Digite o nome do aluno: ")
    print("Aluno registrado com sucesso!")
    pessoa["nota01"] = float(input("Digite a primeira nota do aluno " ))
    print("nota 01 registrada com sucesso!")
    pessoa["nota02"] = float(input("Digite a segunda nota do aluno ")) 
    print("nota 02 registrada com sucesso!")
    pessoa["nota03"] = float(input("Digite a terceira nota do aluno ")) 
    print("nota 03 registrada com sucesso!")
    pessoa["media"] = round((pessoa["nota01"] + pessoa["nota02"] + pessoa["nota03"]) / 3, 2)
print(pessoa)

# Questão 02

contatos = {
    }

while True:
    pergunta = int(input("Digite 1 para adicionar um novo contato, 2 para editar o contato ou 3 para remover um contato: "))
    if pergunta == 1:
        print("Opção escolhida: Adicionar um contato")
        usuario = input("Digite um nome do contato: ")
        print("Número registatrado com sucesso")
        contatos[usuario] = input("Digite um numero para este contato: ")
        print("Contato registrado com sucesso")
        print(contatos)
        pergunta02 = int(input("Digite 1 para sair ou 2 para fazer alguma outra ação: "))
        if pergunta02 == 2:
            continue
        elif pergunta02 == 1:
            break
    elif pergunta == 2:
        print("Opção escolhida: Edição de contatos")
        pergunta03 = input("Digite o nome do contato a ser editado: ")
        if pergunta03 in contatos:
            pergunta04 = int(input("Digite 1 para editar o nome do contato e 2 para editar o número do contato: "))
            if pergunta04 == 1:
                excluir = contatos.pop(pergunta03)
                usuario = input("Digite um nome do contato: ")
                contatos[usuario] = excluir
            elif pergunta04 == 2:
                contatos[usuario] = int(input("Digite um novo número de telefone: "))
                print("Número editado com sucesso")
        print("Contato editado com sucesso")
        print(contatos)
        pergunta05 = int(input("Digite 1 para sair ou 2 para fazer alguma outra ação: "))
        if pergunta05 == 2:
            continue
        elif pergunta05 == 1:
            break
    elif pergunta == 3:
        pergunta06 = input("Digite o nome do contato a ser removido: ")
        if pergunta06 in contatos:
            contatos.pop(usuario)
        print("Contato removido com sucesso: ", contatos)
        pergunta07 = int(input("Digite 1 para sair ou 2 para fazer alguma outra ação: "))
        if pergunta07 == 2:
            continue
        elif pergunta07 == 1:
            break
        
                                         
        
                 
