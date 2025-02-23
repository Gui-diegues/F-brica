class calculadora():
  
  while True:
    n1 = float(input("Digite um número: "))
    op = input("Digite um operador mtemático: ")
    n2 = float(input("Digite outro número: "))

    if op == '+':
        resultado = n1 + n2
        print(f"{n1} {op} {n2} = {resultado}")
        
    elif op == '-':
        resultado = n1 - n2
        print(f"{n1} {op} {n2} = {resultado}")
        
    elif op == '/':
        resultado = n1 / n2
        print(f"{n1} {op} {n2} = {resultado:}")

    elif op == '*':
        resultado = n1 * n2
        print(f"{n1} {op} {n2} = {resultado:}")
    else:
        print("Por favor, digite um operador válido.")
        break
    
calculadora()
