def soma(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError
        return a + b
    except TypeError:
        return f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}."

def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print('Erro: Divisão inválida!')
        return 0 
    
def multiplicacao(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError
        return a * b
    except TypeError:
        return f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}."