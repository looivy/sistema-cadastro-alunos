#lista que armazena os alunos cadastrados
data = []

#funcao menu
def menu():
  while True:
    try:
      opcao = int(input("1. Adicionar aluno\n2. Listar Alunos\n3. Buscar Aluno\n4. Remover Aluno\n5. Mostrar média\n6. Sair\nEscolha uma opção: "))
    except ValueError:
      print("Digite uma opção válida.")
      continue

    match opcao:
      case 1:
        cadastrar()

      case 2:
        listar()

      case 3:
        buscar()
          
      case 4:
        remover()
        
      case 5:
        media()
          
      case 6:
        print("--- PROGRAMA ENCERRADO ---")
        break

      case _:
        print("Digite uma opção válida.")

#funcao cadastro de alunos
def cadastrar():
  print("--- ADICIONE O ALUNO ---")

  nome = input("Digite o nome completo do aluno: ").strip().upper()
  if not nome:
    print("Nome não pode ser vazio. Cadastro cancelado.")
    return

  try:
    idade = int(input("Digite a idade do aluno: "))
    nota1 = float(input("Digite a nota do aluno: [1/3]")) 
    nota2 = float(input("Digite a nota do aluno: [2/3]")) 
    nota3 = float(input("Digite a nota do aluno: [3/3]"))
  except ValueError:
    print("Valor inválido. Cadastro cancelado.")
    return

  aluno = {
    "Aluno": nome,
    "Idade": idade,
    "Media": round((nota1 + nota2 + nota3) /3, 2)
  }

  data.append(aluno)
  print(f"Aluno {nome} cadastrado.")

#funcao lista de alunos
def listar():
  print("--- ALUNOS CADASTRADOS ---")

  if not data:
    print("Nenhum aluno cadastrado ainda.")
    return

  for aluno in data:
    print(f"Nome: {aluno['Aluno']}")
    print(f"Idade: {aluno['Idade']}")
    print(f"Média: {aluno['Media']:.2f}")
    print("----------------------")

#funcao de busca de aluno
def buscar():
  print("--- BUSQUE ALUNO ---")

  if not data:
    print("Nenhum aluno cadastrado ainda.")
    return

  nome = input("Digite o nome completo ou parcial do aluno: ").strip().upper()

  encontrados = []
  for aluno in data:
    if nome in aluno["Aluno"]:
      encontrados.append(aluno)

  if encontrados:
    for aluno in encontrados:
      print(f"Aluno encontrado: {aluno['Aluno']} | Idade: {aluno['Idade']} | Média: {aluno['Media']:.2f}")
  else:
    print(f"Nenhum aluno encontrado com '{nome}'.")

#funcao de remover aluno cadastrado
def remover():
  print("--- REMOVER ALUNO CADASTRADO ---")

  if not data:
    print("Nenhum aluno cadastrado ainda.")
    return

  nome = input("Nome completo do aluno a ser removido: ").strip().upper()
  
  for aluno in data:
    if aluno["Aluno"] == nome:
      data.remove(aluno)
      print(f"Aluno {aluno['Aluno']} removido com sucesso.")
      break
  else:
    print(f"Aluno {nome} não encontrado.")

#funcao de mostrar media do aluno
def media():
  print("--- MÉDIA DO ALUNO ---")

  if not data:
    print("Nenhum aluno cadastrado ainda.")
    return
  
  nome = input("Nome do aluno que deseja ver a média: ").strip().upper()
         
  for aluno in data:
    if aluno["Aluno"] == nome:
      print(f"A média de {aluno['Aluno']} é {aluno['Media']:.2f}")
      break
  else:
    print(f"Aluno {nome} não encontrado.")   

if __name__ == "__main__":
  menu()