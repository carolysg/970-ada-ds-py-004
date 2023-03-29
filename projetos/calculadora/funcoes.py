def soma(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except:
        return f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}."

def subtracao(a, b):
    try:
        a = float(a)
        b = float(b)
        return a - b
    except:
        pass

def divisao(a, b):
    try:
        a = float(a)
        b = float(b)
        if b != 0:
            return a / b
        elif b == 0:
            print('Erro: Divisão inválida!')
            return 0 
    except:
        pass
    
def multiplicacao(a, b):
    try:
        a = float(a)
        b = float(b)
        return a * b
    except:
        return f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}."