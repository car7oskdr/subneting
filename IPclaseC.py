from os import system
class claseC:
    # metodo inicial de la clase clasC
    def __init__(self, subredes, dir_ip):
        # variables de inicializaciń de la clase.
        system("clear")
        self.subredes = subredes
        self.dir_ip = dir_ip
        print('*' * 80)
        # mensaje de salida al utilizar la clase.
        ip_string = '.'.join(map(str, self.dir_ip))
        print('\n\tLa ip ',ip_string,'es clase C su mascara de red es: 255.255.255.0')
        print('\tEl número de subredes requerido son',self.subredes,'\n')
    # comprovación para saber si es viable el desarrollo de subneting.
        # pasar el número de subredes a binario.
        subredes_bin = bin(self.subredes)
        var_subred = (2**(len(subredes_bin) - 2)) - 2
        # creamos una lista para obtener el numero binario del ultimo octeto.
        lista_mascara = []

        for x in range(1, 9):
            if x <= (len(subredes_bin) - 2):
                lista_mascara.append(1)
            else:
                lista_mascara.append(0)
        # los valores de la lista los unimos en un solo valor y los pasamos a int.
        lista_str = ''.join(map(str, lista_mascara))
        # la variable "var_int" almacenara el valor decimal del último octeto.
        var_int = int(lista_str, 2)
        # finalmente comprobamos si es viable el subneteo y mostramos los mensajes.
        if var_subred >= self.subredes:
            print('\tEl desarrollo del subneting es viable.\n \tse comprobo con la formula: 2^#bit - 2 ≥ #subredes')
            print('\t\t\t',var_subred,'>=',self.subredes)
            print('\t\t La nueva mascara es: 255.255.255.' + str(var_int) + '\n')
            print('*' * 80)
        else:
            print('No es valido el desarrollo de subneting. 2^#bit - 2 !≥ #subredes')
            print('\t\n',var_subred,'!>=',self.subredes)
            print('*' * 80)
    
    def subnettin(self):
        pass