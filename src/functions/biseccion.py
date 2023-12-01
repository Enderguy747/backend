import math


def biseccion(funcion, intervalo_inicial, intervalo_final, tolerancia=None, pasos=10):
    # Verifica si el método de la bisección puede aplicarse
    if funcion(intervalo_inicial) * funcion(intervalo_final) >= 0:
        print("El método de la bisección no se puede aplicar.")
        return None

    # Calcula el número de pasos basado en la tolerancia
    if tolerancia is not None:
        pasos = math.ceil(math.log((intervalo_final - intervalo_inicial) / tolerancia) / math.log(2))

    # Inicializa listas para almacenar iteraciones y errores
    iteraciones = []
    errores = []

    # Método de la bisección
    for n in range(pasos + 1):
        punto_medio = (intervalo_inicial + intervalo_final) / 2

        iteraciones.append(punto_medio)
        error = abs(funcion(punto_medio))
        errores.append(error)

        # Verifica si la aproximación actual es una raíz exacta
        if funcion(punto_medio) == 0:
            return punto_medio, iteraciones, errores

        # Actualiza el intervalo [intervalo_inicial, intervalo_final] basado en el cambio de signo
        if funcion(intervalo_inicial) * funcion(punto_medio) < 0:
            intervalo_final = punto_medio
        else:
            intervalo_inicial = punto_medio

    # Devuelve la aproximación de la raíz y las listas de iteraciones y errores
    return (intervalo_inicial + intervalo_final) / 2, iteraciones, errores

# Ingresar la función por teclado
funcion_str = input("Ingrese la función (utilice 'x' como la variable independiente): ")

# Convertir la cadena de la función a una función de Python utilizando eval
funcion = lambda x: eval(funcion_str)

# Ingresar los demás parámetros por teclado
intervalo_inicial = float(input("Ingrese el extremo izquierdo del intervalo: "))
intervalo_final = float(input("Ingrese el extremo derecho del intervalo: "))
tolerancia = float(input("Ingrese la tolerancia: "))
pasos = int(input("Ingrese el número de pasos: "))

# Ejecutar el método de la bisección con los parámetros ingresados por teclado
resultado, iteraciones, errores = biseccion(funcion, intervalo_inicial, intervalo_final, tolerancia, pasos)  # type: ignore

# Muestra los resultados y comentarios
print(f"Aproximación de la raíz: {resultado}")
print("\nIteraciones y Errores:")
for i, (iteracion, error) in enumerate(zip(iteraciones, errores)):
    print(f"Iteración {i + 1}: {iteracion}, Error: {error}")



'''
Nota: La variable pasos en el código representa el número máximo de iteraciones que realizará el método de la bisección.
En cada iteración, el método divide el intervalo actual a la mitad y evalúa en qué subintervalo ocurre un cambio de signo en la función.
Este proceso se repite hasta que se alcanza la tolerancia deseada o se alcanza el número máximo de iteraciones.
'''