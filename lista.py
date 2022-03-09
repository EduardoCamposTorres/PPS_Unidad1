# VARIABLES
minimo = 1
maximo = 20
lista = (6, 14, 11, 3, 2, 1, 15, 19)

# FUNCIONES
def estaEnRango(valor, minimo, maximo):
    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False


def estaEnLista(valor, lista):
    if estaEnRango(valor, minimo, maximo):
        for i in lista:
            if valor == i:
                return True
        return False

    else:
        return False



try:
    num = int(input("Introduzca un numero entre 1 y 20:"))

    if estaEnLista(num, lista):
        print("El número está en la lista")
    else:
        print("El número no está en la lista.")

except ValueError:
    print("El número no está en la lista")

except TypeError:
    print("El número no está en la lista")

except IndexError:
    print("El número no está en la lista")