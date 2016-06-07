class Producto():
	def __init__(self, nombre, precio, disponibilidad):
		self.nombre = nombre
		self.precio = precio
		self.disponibilidad = disponibilidad

	def __str__(self):
		return "Producto(%s, %s, %s)" % (self.nombre, self.precio, self.disponibilidad)

	def __repr__(self):
		return "Producto(%s, %s, %s)" % (self.nombre, self.precio, self.disponibilidad)