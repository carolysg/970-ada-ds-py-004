from funcoes import soma
from funcoes import subtracao
from funcoes import divisao
from funcoes import multiplicacao

def calcule():
    a = input('Digite o primeiro número: ')
    b = input('Digite o segundo número: ')
    operacao = input('Digite a operação ("soma" ou +, "subtracao" ou -, "divisao" ou /, "multiplicacao" ou *): ')

    if operacao in ["soma", "+"]:
        print(f'O resultado é: {soma(a,b)}')
    
    elif operacao in ["subtracao", "-"]:
        print(f'O resultado é: {subtracao(a,b)}')

    elif operacao in ["divisao", "/"]:
        print(f'O resultado é: {divisao(a,b)}')

    elif operacao in ["multiplicacao", "*"]:
        print(f'O resultado é: {multiplicacao(a,b)}')

    else:
        print('Operação inválida!')