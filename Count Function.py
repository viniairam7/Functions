from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-' * 30)
    print('VOCÊ GOSTA DE CONTAR? EU TAMBÉEM!.')
    print('-' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}  ', end='', flush=True)
            sleep(0.5)
            cont += p

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p


# Programa Principal
contador (1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de criar a contagem!')
ini = int(input('1° número: '))
fim = int(input('Último: '))
passo = int(input('De quanto em quanto:  '))
contador(ini, fim, passo)
print('Fim daS Contagens!')