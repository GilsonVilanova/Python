import random

def adivinhacao():
    numero = random.randint(1,10)
    #print(f"{numero}")
    
    
    while True:       
        try: 
            chute = int(input("Digite um numero de 1 a 10:  "))
            
            if chute == "":
                print("Você não digitou nada")
                continue
                
            if chute < 1 or chute > 10:
                print("\nDigite apenas numeros de 1 a 10\n")
                continue
            
            if chute < (numero):
                print("\nO numeor é maior\n")
                
            elif chute > (numero):
                print("\nO numeor é menor\n")
                
            else:
                print("\nVoce acertou!\n")
                break
            
        except ValueError: 
            print("\nDigite um numero valido de 1 a 10\n")
            
adivinhacao()