##Funções da aplicação

def add_contact(list_contacts,name,email,phone):
  info_add={"Name":name,"Email":email,"Phone":phone,"Favorito":False}
  list_contacts.append(info_add)
  
  print(f"Contato {name} foi incluido com sucesso!")
  return

def visualize_list(list_contacts):
  print("\n Contatos da agenda:")
  for indice,item in enumerate(list_contacts,start=1):
    status = "✓" if item["Favorito"] else "Não favorito" 

    print(f"{indice}. [{item['Name']} - {status} ]")
  return

def delete_contact(list_contacts):
  visualize_list(list_contacts)
  index_delete = int(input("Informe o indice  que deseja apagar!"))
  if 0 <= index_delete < len(list_contacts):
    del list_contacts[index_delete]
    print("Contato deletado de agenda!")
  else:
    print("Indice inválido!")
  return 


def add_contact_favorite(list_contacts):
  visualize_list(list_contacts)

  item_favorite = int(input("Favor informar qual indice deseja favoritar ou desmarcar em agenda!"))

  if 0 <= item_favorite < len(list_contacts):
    list_contacts[item_favorite]['Favorito'] = not list_contacts[item_favorite]['Favorito']
    print("Contato marcado ou desmarcado como favorito!")
  return


## Inicialização de lista 
list_contacts = []

## Inicio do programa para selecionar opção desejada
while True:
  print("\n Menu de agenda:")
  print("1. Criação de cadastro em agenda.")
  print("2. Visualisar itens de agenda.")
  print("3. Deletar cadastro da agenda.")
  print("4. Marcar como Favorito item da agenda.")
  print("5. Editar cadastro da agenda.")
  print("7. Sair")

  input_choice = input("Digite sua escolha:")


  if input_choice == "1":
    name = input("Insira o nome do contato:")
    email = input("Insira o email de contato:")
    phone = input("Insira o telefone de contato:")
    add_contact(list_contacts,name,email,phone)
  elif input_choice =="2":
    visualize_list(list_contacts)
  elif input_choice =="3":
    delete_contact(list_contacts)
  elif input_choice =="4":
    add_contact_favorite(list_contacts)
