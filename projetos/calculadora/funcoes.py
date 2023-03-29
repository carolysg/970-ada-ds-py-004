def soma(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except:
        return f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}."

"""
def soma(a,b):
    if isinstance(a, (int,float)) and isinstance(b, (int,float)):
        return a + b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}.")
"""

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