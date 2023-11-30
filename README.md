# Codigo-Aplicadas-SVD
# SVD


# 1. Codigo a escala gris:
Este código Python proporciona una implementación básica de la compresión de imágenes en escala de grises mediante la descomposición de valores singulares (SVD). La técnica SVD se utiliza para descomponer la matriz de píxeles de una imagen en tres matrices: U, S y Vt, y así reducir la cantidad de información redundante.

# Requisitos
-Asegúrate de tener los siguientes requisitos antes de ejecutar el código:
-Python 3.x
-Bibliotecas: NumPy, Pillow (PIL)
-Puedes instalar las bibliotecas necesarias utilizando el siguiente comando: pip install numpy Pillow
# Uso
Descarga el código fuente a tu máquina local.
Abre el archivo compress_image.py y modifica la variable image_path con la ruta correcta de la imagen que deseas comprimir.
Ajusta el valor de num_components según tus preferencias. Este valor controla la cantidad de componentes singulares utilizados para comprimir la imagen, y afectará la calidad de la imagen comprimida.

Ejecuta el script:
python compress_image.py
El script comprimirá la imagen y guardará la versión comprimida como 'imagen_comprimida.png' en el directorio actual.

# Resultados
El script mostrará la imagen original y la imagen comprimida utilizando la biblioteca Pillow. Además, la matriz de valores singulares y la matriz Vt se imprimirán en la consola para su referencia.

# Notas
Ajusta el valor de num_components para equilibrar la calidad de compresión y el tamaño del archivo resultante.
Asegúrate de tener permisos de escritura en el directorio actual para guardar la imagen comprimida.
Este código está diseñado para imágenes en escala de grises. Si deseas trabajar con imágenes a color, se deben realizar modificaciones adicionales.
¡Disfruta explorando la compresión de imágenes con SVD!

# 2. Codigo con graficas

Este script en Python utiliza la descomposición de valores singulares (SVD) para aproximar y visualizar una imagen en escala de grises. La implementación utiliza la biblioteca Matplotlib y NumPy para cargar la imagen, realizar la descomposición SVD y mostrar las aproximaciones de la imagen para diferentes valores de r (rango).

# Requisitos
-Asegúrate de tener los siguientes requisitos antes de ejecutar el código:
-Python 3.x
-Bibliotecas: Matplotlib, NumPy
-Puedes instalar las bibliotecas necesarias utilizando el siguiente comando: pip install matplotlib numpy

# Uso
Descarga el código fuente a tu máquina local.
Abre el archivo image_approximation.py y modifica la variable image_path con la ruta correcta de la imagen que deseas cargar.

Ejecuta el script:
python image_approximation.py
El script cargará la imagen, realizará la descomposición SVD y mostrará las aproximaciones de la imagen para diferentes valores de r (rango).

# Resultados
El script generará visualizaciones de las aproximaciones de la imagen para diferentes valores de r utilizando la biblioteca Matplotlib. También mostrará gráficos de los valores singulares y la suma acumulativa de los valores singulares.

# Notas
Ajusta los valores en el bucle for r in (5, 20, 100): para controlar los diferentes rangos utilizados en la aproximación de la imagen.
Este script está diseñado para imágenes en escala de grises. Si deseas trabajar con imágenes a color, se deben realizar modificaciones adicionales.




