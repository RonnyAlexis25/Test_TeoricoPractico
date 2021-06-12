def numeroAristas(grafo, objeto):
	#Se crea el diccionario con el conjunto de datos
	G={"a" : ["c"],
	"b" : ["c","e"],
	"c" : ["a","b","d","e"],
	"d" : ["c"],
	"e" : ["c","b"],
	"f" : []
	}

	#Se verifica si existe el grafo ingresado y se obtienen las claves y los valores
	if grafo in locals():
		vertices = list(G.keys())
		aristas = list(G.values())
	else:
		#Si no existe el grafo ingresado se muestra el mensaje
		return "El grafo no existe"

	#Se busca la clave ingresada en el grafo
	if objeto in vertices:
		#Se obtiene el indice de la clave
		pos = vertices.index(objeto)
		#Se guardan los valores de la clave correspondiente
		valores = aristas[pos]
		#Retorna el numero de valores
		return len(valores)
	else:
		#Si no existe el vértice ingresado se muestra el mensaje
		return "El vertice no existe"

while 1:
	#Se leen los datos de entrada
	grafo = input("Ingresar grafo: ")
	vertice = input("Ingresar vertice: ")
	aristas = numeroAristas(grafo, vertice)
	#Se impprime el numero de aristas del vertice ingresado
	print(aristas)

	#Si se ingresa 'q' en grafo termina el programa
	if grafo == "q":
		break