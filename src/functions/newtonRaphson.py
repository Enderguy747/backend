
import sympy as sp

def newton_raphson(func, initialValue,fd, tolerance=1e-6, maxIterations=100):
    """
    Encuentra una raíz de la función utilizando el método de Newton-Raphson.

    :param func: La función para la cual se busca la raíz.
    :param func_deriv: La derivada de la función.
    :param x0: El valor inicial para comenzar las iteraciones.
    :param tolerance: Tolerancia para la convergencia.
    :param max_iterations: Número máximo de iteraciones permitidas.
    :return: La aproximación de la raíz y el número de iteraciones.
    """
    x = sp.symbols('x')
    
    funcion_sym = sp.sympify(func)
    funcion = sp.lambdify(x, funcion_sym)
    
    funcion_sym_deriv = sp.sympify(fd)
    funcionDeriv = sp.lambdify(x, funcion_sym_deriv)
    
   

    iv = initialValue
    
    for iteration in range(maxIterations):
        f_x = funcion(iv)
        print(f_x)
        f_prime_x = funcionDeriv(iv)
        print(f_prime_x)
        if abs(f_prime_x) < tolerance:
            raise ValueError("Derivada demasiado pequeña. Posiblemente no haya una raíz única.")

        iv = iv - f_x / f_prime_x

        if abs(f_x) < tolerance:
            return iv, iteration + 1

    raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones.".format(maxIterations))


# Definir la función y su derivada


# Especificar un valor inicial
initialValue = 3.0
tolerance = 1e-6
maxIterations=100
func="x**2-4"
fd="2*x"
# Llamar al método de Newton-Raphson
root, iterations = newton_raphson(func, fd,initialValue, tolerance, maxIterations)

# Mostrar resultados
print("Raíz encontrada:", root)
print("Número de iteraciones:", iterations)
