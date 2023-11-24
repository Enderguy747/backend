
from sympy import symbols, simplify

import numpy as np

x = symbols('x')

def divDefNewton(xAxis, yAxis):

    #se crea la tabla de diferencias divididas
    ddTable = []
    for a in range(len(xAxis)+1):
        auxiliar = []     
        for y in range(len(xAxis)):
            auxiliar.append(0)   
        ddTable.append(auxiliar)


    for z in range (len(xAxis)):
        ddTable[0][z]=(xAxis[z])
        ddTable[1][z]=(yAxis[z])
    
    b=1
    c=1
    d=1

    for i in range(len(ddTable[0])):
        for j in range(len(ddTable[0])-b):
            ## formula de la tabla de diferencias
            ddTable[c+1][j] = (ddTable[c][j+1]-ddTable[c][j])/(ddTable[0][j+d]-ddTable[0][j])
            
        b+=1
        c+=1
        d+=1
    
    
    print('\n valores de los terminos: ')
    for l in range(len(ddTable[0])):
        print("a [",l,"] =",ddTable[l+1][0])



    print('\n')
    matrix=np.array(ddTable)
    matrix_transpose=np.transpose(matrix)
    print(matrix_transpose)
    
    #polinomio
    p = 0
    w = 0
    for t in range(len(ddTable[0])):
        terms = 1
        for r in range(w):
            terms*=(x-ddTable[0][r])
        w+=1
        p += ddTable[t+1][0]*terms
        
    print('\n polinomio entero')
    print(p)    
    print('\n polinomio simplificado')
    print(simplify(p))
        
    




m=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
n=[16,22,12,13,10,8,8,6,7,5,6,4,3,42,2,2]
divDefNewton(m,n)