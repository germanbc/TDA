#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    
    with open(archivo, 'r') as f:
        #Leer cantidad de transacciones
        n = int(f.readline().strip())
        transacciones = []
        
        # Leer transacciones
        for _ in range(n):
            t, e = map(int, f.readline().strip().split(','))
            transacciones.append((t, e))
        
        # Leer transacciones del sospechoso (ya ordenadas)
        sospechoso= [int(f.readline().strip()) for _ in range(n)]
    print(transacciones)
    print(sospechoso)

if __name__ == "__main__":
    main()