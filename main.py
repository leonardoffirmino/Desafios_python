##Funções da aplicação

def add_contact(list_contacts,name,email,phone):
  info_add={"Name":name,"Email":email,"Phone":phone,"Favorito":False}
  list_contacts.append(info_add)
  
  print(f"Contato {name} foi incluido com sucesso!")
  return

def ver_lista():
  return


## Inicialização de lista 
list_contacts = []

## Inicio do programa para selecionar opção desejada
while True:
  print("\n Menu de agenda:")
  print("1. Criação de cadastro em agenda.")
  print("2. Visualisar itens de agenda.")
  print("3. Deletar cadastro da agenda.")
  print("4. Marcar como concluído item da agenda.")
  print("5. Editar cadastro da agenda.")
  print("7. Sair")

  input_choice = input("Digite sua esolha:")


  if input_choice == "1":
    name = input("Insira o nome do contato:")
    email = input("Insira o email de contato:")
    phone = input("Insira o telefone de contato:")
    add_contact(name,email,phone)
  elif input_choice =="2":
    ver_lista(list_contacts)
