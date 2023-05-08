from ClaseConjunto import Conjunto

if __name__ == '__main__':
    conjunto1 = Conjunto([1, 2, 3, 4])
    conjunto2 = Conjunto([4, 3, 2, 1])
    Conjunto.menu()
    opcion = int(input('Ingrese una opcion: '))
    Conjunto.opcionElegida(opcion)
    print(conjunto1 + conjunto2)