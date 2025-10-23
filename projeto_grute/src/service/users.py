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
