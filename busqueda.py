import pickle 
from producto import Producto
archivo = open("productos.txt" , "rb")
listaB = pickle.load (archivo)


r = 1
while r == 1 :
	pro = input("Ingrese el nombre del producto que desea buscar: ")
	for Producto in listaB :
		if Producto.nombre == pro:
			proD = str(Producto.disponibilidad)
			proP = str(Producto.precio)
			print ("Disponibilidad: " + proD)
			print ("Precio: " + proP)
		else :
			print ("Ese producto no existe")
	r = int(input("Desea buscar otro producto? Si = 1 No = 2 "))




