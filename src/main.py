import uso_matrices as matrices
from uso_matrices import Matriz_Gauss_Jordan

num_incognitas = 3
sistema_ecuaciones = []

for i in range(num_incognitas):
    sistema_ecuaciones.append(matrices.traducir_ecuacion(input(f"Introduce ecuacion #{i + 1}: ")))

matriz = Matriz_Gauss_Jordan(sistema_ecuaciones, num_incognitas)
matrices.mostrar_matriz(matriz.matriz_extendida)
print()

try:
    no_incognita = 0
    for i in range(matriz.filas):
        matriz.multiplicar(i, (1/matriz.get(i, i)))
        
        for j in range(matriz.filas):
            pivot = i
            if j != i:
                matriz.restar(j, pivot, multiplicador_b = matriz.get(j, pivot))
                matrices.mostrar_matriz(matriz.matriz_extendida)
    
    for i in range(matriz.filas):
        print(f"{chr(ord('a') + no_incognita)} = {matriz.get(i, matriz.columnas - 1):.02f}")
        no_incognita += 1
                
except ZeroDivisionError:
    es_infinito = False
    filas_revisadas = 0
    while (not es_infinito) and (filas_revisadas < matriz.filas):
        for j in range(matriz.columnas):
            es_infinito = matriz.get(filas_revisadas, j) == 0
            
        filas_revisadas += 1

    if es_infinito:
        print("El sistema de ecuaciones tiene infinitas soluciones")
    else:
        print("El sistema de ecuaciones no tiene solución")
