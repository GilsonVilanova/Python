def calculadora():
    x = input("Primeiro número: ")  
    op = input("Operador: - + * /: ")
    y = input("Segundo número: ")
    try:
        a = float(x.replace(",", "."))
        b = float(y.replace(",", "."))  
    except ValueError:
        print("Entrada invalida.")
        return
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

calculadora()