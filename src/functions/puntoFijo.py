import sympy as sp

def puntoFijo(expresion_funcion,expresion_iteracion,valor_inicial:float,tolerancia:float):

    funcion_original = sp.sympify(expresion_funcion)

    funcion_iteracion = sp.sympify(expresion_iteracion)
    x=funcion_original
    # Establecer un número máximo de iteraciones
    max_iteraciones = 100

    # Aplicar el método del punto fijo
    error_actual = float('inf')  # Inicializar el error
    iteracion_actual = 0  # Contador de iteraciones
    valor_iteracion=0
    # Mostrar encabezado
    ##print("Iteración\tValor Actual\tError")
    iteraciones=[]
    while error_actual > tolerancia and iteracion_actual < max_iteraciones:
        valor_iteracion = funcion_iteracion.evalf(subs={sp.symbols('x'): valor_inicial})

        error_actual = abs(valor_iteracion - valor_inicial) / abs(valor_iteracion) if abs(valor_iteracion) != 0 else 0
        valor_inicial = valor_iteracion
        iteracion_actual += 1

        # Mostrar iteración y error en cada paso
        iteraciones.append({"iteracionActual":iteracion_actual,"valorInicial":valor_inicial,"errorActual":error_actual})

    # Mostrar el resultado final
    if iteracion_actual < max_iteraciones:
        return valor_iteracion,error_actual,iteracion_actual,iteraciones
    else:
        return (f"\nNo se encontró un punto fijo en {max_iteraciones} iteraciones.")

# Llamada a la función
"""""
x="2*tan(x)-4*x+5"
g="(2*tan(x*(3.14/180))+5)/4"
pi=1
tol=0.01
print(puntoFijo(x,g,pi,tol))
"""""