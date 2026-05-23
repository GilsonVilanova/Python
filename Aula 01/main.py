def calculadora():
    while True: #Laço de repeticao, fica nessa opcao ate digitar corretamente
        x = input("Primeiro número: ")  
        try:
            a = float(x.replace(",",".")) #O float tbem ser pra aceitar apenas numeros
            break
        except ValueError: 
            print("Digite apenas númeross.")
           
    while True: #
        op = input("Operador: - + * /: ")
        if op in ("-","+","*","/"):
            break
        print("Operador invalido, selecionar apenas - , + , * , / ")
            
        
    while True:    
        y = input("Segundo número: ")
        try:
            b = float(y.replace(",","."))
            break
        except ValueError:
            print("Digite apenas números.")
    

    if op == ('+'):
            res = a + b
    elif op == ('-'):
            res = a - b
    elif op == ('*'):
            res = a * b
    elif op == ('/'):
            res = a / b if b != 0 else "Inf"
    else:
            res = "Operador inválido"
    print(f"Resultado: {res}")

while True:  
    calculadora()
    continuar = input("Deseja calcular novamente? (s/n)").lower()
    if continuar != 's':
        input("\nPresione Enter para fechar o programa...") 
        break