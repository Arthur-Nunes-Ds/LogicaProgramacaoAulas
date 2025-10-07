#biblioteca só para interagir com o terminal 
from os import system as cmd
#var's:
#dicinario com cores/algumas fomataçãoes nele
sytile_str = {
    "red":"\033[31m",#<- text vermelho 
    "verde":"\033[32m", #<- text verde
    "amrelo":"\033[93m", #<- text amrelo
    "normal":"\033[0m", #<- text normal
    "negrito":"\033[1m" #<- negrito
}
tabuleiro = [ ["1","2","3"], ["4","5","6"], ["7","8","9"]]
tabuleiro_cord_x = [] # [(l,c),...] 
tabuleiro_cord_o = []
velha = False
is_cheio = False

def print_tabuleiro():
    l0 = ""
    l1 = ""
    l2 = ""
    #add linha a linha a l0,l1,l2
    for i in range(len(tabuleiro)):
        for x in tabuleiro[i]:
            if x in tabuleiro[0]:
                l0 += x
            elif x in tabuleiro[1]:
                l1 += x
            elif x in tabuleiro[2]:
                l2 += x

    def p_l(l):
        print(" "*43, end="")
        for i in range(3):
            print(f"|  {l[i]}  |  ", end="")
        return print()
    
    print(f"{"-="*25} Tabuleiro ={"-="*36}")
    #executa a fun 3vez de um vez
    p_l(l0);p_l(l1);p_l(l2)
    return

#aultualiza com o input do user e já ver se a jogada é legal
def is_legal_selecte(is_x = True,input_user = ""):
    #ver se a opção está dentro do range
    if input_user in ["1","2","3","4","5","6","7","8","9"]:
        #ignore é continua 
        pass
    else:
        len
        print(f"{sytile_str['red']}Digite uma opação valida!!{sytile_str['normal']}") 
        #erro de opção
        return False 
    
    #passa pela lista toda(Linha)
    for l in range(0,3):
        #passa pela lista toda(Coluna)
        for c in range(0,3):
            #ver a onde é o input do user dentro da matrix caso o play seja o X
            if input_user == tabuleiro[l][c] and is_x:
                if (l,c) not in tabuleiro_cord_o:
                    #adribui o "X" no tabuleiro
                    tabuleiro[l][c] = "X"
                    tabuleiro_cord_x.append((l,c))
                else:
                    print(f"{sytile_str['red']}Digite uma opeção que não esteja ocupada{sytile_str['normal']}") 
                    #jogada inlegal'
                    return False
            elif input_user == tabuleiro[l][c] and not is_x:
                if (l,c) not in tabuleiro_cord_x:
                    #adribui o "O" no tabuleiro
                    tabuleiro[l][c] = "O"
                    tabuleiro_cord_o.append((l,c))
                else:
                    print(f"{sytile_str['red']}Digite uma opeção que não esteja ocupada{sytile_str['normal']}") 
                    return False
                
    print_tabuleiro()
    #indica que a jogada é valida
    return True

#ver que ganhou
def vitoria():
    #função interna :)
    def is_velha():
        if len(tabuleiro_cord_x) == 5 and len(tabuleiro_cord_o) == 4:
            global is_cheio
            is_cheio = True
        else:
            return 
        
    #caso 1: linhas
    for l in range(0,3):
        #tira do arry e as: "
        Vline = "".join(tabuleiro[l])
        #ver quem ganhou
        if Vline == "XXX":
            print(f'{sytile_str['verde']}O: "X", ganhou ^.^{sytile_str["normal"]}')
            return True
        elif Vline == "OOO":
            print(f'{sytile_str['verde']}O: "O", ganhou ^.^{sytile_str["normal"]}')
            return True
        else:
            is_velha()
            pass

    #caso 2: colunas
    #quantida de colunas
    for c in range(0,3): 
        reperte_x = 0
        #aqui ele vai pega a tupla
        for cord_x in tabuleiro_cord_x:
            coluna_x = cord_x[1]
            if coluna_x == c:
                reperte_x += 1
        if reperte_x == 3:
            print(f'{sytile_str['verde']}O: "X", ganhou ^.^{sytile_str["normal"]}')
            return True
        else: 
            is_velha()
        
        reperte_o = 0
        for cord_o in tabuleiro_cord_o:
            coluna_o = cord_o[1]
            if coluna_o == c:
                reperte_o += 1
        if reperte_o == 3:
            print(f'{sytile_str['verde']}O: "O", ganhou ^.^{sytile_str["normal"]}')
            return True
        else:
            is_velha()
    
    #caso 3: diagonais        
    condador1_x = 0 ;condador2_x = 0
    for tx in tabuleiro_cord_x:
        if tx in [(0,0), (1,1), (2,2)]:
            condador1_x += 1
        if tx in [(0,2), (1,1), (2,0)]:
            condador2_x += 1

    if condador1_x == 3 or condador2_x == 3:
            print(f'{sytile_str['verde']}O: "X", ganhou ^.^{sytile_str["normal"]}')
            return True
    else:
        is_velha()

    condador1_o = 0 ;condador2_o = 0
    for to in tabuleiro_cord_o:
        if to in [(0,0), (1,1), (2,2)]:
            condador1_o += 1
        if to in [(0,2), (1,1), (2,0)]:
            condador2_o += 1
    if condador1_o == 3 or condador2_o == 3:
            print(f'{sytile_str['verde']}O: "O", ganhou ^.^{sytile_str["normal"]}')
            return True
    else:
        is_velha()
    
    return False
    
def game():
    global is_cheio
    def victory():
        if vitoria() or velha == True:
            print(25*"-=","Deseja jogar denovo? =",24*"-=")
            i_user = input("s = sim e n = não: ")
            #rest o jogo
            if i_user.upper() == "S":
             cmd("cls")
             #fala para o pytho que eu estou pegandoas var global's não declaranto outra var
             global tabuleiro, tabuleiro_cord_o, tabuleiro_cord_x
             #resta a matrix e limpa as vars de codernadas
             tabuleiro.clear()
             tabuleiro_cord_x.clear(),tabuleiro_cord_o.clear()
             tabuleiro = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
             is_cheio = False
             game()
            else:
             print(25*"-=","Ok tachu :) =",28*"-=")
             exit()
        else: 
            return
        
    print(25*"-=",f"Olá seja bem vindo aou jogo da velha. ={24*"-="}")
    print(25*"-=",f"O primeiro a jogar é o \"X\" ! ={29*"-="}")
    print(25*"-=",f"Precione enter para continuar. ={28*"-="}")
    input()
    #limpara a tela
    cmd("cls")
    print_tabuleiro()
    #não pode usar while True por que se não ele não pede o input do user por algum motivo
    while is_cheio == False:
        is_loop = True
        print(25*"-=",f"é vez do \"X\" ={34*"-="}")
        i_user = input("Digite o número que vócê quer colocar o \"X\": ")
        cmd("cls")
        #enquanto não for uma jogada legal ficara forçando o user a digita um jogada legal
        while not is_legal_selecte(True,i_user) and is_loop:
            print_tabuleiro()
            if is_legal_selecte(True,input("{}Opeção valida: {}".format(sytile_str['negrito'],sytile_str["normal"]))):
                is_loop = False
            victory()
        victory()
        #velha
        if is_cheio == True:
            print(15*"-=",f"{sytile_str['amrelo']} Que pena ninguem ganho deu impate quer joga denovo? {sytile_str['normal']}","="+11*"-=",sep="")
            i_user = input("s = sim e n = não: ")
            #rest o jogo
            if i_user.upper() == "S":
             cmd("cls")
             #fala para o pytho que eu estou pegandoas var global's não declaranto outra var
             global tabuleiro, tabuleiro_cord_o, tabuleiro_cord_x
             #resta a matrix e limpa as vars de codernadas
             tabuleiro.clear()
             tabuleiro_cord_x.clear(),tabuleiro_cord_o.clear()
             tabuleiro = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
             is_cheio = False
             game()
            else:
             print(25*"-=","Ok tachu :) =",28*"-=")
             exit()

        print(25*"-=","é vez do \"O\" =",34*"-=")
        i_user = input("Digite o número que vócê quer colocar o \"O\": ")
        cmd("cls")
        while not is_legal_selecte(False,i_user) and is_loop:
            print_tabuleiro()
            if is_legal_selecte(False,input("{}Opeção valida: {}".format(sytile_str['negrito'],sytile_str["normal"]))):
                is_loop = True
            victory()
        victory()

game()