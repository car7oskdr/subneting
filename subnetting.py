from MetodosSubnetting import metodosSub

# metodo para validar la IP.
def valida_ip():
    while True:
        try:
            str_ip = input('\n\tIngrese la IP: ')
            # dividir la IP.
            lista_ip = list(str_ip.split(sep = '.'))
            # conversión de valores de la lista a enteros.
            lista_ip_int = []
        
            for x in range(len(lista_ip)):
                lista_ip_int.append(int(lista_ip[x]))
            # if para saber si hay 4 elementos en la lista que conformen los cuatro octetos
            if len(lista_ip_int) == 4:
                break
            else:
                 print('Ip no valida favor de verificar.')
        except ValueError:
            print('IP no valida favor de verificar.')
    return lista_ip_int
            
    
while True:
    #menu de subnetting
    print('\n\t\t\=======>SUBNETTING<=======/\n')
    print('\t\t1.-Conocer la clase y mascara de red de una IP.')
    print('\t\t2.-Conocer la viabilidad del subneteo de un IP.')
    print('\t\t3.-Realizar subenetting.')
    print('\t\t4.-Salir\n')

    try:
        opc = int(input('Favor de eligir una opción: '))
        print('\n\n')

        if opc <= 0:
            print('=' * 85)
            print('\n\t\tHas ingresado un cero o un numero negativo')
            print('\t\tFavor de elegir un numero entero de la lista.\n')
            print('=' * 85)
        elif opc == 1:
            metodosSub(valida_ip(), 1)
        elif opc == 2:
            metodosSub(valida_ip(), 2)
        elif opc == 3:
            metodosSub(valida_ip(), 3)
        elif opc == 4:
            print('=' * 85)
            print('\n\t\t "Gracias por usar la app"\n')
            print('=' * 85)
            break
        else:
            print('=' * 85)
            print('\n\t El numero ingresado',opc,' esta fuera del rango de la lista, elige otra opción.\n\n')
            print('=' * 85)

    except ValueError:
        print('=' * 85)
        print('\n\tHas escogido un carater o ingresaste un numero con punto decimal.')
        print('\t\tFavor de elegir un numero entero de la lista.\n')
        print('=' * 85)
