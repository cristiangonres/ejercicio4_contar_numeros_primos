def count_primos(rango_max):
    primo = True
    count = 0
    primos = []
    for i in range(2, rango_max+1):
        for x in range(2, i):
            if i % x != 0:
                print(f'Evaluando número {i}: ')
                print(f'{i } / {x} = {i/x} y su resto es {i % x}') 
                primo = True
            else:
                print(f'Evaluando número {i}: ')
                print(f'{i } / {x} = {i/x} y su resto es {i % x}') 
                primo = False
                break
        if primo:
            print(f'El número {i} es primo ')
            count += 1
            primos.append(i)
            
        else:
            print(f'El número {i} NO es primo ')
            
    return f'En el rango indicado, entre los números 0 e {i}, hay {count} números primos: \n {primos}'

print(count_primos(int(input('Introduzca el número hasta que el desee revisar los números primos: '))))