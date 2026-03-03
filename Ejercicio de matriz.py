# escribir en dico duro una matriz de 100000 * 100000 de ceros y unos #

import numpy as np

with open("archivo.bin","wb") as file:   # tuve que buscar en internet como guardar archivos en el disco duro, ni idea de si si se guarda en disco duro, me dio mucho miedo probarlo 
    file.write(data)
    n= 100000
    matriz_np = np.random.randint(2, size=(n, n))
    np.save("archivo.npy", matriz_np)