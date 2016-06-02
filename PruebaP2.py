import pickle 
import os.path 
def checkfile(archivo): 
    return os.path.exists(archivo)

if checkfile("numeros.txt"):
	archivo = open ("numeros.txt", 'rb' )
	lista = pickle.load (archivo)
	archivo.close
else:
	lista = []

r =int(input("Desea ingresar un valor? si = 1 no = 2 ")) 
while r == 1 :
	n = input("Ingrese un numero: ")
	lista.append (n)
	r =int(input("Desea ingresar otro valor? si = 1 no = 2 ")) 

print (lista)
pickle.dump (lista, open("numeros.txt" , "wb") )