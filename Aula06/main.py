from os import system,name 
import json

user = []
nome_arquivo = "" 

while True:
   #lamba = função de linha
   clear = lambda: system("cls" if name == "nt" else "clear")
   usuario = {}
   print("1 - Cadastra nome do user")
   print("2 - Salvar aqrqui JSON")
   print("3 - Fazer leitura JSON")
   print("4 - Sair")

   opcao = input("Informe uma opeção: ")
   clear()

   match opcao:
      case "1":
         usuario["noem"] = input("nome: ").strip().title() #title faz a Primeira Letra Fica Maiscula
         usuario["idade"] = input("iforme a idade: ")
         usuario["email"] = input("Dgite e-mail: ").strip().lower()

         user.append(usuario)
         clear()
         continue
      case "2":
         with open(f"Aulas06/a.json", "r", encoding="utf-8") as f:
            dd_extinte = json.load(f)
         
         dd_extinte.extend(usuario) # .extend(lst) -> junta lista
         
         with open(f"Aulas06/a.json", "w", encoding="utf-8") as f:
            json.dump(user, f, ensure_ascii=False, indent= 2) # dump(list/dic, arquivo_lido, formatação_anbt, intentação)
         clear()
         print("Arquivo salvo")
         continue
      case "3":
         with open(f"Aula06/a.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
         for i in dados:
            for n in i:
               print(f"{n.capitalize()}: {i.get(n)}") #capitilizer() --> chave; get() --> valor
      case "4":
         print("fim do programa exit")
         exit()
      case _:
         print("opção invalida")