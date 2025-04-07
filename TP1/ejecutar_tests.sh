#!/bin/bash

# Directorio donde están los archivos de prueba
directorio="/home/german/Documentos/TDA/TP1/CasosDePrueba"

# Verifica que el directorio existe
if [ ! -d "$directorio" ]; then
    echo "El directorio $directorio no existe."
    exit 1
fi

# Recorre todos los archivos en el directorio y ejecuta el script tp1.py
for archivo in "$directorio"/*; do
    if [ -f "$archivo" ]; then
        echo "Ejecutando con: $archivo"
        ./tp1.py "$archivo"
        echo "----------------------------------"
    fi
done

