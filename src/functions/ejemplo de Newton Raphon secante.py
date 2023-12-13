def secant_method(func, x0, x1, tolerance=1e-6, max_iterations=100):
    """
    Encuentra una raíz de la función utilizando el método de la secante.

    :param func: La función para la cual se busca la raíz.
    :param x0: El primer valor inicial.
    :param x1: El segundo valor inicial.
    :param tolerance: Tolerancia para la convergencia.
    :param max_iterations: Número máximo de iteraciones permitidas.
    :return: La aproximación de la raíz y el número de iteraciones.
    """
    x_prev = x0
    x_curr = x1

    for iteration in range(max_iterations):
        f_prev = func(x_prev)
        f_curr = func(x_curr)

        if f_curr - f_prev == 0:
            raise ValueError("La secante se volvió vertical. No se puede continuar.")

        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)

        if abs(x_next - x_curr) < tolerance:
            return x_next, iteration + 1

        x_prev = x_curr
        x_curr = x_next

    raise ValueError("El método de la secante no convergió después de {} iteraciones.".format(max_iterations))


# Definir la función
def func(x):
    return x**2 - 4

# Especificar valores iniciales
x0 = 3.0
x1 = 4.0

# Llamar al método de la secante
root, iterations = secant_method(func, x0, x1)

# Mostrar resultados
print("Raíz encontrada:", root)
print("Número de iteraciones:", iterations)
