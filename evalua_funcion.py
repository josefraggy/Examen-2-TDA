"""
Ejercicio 1. Programa que Evalua la Función:
   y(x) = Σ [mi * e^(γ(x - xi)^2)] de i = 1 -> k
Donde:
   x, xi ∈ a los ℝ^n
   mi ∈ ℝ
   r ∈ ℝ > 0

Creado por: José Fragoso, 22/03/2019.

TODO: - Revisar el cambio que se hizo en la creación de arreglos.
      - Generar una mejor impresión en la terminal.
"""

import numpy as np
import math

# 1. Creamos los Datos.
def get_params():
	"""
	  Genera matrices y vectores para ser utilizados en la evaluación del
	  kernel RBF
	"""
	K = np.random.randint(5, 40)
	N = np.random.randint(2, 20)

	xi    = np.random.normal( 0,1,(K,N) )
	x     = np.random.normal( 0,1, N    )
	mi    = np.random.normal( 0,1,   K  )
	gamma = np.random.normal( 0,1,1     )

	return x,xi,mi,gamma

def main():
	x,xi,mi,gamma = get_params()

if __name__ == "__main__":
	main()

x,xi,mi,gamma = get_params()

# 3. Declaramos variables, len() nos da el tamaño del arreglo.
n = len(x)
k = len(xi)
elevado = 0
y = 0

# 4. Hacemos Operaciones.
for i in range(k):
    elevado        = np.dot(x, xi[i]) *  gamma
    multiplicacion = np.exp(elevado)  *  mi[i]
    y              = y     +    multiplicacion

# 5. Terminamos Imprimiendo el Resultado
print("El Resultado de la Función Evaluada es: %f" % (y))
