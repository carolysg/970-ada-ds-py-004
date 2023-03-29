def soma(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError
        return a + b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser int ou float, recebido {a} tipo {type(a)}, {b} tipo {type(b)}.")

def subtracao(a, b):
    return a - b