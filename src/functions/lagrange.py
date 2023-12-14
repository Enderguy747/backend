
import numpy as np
from sympy import lambdify, symbols, simplify
import matplotlib.pyplot as plt


x = symbols("x")

def polinomioFactory (xi,yi):
    polinomio = 0 
    for i in range(len(xi)):
        numerador = 1
        denominador =1
        for j in range(len(xi)):
            if j!=i:
                numerador*=(x-xi[j])
                denominador*=(xi[i]-xi[j])
        terminoL = numerador/denominador
        polinomio+=terminoL*yi[i]
    return polinomio
    
def valoresDelPolinomio(xi,yi):
    polinomio=polinomioFactory(xi,yi)
    polinomioSimplificado=simplify(polinomio)
    px=lambdify(x,polinomioSimplificado)
    muestras=100## tamaño de muestras
    a,b=min(xi),max(xi)
    pxi=np.linspace(a,b,muestras)
    pyi=px(pxi)
    return pxi.tolist(),pyi.tolist(),str(polinomio),str(polinomioSimplificado)

def grafico(xi,yi,pxi,pyi):
    plt.plot(xi,yi,"o",label="puntos")
    plt.plot(pxi,pyi,label="polinomio")
    plt.legend()
    ##plt.grid(1)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("interpolacion de lagrange")
    plt.show()
    ''''
xi=np.array([0,6,10,13,17,20,28])
yi=np.array([6.67,17.33,42.97,37.33,30.10,29.31,28.74])
'''  
