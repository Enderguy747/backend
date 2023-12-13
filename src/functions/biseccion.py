import sympy as sp

def biseccion(funcion_str, intervalo_inicial, intervalo_final, tolerancia=None, iteramax=10):
    
    x = sp.symbols('x')
    funcion_sym = sp.sympify(funcion_str)
    funcion = sp.lambdify(x, funcion_sym)
    
    # Verifica si el método de la bisección puede aplicarse
    if funcion(intervalo_inicial) * funcion(intervalo_final) >= 0:
        print("El método de la bisección no se puede aplicar.")
        return None


  
    # Inicializa listas para almacenar iteraciones y errores
    iteraciones = []

    # Método de la bisección
    for i in range(1, iteramax + 1):
        punto_medio = (intervalo_inicial + intervalo_final) / 2

        iteracion = {
            'Iteración': i,
            'Intervalo': (intervalo_inicial, intervalo_final),
            'a': intervalo_inicial,
            'f(a)': funcion(intervalo_inicial),
            'b': intervalo_final,
            'f(b)': funcion(intervalo_final),
            'xi': punto_medio,
            'f(xi)': funcion(punto_medio),
            'Error': None  # Se calculará en la siguiente iteración
        }

        # Verifica si la aproximación actual es una raíz exacta o si se cumple la tolerancia
        if iteracion['f(xi)'] == 0 or (tolerancia is not None and abs(iteracion['f(xi)']) < tolerancia):
            iteracion['Error'] = 0
            iteraciones.append(iteracion)
            break

        # Actualiza el intervalo [intervalo_inicial, intervalo_final] basado en el cambio de signo
        if funcion(intervalo_inicial) * funcion(punto_medio) < 0:
            intervalo_final = punto_medio
        else:
            intervalo_inicial = punto_medio

        # Calcula el error y agrega la iteración a la lista
        iteracion['Error'] = abs(iteracion['f(xi)'])
        iteraciones.append(iteracion)

    return iteraciones


funcion_str="exp(-x)-x"
intervalo_inicial=0
intervalo_final=1
tolerancia=0.01

# Ejecutar el método de la bisección con los parámetros ingresados por teclado
iteraciones = biseccion(funcion_str, intervalo_inicial, intervalo_final, tolerancia)

print(iteraciones)