import random

#estrutura basica de uma class
class Personagem:
    '''construdor
    O self é obrigado dentro de todos metedos(fução)'''
    def __init__(self, nome, vida, dinheiro = 100):
        #atribudoos
        self.__nome = nome
        #__ siginifica que ele é privado ou seja ninguem pode acessar-lá
        self.__vida = vida

        self.__dinheiro = dinheiro
        self.__esta_vivo = True

    #decorador- metedo sem paretes
    @property
    #metedos
    def nome(self):
        return self.__nome

    #atualiza o uma metedo privado
    @nome.setter
    #só pode der um parametro como: (self, parametro)
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

    @property
    def dinheiro(self):
        return self.__dinheiro
    
    @dinheiro.setter
    def dinheiro(self, novo_valor):
        if novo_valor >= 0: 
            self.__dinheiro = novo_valor
        else:
            self.__dinheiro = 0

    @property
    def escudo_pontos(self):
        return self.__escudo_ponto
    
    @escudo_pontos.setter  
    def escudo_pontos(self, pontos):
        self.__escudo_ponto = pontos

    @property
    def esta_vivo(self):
        return self.__esta_vivo
    
    @esta_vivo.setter
    def esta_vivo(self, estado):
        self.__esta_vivo = estado

    def atacar(self, personagem, _PontoAtaca = 20):
        if not self.__esta_vivo:
            print(f"{self.nome} está morto e não pode atacar!")
            return
            
        if personagem.nome != self.nome:
            personagem.vida -= _PontoAtaca
            print(f"O {self.nome} atacou {personagem.nome} e tirou {_PontoAtaca} ponto de vida.\nE agora ele estar com {personagem.vida}")
            # Verifica se o personagem morreu e pega o dinheiro
            if personagem.verificar_vida(self):
                print(f"{self.nome} pegou {personagem.dinheiro} moedas do inimigo derrotado!")
        else:
            print("Você não pode atacar você mesmo")
    
    def verificar_vida(self, atacante):  # Removido o =None
        if self.vida <= 0 and self.__esta_vivo:
            self.__esta_vivo = False
            print(f"{self.nome} morreu em combate contra {atacante.nome}!")
            # Transfere o dinheiro sempre, já que só morre em combate
            atacante.dinheiro += self.dinheiro
            self.dinheiro = 0
            return True
        return False

#sub classes | Guerreiro é filho de Personagem <- isso é herença
class Guerreiro(Personagem):
    def __init__(self, nome, vida, dinheiro, escudo=False, escudo_ponto=1):
        super().__init__(nome, vida, dinheiro)
        self.__escudo = escudo
        self.__escudo_ponto = escudo_ponto

    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter
    def escudo(self, novo_valor):
        self.__escudo = novo_valor

    @property
    def escudo_ponto(self):  # Correção aqui
        return self.__escudo_ponto
    
    @escudo_ponto.setter
    def escudo_ponto(self, novo_valor):
        self.__escudo_ponto = novo_valor

    #modifica a função o metedot: atacar do pai(Personagem)
    def atacar(self, personagem):
        self.protecao()
        #para não ter que escrever o metedo atacar de novo <- isso é polimorfiso <=> protegido(_)
        super().atacar(personagem,45) 
    
    def protecao(self):
        if self.__escudo == True:
            self.vida += 10
            self.__escudo_ponto -= 1
            print(f"O {self.nome} usou o escudo. Tem mas {self.__escudo_ponto} de ponto do escudo.")
            if self.escudo_ponto <= 0:
                self.__escudo = False
                print(f"O {self.nome} não pode mas usar escudo.")
        return

class Mago(Personagem):
    def __init__(self, nome, vida, dinheiro):
        super().__init__(nome, vida, dinheiro)

    def atacar(self, personagem):
        super().atacar(personagem, 5)

    def cura(self, personagem):
        personagem.vida += 10
        print(f"O {self.nome} uso cura em {personagem.nome}")

class Arquiro(Personagem):
    def __init__(self, nome, vida, dinheiro, flechas = 10):
        super().__init__(nome, vida, dinheiro)
        self.__flechas = flechas
    
    @property
    def flechas(self):
        return self.__flechas 
    
    @flechas.setter
    def flechas(self, qnt_flechas):
        self.__flechas = qnt_flechas

    def atacar(self, personagem):
        if self.__flechas <= 0:
            super().atacar(personagem, 25)
        else:
            print(f"O {self.nome} não tem flechas")

class Mercado:
    def __init__(self):
        self.__produtos = {
            "Poção de Vida": [50, ["Mago", "Guerreiro", "Arqueiro"]],
            "Escudo": [100, ["Guerreiro"]],
            "Flechas": [30, ["Arqueiro"]],
        }

    def print_produtos(self):
        print("\n=== MERCADO ===")
        for produto, info in self.__produtos.items():
            preco, classes,ponto_escudo = info
            print(f"Produto: {produto}")
            print(f"Preço: {preco} dinheiro")
            print(f"Classes permitidas: {', '.join(classes)}")
            print("-" * 20)

    def comprar(self, personagem, produto):
        if produto not in self.__produtos:
            return f"Produto {produto} não encontrado!"
        
        preco = self.__produtos[produto][0]
        classes_permitidas = self.__produtos[produto][1]
        
        #ver o nome da class atraves do obj
        if personagem.__class__.__name__ not in classes_permitidas:
            return f"Sua classe não pode comprar {produto}!"
        
        if personagem.dinheiro < preco:
            return f"Dinheiro insuficiente! Faltam {preco - personagem.dinheiro} dinheiro"
        
        mensagem = ""

        match produto:
            case "Escudo10":
                personagem.dinheiro -= preco
                if not personagem.escudo :
                    personagem.escudo = True
                personagem.escudo_pontos += 10
                mensagem = "Escudo com 10 pontos equipado!"
            
            case "Escudo5":
                personagem.dinheiro -= preco
                if not personagem.escudo :
                    personagem.escudo = True
                personagem.escudo_pontos += 5
                mensagem = "Escudo com 5 pontos equipado!"
            
            case "Escudo1":
                personagem.dinheiro -= preco
                if not personagem.escudo :
                    personagem.escudo = True
                personagem.escudo_pontos += 1
                mensagem = "Escudo com 1 ponto equipado!"
            
            case "Flechas":
                personagem.dinheiro -= preco
                personagem.flechas += 10
                mensagem = "+10 flechas adicionadas!"
        
        return f"Compra realizada com sucesso! {mensagem}\nResta {personagem.dinheiro} dinheiro"
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, dinheiro, dano=15):
        super().__init__(nome, vida, dinheiro)
        self.__dano = dano
        self.__esta_vivo = True
        self.__tipo = self.__definir_tipo()

    @property
    def dano(self):
        return self.__dano
    
    @dano.setter
    def dano(self, novo_dano):
        if novo_dano > 0:
            self.__dano = novo_dano
    
    @property
    def tipo(self):
        return self.__tipo
    
    def __definir_tipo(self):
        """Define o tipo do inimigo baseado no nome"""
        tipos = {
            "Goblin": "Humanoide",
            "Orc": "Humanoide",
            "Troll": "Gigante",
            "Bandido": "Humano",
            "Lobo": "Besta"
        }
        return tipos.get(self.nome, "Desconhecido")

    def atacar(self, personagem):
        """Ataque específico do inimigo"""
        if self.esta_vivo:
            # Bônus de dano baseado no tipo
            bonus = {
                "Humanoide": 2,
                "Gigante": 5,
                "Humano": 1,
                "Besta": 3
            }.get(self.__tipo, 0)

            dano_total = self.__dano + bonus
            personagem.vida -= dano_total
            print(f"O {self.nome} ({self.__tipo}) atacou {personagem.nome} e causou {dano_total} de dano!")
            
            if personagem.verificar_vida(self):
                print(f"O {self.nome} derrotou {personagem.nome} e pegou {personagem.dinheiro} moedas!")
        else:
            print(f"O {self.nome} está morto e não pode atacar!")

    def drop_dinheiro(self, atacante):
        """Sistema de drop de dinheiro"""
        if not self.esta_vivo:
            dinheiro_drop = self.dinheiro
            bonus_aleatorio = random.randint(1, 10)  # Bônus aleatório
            dinheiro_total = dinheiro_drop + bonus_aleatorio
            
            atacante.dinheiro += dinheiro_total
            self.dinheiro = 0
            
            print(f"Você pegou {dinheiro_total} moedas! (Bônus: +{bonus_aleatorio})")
            return dinheiro_total
        return 0

    def verificar_vida(self, atacante):
        """Verifica se o inimigo morreu e dá as recompensas"""
        if self.vida <= 0 and self.esta_vivo:
            self.esta_vivo = False
            print(f"\n{self.nome} foi derrotado!")
            self.drop_dinheiro(atacante)
            return True
        return False