from service.produdo import *
from service.users import *

from getpass import getpass
from time import sleep as delay

def clear(t: float = 0.2): delay(t); return print('\033[H\033[J')

init()
user_id = None
user_email = None

def login():
    global user_id, user_email
    while True:
        clear()
        print("Sitema de login", end=2*"\n")
        print("Logar na conta - 1")
        print("Criar conta    - 2")
        print("Sair           - 3", end=2*"\n")
        input_user = input("Digite uma opção: ").strip()
        if input_user == "2":
            print("Criação de conta")
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            senha = getpass("Senha: ").strip()
            if cria_user(nome, email, senha):
                print("Usuário criado com sucesso. Faça login.")
                clear(1)
            else:
                print("Falha ao criar usuário.")
                clear(1)
        elif input_user == "1":
            print("Login")
            email = input("Email: ").strip()
            senha = getpass("Senha: ").strip()
            #retorna o id
            dados = logar(email, senha)  
            if dados is not None:
                user_id = dados
                user_email = email
                menu()
            else:
                print("Login falhou.")
                clear(1)
        elif input_user == "3":
            exit()
        else:
            print("Opção inválida")
            clear(0.8)

def menu():
    global user_id, user_email
    if user_id is None:
        print("Nenhum usuário logado.")
        clear(0.8)
        return login()
    while True:
        clear()
        print("1 - Mudar senha")
        print("2 - Deletar conta")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Vender produto")
        print("6 - Alterar produto")
        print("7 - Sair da conta")
        print("8 - Sair")
        input_user = input("Digite uma opção: ").strip()
        match input_user:
            case "1":
                #verifica senha atual e altera
                senha_atual = getpass("Senha atual: ").strip()
                
                if logar(user_email, senha_atual) is not None:
                    nova_senha = getpass("Nova senha: ").strip()
                    if restar_senha(user_id, nova_senha):
                        print("Senha alterada com sucesso.")
                    else:
                        print("Erro ao alterar senha.")
                else:
                    print("Senha atual incorreta.")
                clear(1)
            case "2":
                resp = input("Você tem certeza da ação? (S/N): ").strip().upper()
                if resp == "S":
                    if excluir_user(user_id):
                        print("Conta deletada. Voltando ao login.")
                        user_id = None
                        user_email = None
                        clear(1)
                        login()
                    else:
                        print("Erro ao deletar conta.")
                        clear(1)
                elif resp == "N":
                    continue
                else:
                    print("Opção inválida")
                    clear(1)
            case "3":
                desc = input("Nome do produto: ").strip()
                qn = input("Quantidade: ").strip()
                pr = input("Preço: ").strip()
                cadastrar_produtos(desc, pr, qn)
                clear(1)
            case "4":
                listar_produtos()
                input("Digite enter para continuar")
                clear()
            case "5":
                listar_produtos()
                print()
                _id = input("Digite o id do produto: ").strip()
                quantidade = input("Digite a quantidade a vender: ").strip()
                vender(_id, quantidade)
                print()
                listar_produtos()
                input("Digite enter para continuar")
                clear()
            case "6":
                listar_produtos()
                print()
                _id = input("Digite o id do produto: ").strip()
                desc = input("Nome do produto: ").strip()
                qn = input("Quantidade: ").strip()
                pr = input("Preço: ").strip()
                editar_produtos(_id, desc, pr, qn)
                print()
                listar_produtos()
                input("Digite enter para continuar")
                clear()
            case "7":
                user_id = None
                user_email = None
                print("Usuário deslogado")
                clear(1)
                login()
            case "8":
                exit()
            case _:
                print("Opção inválida")
                clear(0.8)

if __name__ == "__main__":
    login()