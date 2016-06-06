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
	pro = input("Ingrese el nombre del producto: ")
	lista.append (pro)
	r =int(input("Desea ingresar otro valor? si = 1 no = 2 ")) 

print (lista)
pickle.dump (lista , open("productos.txt" , "wb") )