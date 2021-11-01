from time import sleep

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

opção = 0

while opção != 7:

    print('''    [1] somar
    [2] Multiplicar
    [3] Subtrair
    [4] Dividir
    [5] Raiz quadrada
    [6] Novos numeros
    [7] Fechar o programa''')

    opção = int(input('Qual opção: '))
    if opção == 1:
        soma = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, mult))
    elif opção == 3:
        sub = n1 - n2
        print('O resultado de {} - {} é {}'.format(n1, n2, sub))
    elif opção == 4:
        div = n1 / n2
        print('O resultado de {} / {} é {}'.format(n1, n2, div))
    elif opção == 5:
        n1 = int(input('A raiz de qual numero você quer?: '))
        rai = n1 ** (1/2)
        print('A raiz de {} é {}'.format(n1, rai))
    elif opção == 6:
        print('informe os novos numeros')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif opção == 7:
        print('Encerrando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=' * 26)
    sleep(2)
print('Programa encerrado, volte sempre')