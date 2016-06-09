import pickle 
from producto import Producto
archivo = open("productos.txt" , "rb")
listaB = pickle.load (archivo)

r = 1
while r == 1 :
	encontrado = False 
	pro = input("Ingrese el nombre del producto que desea buscar: ")
	for producto in listaB :
		if producto.nombre == pro:
			proD = str(producto.disponibilidad)
			proP = str(producto.precio)
			print ("Disponibilidad: " + proD)
			print ("Precio: " + proP)
			encontrado = True 
	if not encontrado:
		print ("Ese producto no esta en la lista") 
	r = int(input("Desea buscar otro producto? Si = 1 No = 2 "))




