#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]

    with open(archivo, 'r') as f:
        # Ignoramos líneas vacías y las que comienzan con '#'
        lineas = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    n = int(lineas[0])
    transacciones = []
    
    # Creamos los intervalos
    for i in range(1, n + 1):
        t, e = map(int, lineas[i].split(','))
        minimo = t - e
        maximo = t + e
        transacciones.append((minimo, maximo, (t, e)))

    # Ordenamos los intervalos por su extremo derecho
    transacciones.sort(key=lambda x: x[1])
    
    # Asumimos que los timestamps del sospechoso ya vienen ordenados
    sospechoso = [int(lineas[i]) for i in range(n + 1, 2 * n + 1)]

    coincidencias = []
    usados = set()  # Para no reutilizar intervalos

    j = 0  # Índice para las transacciones del sospechoso
    while j < n:
        i = 0 # Índice de las transacciones sospechosas
        encontrado = False
        while i < n:
            inicio, fin, intervalo = transacciones[i]
            if i not in usados and inicio <= sospechoso[j] <= fin:
                coincidencias.append((intervalo, sospechoso[j]))
                usados.add(i)
                encontrado = True
                break  # Se encontró una coincidencia, se pasa a la siguiente transacción del sospechoso
            i += 1
        
        if not encontrado:
            print("No es el sospechoso correcto")
            return
        
        j += 1

    # Si hubo coincidencia en todas las transacciones imprimimos el resultado
    for (t, e), s in coincidencias:
        print(f"{s} --> {t} ± {e}")

if __name__ == "__main__":
    main()
