import re as regular_expression
 
class Matriz_Gauss_Jordan:
    def __init__(self, matriz:list, no_incognitas:int = 2) -> None:
        self.matriz_extendida = matriz
        self.filas = no_incognitas
        self.columnas = no_incognitas + 1

    
    def restar(self, fila_a:int , fila_b:int, multiplicador_a = 1, multiplicador_b = 1):
        for i in range(self.columnas):
            temp_1 = multiplicador_a * self.matriz_extendida[fila_a][i]
            temp_2 = multiplicador_b * self.matriz_extendida[fila_b][i]
            self.matriz_extendida[fila_a][i] = temp_1 - temp_2

    
    def sumar(self, fila_a:int , fila_b:int, multiplicador_a = 1, multiplicador_b = 1):
        for i in range(self.columnas):
            temp_1 = multiplicador_a * self.matriz_extendida[fila_a][i]
            temp_2 = multiplicador_b * self.matriz_extendida[fila_b][i]
            self.matriz_extendida[fila_a][i] = temp_1 + temp_2


    def multiplicar(self, fila, constante:float):
        for i in range(self.columnas):
            self.matriz_extendida[fila][i] = self.matriz_extendida[fila][i] * constante

    
    def intercambiar(self, fila_a:int , fila_b:int):
        for i in range(self.columnas):
            self.matriz_extendida[fila_a][i], self.matriz_extendida[fila_b][i] = self.matriz_extendida[fila_b][i], self.matriz_extendida[fila_a][i]


    def get(self, fila:int, columna:int):
        return self.matriz_extendida[fila][columna]


def traducir_ecuacion(ecuacion:str) -> list:
    lista_ecuacion = ecuacion.replace(" ", "").replace("=", ",").replace("-", ",-").replace("+", ",").split(",")
    
    if '' in lista_ecuacion:
        lista_ecuacion.remove('')

    for elemento in lista_ecuacion:
        if regular_expression.search("[a-z]$", elemento) and regular_expression.search("[0-9]", elemento):
            lista_ecuacion[lista_ecuacion.index(elemento)] = float(elemento[:-1])   
        elif regular_expression.search("[a-z]$", elemento):
            if '-' in elemento:
                lista_ecuacion[lista_ecuacion.index(elemento)] = -1.0
            else:
                lista_ecuacion[lista_ecuacion.index(elemento)] = 1.0
        else:
            lista_ecuacion[lista_ecuacion.index(elemento)] = float(elemento)

    return lista_ecuacion


def mostrar_matriz(matriz:list):
    for fila in matriz:
        print('|', end='')
        for j in range(len(fila)):
            if j == len(fila) - 1:
                print(f"⋮{fila[j]:^10.2f}", end='')
            else:
                print(f"{fila[j]:^10.2f}", end='')

        print('|')
    print()