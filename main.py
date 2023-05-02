from Clase_Conjunto import Conjunto
#def test():
#    A = Conjunto([1,2,3,4])
#    B = Conjunto([3,6,9])
#    print('La resta es: {}' .format(A - B))
if __name__ == "__main__":
    #test()
    A = Conjunto([1,2,3,4])
    B = Conjunto([3,6,9])
    print('Conjunto A: {}' .format(A))
    print('Conjunto B: {}' .format(B))
    print('1 - Unir los conjuntos A y B')
    print('2 - Obtener la diferencia del conjunto A menos B')
    print('3 - Saber si los conjuntos son iguales')
    print('0 - Salir')
    op = int(input('Ingrese su opcion:'))
    while op != 0:
        if op == 1:
            C = Conjunto([])
            C = (A + B)
            print('El nuevo conjunto C es: {}' .format(C))
        elif op == 2:
            print('El nuevo conjunto C es: {}' .format(A - B))
        elif op == 3:
            C = (A==B)
            if C == True:
                print('Los conjuntos son iguales')
            else: print('Los conjuntos no son iguales')
        print('1 - Unir los conjuntos A y B')
        print('2 - Obtener la diferencia del conjunto A menos B')
        print('3 - Saber si los conjuntos son iguales')
        print('0 - Salir')
        op = int(input('Ingrese su opcion:'))
    print('Fin del programa')
