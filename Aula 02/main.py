def calculadora():
    x = input("Primeiro número: ")  
    op = input("Operador: - + * /: ")
    y = input("Segundo número: ")
    try:
        a = float(x.replace(",", "."))
        b = float(y.replace(",", "."))  
    exept ValueError:
        print("Entrada invalida.")
        return
    if op ==