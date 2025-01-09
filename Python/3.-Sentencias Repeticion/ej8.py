numero = int(input('Introduzca un número: '))


es_primo = True


if numero <= 1:
    es_primo = False
else:
    i = 2

    while i <= numero ** 0.5:
        if numero % i == 0:
            es_primo = False
            break
        i += 1


if es_primo:
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')
