#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: ./tp1.py ruta/a/entrada.txt")
        sys.exit(1)

    archivo = sys.argv[1]

    # Armado de intervalos
    with open(archivo, 'r') as f:
        lineas = [line.strip() for line in f if not line.startswith("#")]
    
    n = int(lineas[0])
    transacciones_originales = []

    for i in range(1, n + 1):
        t, e = map(int, lineas[i].split(','))
        minimo = t - e
        maximo = t + e
        # Guardamos (min, max, datos_originales, indice_original)
        transacciones_originales.append((minimo, maximo, (t, e), i - 1))

    # Leer transacciones del sospechoso (ya ordenadas)
    sospechoso = [int(lineas[i]) for i in range(n + 1, len(lineas))]

    transacciones_ordenadas = sorted(transacciones_originales, key=lambda x: x[1])

    coincidencias = []
    intervalos_usados = [False] * n  # Para rastrear qué intervalos originales (por índice) ya fueron asignados
    match_count = 0

    for j in range(n):
        s_j = sospechoso[j]
        mejor_intervalo_idx = -1 

        for i in range(len(transacciones_ordenadas)):
            inicio, fin, _, indice_original = transacciones_ordenadas[i]

            if not intervalos_usados[indice_original] and inicio <= s_j <= fin:
                mejor_intervalo_idx = i
                break  # Salimos del bucle interno, ya encontramos el mejor para s_j

        # Si encontramos un intervalo adecuado para s_j
        if mejor_intervalo_idx != -1:
            # Marcamos el intervalo original como usado
            indice_original_a_usar = transacciones_ordenadas[mejor_intervalo_idx][3]
            intervalos_usados[indice_original_a_usar] = True

            # Guardamos la coincidencia (datos originales del intervalo, s_j)
            datos_originales_intervalo = transacciones_ordenadas[mejor_intervalo_idx][2]
            coincidencias.append((datos_originales_intervalo, s_j))
            match_count += 1
        else:
            # Si para este s_j no encontramos ningún intervalo disponible, detenemos el proceso
            break

    # Verificamos si todas las transacciones del sospechoso fueron asignadas
    es_coincidente = (match_count == n)

    if es_coincidente:
        coincidencias.sort(key=lambda x: x[1])
        for (t, e), s in coincidencias:
            print(f"{s} --> {t} ± {e}")
    else:
        print("No es el sospechoso correcto")

if __name__ == "__main__":
    main()
