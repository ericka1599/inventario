from producto import Producto
import pickle 
import os.path


def checkfile(archivo): 
    return os.path.exists(archivo)


if checkfile("productos.txt"):
	archivo = open ("productos.txt", 'rb' )
	lista = pickle.load (archivo)
	archivo.close()
else:
	lista = []

r =int(input("Desea ingresar un producto? si = 1 no = 2 ")) 

while r == 1 :
	nombre = input("Ingrese el nombre del producto: ")
	precio = float(input("Ingrese el precio: "))
	disponibilidad = int(input("Ingrese la disponibilidad: "))
	nuevo_producto = Producto(nombre, precio, disponibilidad)

	lista.append (nuevo_producto)

	r =int(input("Desea ingresar otro valor? si = 1 no = 2 "))

print (lista)
pickle.dump (lista , open("productos.txt" , "wb") )