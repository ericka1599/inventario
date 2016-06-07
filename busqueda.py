r = int(input("Desea buscar un producto? si = 1 no = 2"))
if r == 1 :
	archivo = open("productos.txt" "rb")
	pro = input("Ingrese el nombre del producto que desea buscar: ")
	listaB = pickle.load (archivo)
	pro.lower ()
	
