from personagems import * 
import time
import random

limpar_tela = lambda : print('\033[H\033[J')

def mostrar_status(jogador, inimigo):
    print(f"\n{'='*40}")
    print(f"JOGADOR: {jogador.nome}")
    print(f"Vida: {jogador.vida} | Dinheiro: {jogador.dinheiro}")
    print(f"\nINIMIGO: {inimigo.nome}")
    print(f"Vida: {inimigo.vida}")
    print(f"{'='*40}\n")

def criar_personagem():
    limpar_tela()
    print("=== CRIAÇÃO DE PERSONAGEM ===")
    nome = input("Digite o nome do seu personagem: ")
    
    print("\nEscolha sua classe:")
    print("1 - Guerreiro (Forte e resistente)")
    print("2 - Mago (Usa magia e pode curar)")
    print("3 - Arqueiro (Ataque à distância)")
    
    while True:
        escolha = input("\nSua escolha (1-3): ")
        if escolha == "1":
            return Guerreiro(nome, vida=100, dinheiro=50)
        elif escolha == "2":
            return Mago(nome, vida=80, dinheiro=50)
        elif escolha == "3":
            return Arquiro(nome, vida=90, dinheiro=50, flechas=15)
        else:
            print("Escolha inválida!")

def criar_inimigo(nivel):
    nomes = ["Goblin", "Orc", "Troll", "Bandido", "Lobo"]
    nome = random.choice(nomes)
    vida = 50 + (nivel * 10)
    dano = 10 + (nivel * 2)
    dinheiro = 30 + (nivel * 20)
    return Inimigo(nome, vida, dinheiro, dano)

def menu_combate(jogador):
    print("\nSuas ações:")
    print("1 - Atacar")
    if isinstance(jogador, Guerreiro):
        print("2 - Usar escudo")
    elif isinstance(jogador, Mago):
        print("2 - Curar")
    elif isinstance(jogador, Arquiro):
        print("2 - Verificar flechas")
    print("3 - Fugir")
    return input("\nSua escolha: ")

def main():
    while True:  
        jogador = criar_personagem()
        nivel = 1
        
        while jogador.esta_vivo:
            limpar_tela()
            print(f"\n=== NÍVEL {nivel} ===")
            inimigo = criar_inimigo(nivel)
            
            print(f"\nUm {inimigo.nome} apareceu!")
            time.sleep(1)
            
            while inimigo.esta_vivo and jogador.esta_vivo:
                mostrar_status(jogador, inimigo)
                acao = menu_combate(jogador)
                
                if acao == "1":
                    jogador.atacar(inimigo)
                elif acao == "2":
                    if isinstance(jogador, Guerreiro):
                        jogador.protecao()
                    elif isinstance(jogador, Mago):
                        jogador.cura(jogador)
                    elif isinstance(jogador, Arquiro):
                        print(f"Você tem {jogador.flechas} flechas restantes")
                        time.sleep(1)
                elif acao == "3":
                    print("\nVocê fugiu da batalha!")
                    jogador.esta_vivo = False
                    break
                
                if inimigo.esta_vivo:
                    time.sleep(1)
                    inimigo.atacar(jogador)
                    time.sleep(1)
            
            if jogador.esta_vivo:
                print(f"\nVocê derrotou o {inimigo.nome}!")
                nivel += 1
                time.sleep(2)
        
        print("\nGAME OVER!")
        print(f"Você chegou até o nível {nivel}")
        print(f"Dinheiro acumulado: {jogador.dinheiro}")
        
        while True:
            escolha = input("\nDeseja jogar novamente? (S/N): ").upper()
            if escolha in ['S', 'N']:
                break
            print("Opção inválida! Digite S para Sim ou N para Não")
        
        if escolha == 'N':
            print("\nObrigado por jogar!")
            break
        
        limpar_tela()

if __name__ == "__main__":
    main()