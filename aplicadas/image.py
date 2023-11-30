import numpy as np
from PIL import Image

# Función para comprimir una imagen en escala de grises utilizando SVD
def compress_image(image_path, num_components):
    # Cargar la imagen
    original_image = Image.open(image_path)
    
    # Convertir la imagen a escala de grises
    gray_image = original_image.convert('L')
    image_matrix = np.array(gray_image)
    
    # Realizar la descomposición SVD
    U, S, Vt = np.linalg.svd(image_matrix, full_matrices=False)
    print(S)
    print(Vt)
    
    
    # Mantener solo un número limitado de componentes singulares
    S[num_components:] = 0
    
    # Reconstruir la imagen comprimida
    compressed_image_matrix = np.dot(U, np.dot(np.diag(S), Vt))
    
    # Convertir la matriz resultante en una imagen
    compressed_image = Image.fromarray(np.uint8(compressed_image_matrix))
    
    return original_image, compressed_image

if __name__ == '__main__':
    # Ruta de la imagen de entrada y número de componentes singulares a mantener
    image_path = r'C:\Users\angel\Documents\aplicadas\image.jpg'  # Reemplaza con la ruta correcta a tu imagen
    num_components = 9  # Puedes ajustar este valor para controlar la calidad de compresión

    # Comprimir la imagen
    original_image, compressed_image = compress_image(image_path, num_components)

    # Guardar la imagen comprimida
    compressed_image.save('imagen_comprimida.png')

    # Mostrar la imagen original y la imagen comprimida
    original_image.show()
    compressed_image.show()
    
