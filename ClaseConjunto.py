class Conjunto():
    def __init__(self, conjunto = 0):
        self.__conjunto = conjunto
        
    def menu():
        print("***MENU DE OPCIONES***")
        print("1. Union")
        print("2. Diferencia")
        print("3. Igualdad")    
    
    def __add__(self, otro):
        union = None
        if type(self) == type(otro):
            union = list(self.__conjunto)
            for elem in otro.__conjunto:
                if not elem in union:
                    union.append(elem)
        return union
    
    def __sub__(self, otro):
        diferencia = None
        if type(self) == type(otro):
            diferencia = list(self.__conjunto)
            for eliminar in otro.__conjunto:
                if not eliminar in diferencia:
                    diferencia.pop(diferencia.index(eliminar))
        return diferencia
    
    def __eq__(self, otro):
        igualdad = None
        if type(self) == type(otro):
            igualdad = self.__conjunto == otro.__conjunto
        return igualdad
    
    def opcionElegida(self, opcion):
        match opcion:
            case 1:
                print(Conjunto.__add__(self))
            case 2:
                print(Conjunto.__sub__(self))
            case 3:
                print(Conjunto.__eq__(self))