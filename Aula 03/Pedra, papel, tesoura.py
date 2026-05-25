import random

def jogo():
    opcoes = ["pedra","papel","tesoura"]
    
    computador = random.choice(opcoes)
    
    jogador = input("Escolha entre predra, papel ou tesoura e tente ganhar da maquina!\n\n")
    
    if jogador not in (opcoes):
        print("Opção invalida") 
        return
    
    print(f"\nO computador escolheu: {computador}")
    
    if (jogador == computador):
        print("\nO jogo empatou!!")
    
    elif ((jogador == "tesoura" and computador == "papel") or
          (jogador == "papel" and  computador == "pedra") or
          (jogador == "pedra" and computador == "tesoura")):
        print("Voce venceu")
        
    else:
        print("\nVoce perdeu!")
    
    input("Aperte enter para encerrar!")

jogo()