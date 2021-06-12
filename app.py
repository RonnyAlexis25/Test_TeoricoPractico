#Se leen los datos de entrada
tipo = input("Tipo de log: ").upper()
entrada = input("Entrada: ")
salida = input("Salida: ")

try:
	#Se lee el archivo de entrada y se guarda en una lista
	with open(entrada) as archivo_entrada:
		cont = archivo_entrada.readlines()
		escritura = []
		#Se busca y se guardan las lineas con el tipo de log ingresado
		for line in cont:
			if tipo in line:
				escritura.append(line)
except FileNotFoundError as e:
	#Si no se encuentra el archivo de entrada se imprime el mensaje
	print("No existe el archivo de entrada")

with open(salida,"w") as archivo_salida:
	#Se crea un nuevo archivo y se escriben las lineas obtenidas 
	archivo_salida.write("".join(escritura))

print("Terminado")
