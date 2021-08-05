#!/usr/bin/python

#Script para verificar si una matriz se puede dividir en una posición tal que 
#la suma del lado izquierdo de la división sea igual a la suma del lado derecho.
#Entrada: Recibe la cantidad de elementos del array y los n elementos para llenar el array
#Salida: 1 cuando se localiza la posición buscada, -1 cuando no fue posible localizar la posición
# y 0 cuando el array es vacío

def canBeSplitted(array):
	if len(array) == 0 :
		#Array vacío
		return 0
	elif len(array) == 1 :
		#No es posible dividir el array en 2 partes para realizar las sumas
		return -1
	else :
		for i in range(1,len(array)):
			suma_izq = sum(array[0:i])
			suma_der = sum(array[i:])
			if suma_izq == suma_der :
				#Se localizó una posición que da las sumas iguales
				return 1
	#No se localizó ninguna posición que diera las sumas iguales
	return -1

if __name__ == '__main__':
	array = []
	try :
		n = int(input("Cantidad de elementos: "))
		i = 0
		while i < n:
			try :
				print("Elemento "+str(i+1)+": ",end='')
				elemento = int(input())
				array.append(elemento)
				i += 1
			except Exception as e:
				print("Insertar solo números enteros")

		print(canBeSplitted(array))
	except Exception as e:
		print("La cantidad solo es con números enteros")