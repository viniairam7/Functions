
def maior(* num):
    cont = maior = 0
    print('-' *30)
    print('Recebi novos valores. São eles: ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' -> Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')


# Programa Principal
maior(5, 7, 8, 4, 6)
maior(1, 2, 3)
maior(9,4)
maior()