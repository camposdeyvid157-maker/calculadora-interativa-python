from time import sleep


def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def maior_numero(a, b):
    return a if a > b else b


def pedir_numeros():
    while True:
        try:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            return n1, n2
        except ValueError:
            print('Erro! Digite apenas números inteiros.')


# Programa principal
n1, n2 = pedir_numeros()
opcao = 0

while opcao != 5:
    print(''' 
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
    ''')

    try:
        opcao = int(input('Qual a sua opção?: '))
    except ValueError:
        print('Opção inválida! Digite um número.')
        continue

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {somar(n1, n2)}')

    elif opcao == 2:
        print(f'{n1} x {n2} = {multiplicar(n1, n2)}')

    elif opcao == 3:
        print(f'O maior entre {n1} e {n2} é {maior_numero(n1, n2)}')

    elif opcao == 4:
        n1, n2 = pedir_numeros()

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida!')

    print('-' * 30)
    sleep(1.5)

print('Fim do programa. Volte sempre!')
