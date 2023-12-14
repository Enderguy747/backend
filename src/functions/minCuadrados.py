
import math
from matplotlib import pyplot as plt
import numpy as np



def minCuadrados(xAxis,yAxis,parabola=0):
  
    if(len(xAxis)!=len(yAxis)):
        return ('uppss coordenates are not the same')
    else:
        numberColumn = xAxis
        oneColumn=[]
        powcolumn=[]
        
        for i in range(len(xAxis)):
            
            oneColumn.append(1)
            powcolumn.append(math.pow(xAxis[i],2))
            
        if(parabola==1):
            matrixA= np.array([oneColumn,numberColumn,powcolumn])
        else:
            matrixA= np.array([oneColumn,numberColumn])
             
        matrixB=np.array(yAxis)
        matrixATranspose = np.transpose(matrixA)
        ##matrix multiplication
        normalAXtrasnpose = np.dot(matrixA,matrixATranspose)
        normalBXtrasnpose = np.dot(matrixB,matrixATranspose)
       
        a = normalAXtrasnpose
        b = normalBXtrasnpose
        
        
        xValor=np.linalg.solve(a,b)
        
        plt.title('minimos cuadrados')
        
        if(parabola==1):
            plt.scatter(xAxis,yAxis)
            plt.xlabel("Edad")
            plt.ylabel("cantidad")
            plt.plot(xValor[0],xValor[1],xValor[2])
            ##plt.show()
            return ('y=',xValor[0],'+',xValor[1],'x',xValor[2],'x^2')
        else:
            plt.scatter(xAxis,yAxis)
            plt.xlabel("Edad")
            plt.ylabel("cantidad")
            plt.plot(xValor[0],xValor[1])
            ##plt.show()
            return ('y=',xValor[0],'+',xValor[1],'x') 
       
       
##minCuadrados([15,16,17,18,22,30],[40,45,55,60,70,80],1)