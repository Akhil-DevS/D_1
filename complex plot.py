#This program is to plot complex numbers in graph
import numpy as np
import matplotlib.pyplot as plt

def distance(a,b ):
    dist=np.sqrt(((a.real-b.real)**2)+((a.imag-b.imag)**2))
    return(dist)
def complexplot():
    
    x=complex(input('\tEnter the FIRST complex number it the form a+bj\n\t'))
    y=complex(input('\tEnter the SECOND complex number it the form a+bj\n\t'))

    l=distance(x,y)
    round(l,1)
    dis1=str(l)
    plt.scatter(x.real,x.imag)
    plt.scatter(y.real,y.imag)
    plt.plot([x.real,y.real],[x.imag,y.imag],1)
    z=str(x)
    w=str(y)
    print("\nplot 1\ndistance between "+z+" and "+w+" is "+dis1)

    k=distance(0+0j,x)
    dis2=str(k)
    print("\nplot 2\ndistance of "+z+" from origin "+dis2)
    plt.scatter(x.real,x.imag)
    plt.plot([0,x.real],[0,x.imag])

    t=distance(0+0j,y)
    dis3=str(t)
    print("\nplot 3\ndistance of "+w+" from origin "+dis3)
    plt.scatter(y.real,y.imag)    
    plt.plot([0,y.real],[0,y.imag])
    plt.legend([z+" to "+w,"orgin to "+z," orgin to "+w])
    plt.show()


complexplot()
