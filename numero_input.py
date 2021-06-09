def numero_input(numero):
    cont = 0
    for c in range(2, 9):
        if(numero == 1):
            cont = 1
        elif(not(numero % c)):
            cont = cont+1
            if(numero == c):
                cont -= 1
    if(cont == 0):
        return str(numero) + " es Primo !"
    else:
        return str(numero) + " No Primo :("

numero = input('Ingresa un numero: ')
print('*-'*10)
print(numero_input(int(numero)))
print('*-'*10)

# for o in range(1,100):

#     print(numero_input(int(o)))

