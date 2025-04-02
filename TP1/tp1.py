#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    
    # Armado de intervalos
    with open(archivo, 'r') as f:
        with open(archivo, 'r') as f:
            lineas = [line.strip() for line in f if not line.startswith("#")]  # Ignorar líneas con #

        n = int(lineas[0])
        transacciones = []

        for i in range(1, n + 1):
            t, e = map(int, lineas[i].split(','))
            minimo = t - e
            maximo = t + e
            transacciones.append((minimo, maximo, (t, e)))

        sospechoso = [int(line) for line in lineas[n + 1:]]

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
