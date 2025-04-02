#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    
    # Armado de intervalos
    with open(archivo, 'r') as f:
        n = int(f.readline().strip())
        transacciones = []
        
        for _ in range(n):
            t, e = map(int, f.readline().strip().split(','))
            minimo = t - e
            maximo = t + e
            transacciones.append((minimo, maximo, (t, e)))
        
        # Leer transacciones del sospechoso (ya ordenadas)
        sospechoso= [int(f.readline().strip()) for _ in range(n)]


    # Ordenamos los intervalos por su extremo derecho
    transacciones.sort(key=lambda x: x[1])

    
    coincidencias = []
    i = 0  # Índice para intervalos
    j = 0  # Índice para las transacciones del sospechoso
    # Recorremos los intervalos ordenados y bucamos coincidencia entre las sospechosas y las del intervalo
    while i < n and j < n:
        inicio, fin, intervalo = transacciones[i]
        if inicio <= sospechoso[j] <= fin:
            coincidencias.append((intervalo, sospechoso[j]))
            j += 1
        i += 1
    
    es_coincidente = (j == n)  # Si coincidieron todas las transacciones, es la rata

    if es_coincidente:
        for (t, e), s in coincidencias:
            print(f"{s} --> {t} ± {e}")
    else:
        print("No es el sospechoso correcto")    

if __name__ == "__main__":
    main()