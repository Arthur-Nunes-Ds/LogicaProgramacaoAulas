from time import sleep as delay
import time
import random 

def dados_mago():
    numero_de_dados = 3

    resultados = []

    print("-" * 20) 

    for i in range(numero_de_dados):
        resultado = random.randint(1, 6) 
        print(f"Dado {i+1}: {resultado}")
        resultados.append(resultado)

    print("-" * 20)
    return resultados[0]+resultados[1]



def dados_guerreiro():
    numero_de_dados = 2

    resultados = []

    print("-" * 20) 

    for i in range(numero_de_dados):
        resultado = random.randint(1, 8) 
        print(f"Dado {i+1}: {resultado}")
        resultados.append(resultado)

    print("-" * 20)
    return resultados[0]+resultados[1]
    




class Personagem:

    def __init__(self, nome, vida):
     
        self.__nome = nome
        self.__vida = vida

  
    @property
    def nome(self):
        return self.__nome
    
  
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        

        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'agora esta com {personagem.vida}')




class Guerreiro(Personagem):
     def __init__(self, nome,  vida, escudo=False):
         super().__init__(nome, vida)
         self.__escudo = escudo

     @property
     def escudo(self):
         return self.__escudo
     
     @escudo.setter
     def escudo(self, escudo):
         self.__ = escudo



     def atacar(self, personagem):
         dadinho = dados_guerreiro()
         personagem.vida -= (dadinho)
         print(f'{self.nome} rolou {dadinho} {self.nome} atacou {personagem.nome} e tirou {dadinho} pontos de vida.')
         print(f'agora esta com {personagem.vida}')



     def protecao(self):
         self.__vida += 15





     def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

     @property
     def nome(self):
        return self.__nome
    
    
     @nome.setter
     def nome(self, novo_nome):
        self.__nome = novo_nome

     @property
     def vida(self):
        return self.__vida
    
     @vida.setter
     def vida(self, vida):
        self.__vida = vida

class Mago(Personagem):
     def __init__(self, nome,  vida):
         super().__init__(nome, vida)


     def atacar(self, personagem):
         dadinhos = dados_mago()
         personagem.vida -= (dadinhos)
         print(f'{self.nome} rolou {dadinhos} {self.nome} atacou {personagem.nome} e tirou {dadinhos} pontos de vida.')
         print(f'agora esta com {personagem.vida}')


     def curar(self, personagem):
        personagem.vida += 25 
        print(f'{self.nome} usou o poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')




jubirildo = Guerreiro('Jubirildo', 300)
gandof = Mago('Gandof', 200)

a = 0

while a != 5:
    a +=1
    print("=" * 40) 
    print('turno do Jubirildoi')
    print("=" * 40) 
    jubirildo.atacar(gandof)
    time.sleep(2)
    print("=" * 40) 
    print('turno do Gandof')
    print("=" * 40) 
    gandof.atacar(jubirildo)