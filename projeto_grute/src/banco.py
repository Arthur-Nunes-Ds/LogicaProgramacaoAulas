import mysql.connector as mysql
from mysql.connector import IntegrityError
from dotenv import load_dotenv
from os import getenv
from passlib.hash import pbkdf2_sha256 as sha256

load_dotenv()

def _get_conn():
    return mysql.connect(
        host=getenv("host"),
        port=getenv("port"),
        user=getenv("user"),
        password=getenv("password"),
        database=getenv("database")
    )

def cria_user(nome, email, senha):
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        hashed = sha256.hash(senha)
        cursor.execute(
            "INSERT INTO user (NOME, EMAIL, SENHA) VALUES (%s, %s, %s)",
            (nome, email, hashed)
        )
        conn.commit()
        return True
    except IntegrityError as e:
        print("Erro cria_user: email já existe")
        return False
    except Exception as e:
        print(f"Erro cria_user : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def listar_usaurio():
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT NOME, EMAIL FROM user")
        usuarios = cursor.fetchall()
        if usuarios:
            print("Lista de user:")
            print("user | email |")
            for u in usuarios:
                print(" | ".join(str(x) for x in u))
        else:
            print("user não existe")
    except Exception as e:
        print(f"erro listar_usaurio() : {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def excluir_user(user_id):
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE ID=%s", (int(user_id),))
        conn.commit()
        print("o user deletado com sucesso")
        return True
    except Exception as e:
        print(f"erro excluir_user() : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def logar(email, senha):
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, SENHA FROM user WHERE EMAIL=%s", (email,))
        dado = cursor.fetchone()
        if dado:
            user_id, hashed = dado[0], dado[1] # type: ignore
            if sha256.verify(senha, hashed): # type: ignore
                return int(user_id) # type: ignore
            else:
                print("senha invalida")
                return None
        else:
            print("user não encontrado")
            return None
    except Exception as e:
        print(f"erro logar() : {e}")
        return None
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def restar_senha(user_id, nova_senha):
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        nova_hash = sha256.hash(nova_senha)
        cursor.execute("UPDATE user SET SENHA=%s WHERE ID=%s", (nova_hash, int(user_id)))
        conn.commit()
        print("senha alterada com sucesso")
        return True
    except Exception as e:
        print(f"Erro restar_senha : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

# produtos:
def cadastrar_produtos(Desc, Pr, Qn):
    conn = None
    try:
        # valida preço
        pr_str = str(Pr).replace(",", ".").strip()
        try:
            pr_val = float(pr_str)
            if pr_val < 0:
                print("preço abaixo do zero")
                return False
        except ValueError:
            print("insira um numero valido para o preço")
            return False

        # valida quantidade
        try:
            qn_val = int(Qn)
            if qn_val < 0:
                print("quantidade inválida")
                return False
        except ValueError:
            print("insira um numero inteiro para a quantidade")
            return False

        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (DESCRECAO, PR, QNT) VALUES (%s, %s, %s)",
            (Desc, pr_val, qn_val)
        )
        conn.commit()
        print("produto cadastrado com sucesso")
        return True
    
    except Exception as e:
        print(f"Erro cadastrar_produtos : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def listar_produtos():
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, DESCRECAO, PR, QNT FROM produtos")
        produtos = cursor.fetchall()
        if produtos:
            print("Lista de produtos:")
            print("id | descricao | R$ | QNT")
            for u in produtos:
                print(" | ".join(str(x) for x in u))
        else:
            print("produtos não existe")
    except Exception as e:
        print(f"Erro listar_produtos : {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def vender(prod_id, quantidade):
    conn = None
    try:
        prod_id = int(prod_id)
        quantidade = int(quantidade)
        if quantidade <= 0:
            print("quantidade inválida")
            return False

        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT QNT FROM produtos WHERE ID=%s", (prod_id,))
        dado = cursor.fetchone()
        if not dado:
            print("produto não encontrado")
            return False
        qnt_atual = int(dado[0]) # type: ignore
        novo_qnt = qnt_atual - quantidade

        if novo_qnt > 0:
            cursor.execute("UPDATE produtos SET QNT=%s WHERE ID=%s", (novo_qnt, prod_id))
        else:
            cursor.execute("DELETE FROM produtos WHERE ID=%s", (prod_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro vender : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def editar_produtos(prod_id, Desc, Pr, Qn):
    conn = None
    try:
        prod_id = int(prod_id)
        pr_str = str(Pr).replace(",", ".").strip()
        try:
            pr_val = float(pr_str)
            if pr_val < 0:
                print("preço abaixo do zero")
                return False
        except ValueError:
            print("insira um numero valido para o preço")
            return False

        try:
            qn_val = int(Qn)
            if qn_val < 0:
                print("quantidade inválida")
                return False
        except ValueError:
            print("insira um numero inteiro para a quantidade")
            return False

        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET DESCRECAO=%s, PR=%s, QNT=%s WHERE ID=%s",
            (Desc, pr_val, qn_val, prod_id)
        )
        conn.commit()
        print("produto alterado com sucesso")
        return True
    except Exception as e:
        print(f"Erro editar_produtos : {e}")
        return False
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def init():
    conn = None
    try:
        conn = _get_conn()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            ID INT PRIMARY KEY AUTO_INCREMENT,
            DESCRECAO VARCHAR(120) NOT NULL,
            PR FLOAT,
            QNT INT
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
            ID INT PRIMARY KEY AUTO_INCREMENT,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        )
        ''')
        conn.commit()
    except Exception as e:
        print(f"erro init_db(): {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
