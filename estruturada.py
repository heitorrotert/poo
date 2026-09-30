nomes = []
notas = []
notas2 = []

def cadastrar():
    nome = input("Nome do estudante:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    
    nomes.append(nome)
    notas.append(nota1)
    notas2.append(nota2)
    print("Estudante cadastrado.")

def calcular_media():
    return (notas[-1] + notas2[-1]) / 2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

def lista():
    if len(nomes) == 0:
        print("Nenhum estudante cadastrado.")
        return

print(f"\n{'Nome':<16}{'Nota 1':<7}{'Nota 2':<7}{'Média':<8}{'Situação':<14}")

for i in range(len(nomes)):
    print(f"{nomes[i]:<16}{notas[i]:<7}{notas2[i]:<7}{calcular_media(i):<8.1f}{situacao(i):<14}")

def media_da_turma():
    if len(nomes) == 0:
        print("Nenhum estudante cadastrado.")
        return


    soma = 0 
    for i in range(len(nomes)):
        soma += calcular_media(i)
    print(f"\nMédia da turma: {soma/len(nomes):.2f}")

def menu():
    while True:
        print("\n1. Cadastrar estudante")
        print("2. Listar estudantes")
        print("3. Média da turma")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            lista()
        elif opcao == "3":
            media_da_turma()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")
menu()


    
