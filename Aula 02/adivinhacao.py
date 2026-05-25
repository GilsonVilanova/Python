import random

def adivinhacao():
    numero = random.randint(1,100)
    #print(f"{numero}")
    
    print ("Adivinhe qual numero a maquina escolheu!") 
    while True:
        
        try:
            chute = int(input("Digite um numero de 1 a 100:  "))
            
            if chute == "":
                print("Você não digitou nada")
                continue
                
            if chute < 1 or chute > 100:
                print("\nDigite apenas numeros de 1 a 100\n")
                continue
            
            if chute < (numero):
                print("\nO numero é maior\n")
                
            elif chute > (numero):
                print("\nO numero é menor\n")
                
            else:
                print("\nVoce acertou!\n")
                input("\nPresione Enter para fechar o programa...")
                break
            
        except ValueError: 
            print("\nDigite um numero valido de 1 a 100\n")
            
adivinhacao()