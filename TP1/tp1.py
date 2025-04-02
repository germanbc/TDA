#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    
    # Armado de intervalos
    with open(archivo, 'r') as f:
        while True:
            linea = f.readline().strip()
            if linea and not linea.startswith("#"):
                break
        n = int(linea)
        transacciones = []
        
        for _ in range(n):
            t, e = map(int, f.readline().strip().split(','))
            minimo = t - e
            maximo = t + e
            transacciones.append((minimo, maximo, (t, e)))
        
        # Leer transacciones del sospechoso (ya ordenadas)
        sospechoso = [int(f.readline().strip()) for _ in range(n)]

    # Ordenamos los intervalos por su extremo derecho
    transacciones.sort(key=lambda x: x[1])

    coincidencias = []
    i = 0  # Índice para intervalos
    j = 0  # Índice para las transacciones del sospechoso

    # Recorremos las transacciones del sospechoso asegurando que cada una tenga una coincidencia óptima
    while j < n:
        encontrado = False
        while i < n:
            inicio, fin, intervalo = transacciones[i]
            if inicio <= sospechoso[j] <= fin:
                coincidencias.append((intervalo, sospechoso[j]))
                encontrado = True
                break  # Se encontró una coincidencia, pasamos al siguiente sospechoso
            i += 1
        
        if not encontrado:
            print("No es el sospechoso correcto")
            return
        
        j += 1

    # Si todas las transacciones encontraron coincidencia, imprimimos el resultado
    for (t, e), s in coincidencias:
        print(f"{s} --> {t} ± {e}")

if __name__ == "__main__":
    main()
