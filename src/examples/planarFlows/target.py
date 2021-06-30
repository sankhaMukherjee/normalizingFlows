import numpy as np 
import matplotlib.pyplot as plt

def targetDensity(z):

    z0, z1 = z[:,0], z[:,1]

    norm  = (z0**2 + z1**2)**0.5
    norm1 = 0.5 * (( norm - 4 )/0.4)**2

    exp1 = np.exp( -0.2 * ( (z0 - 2)/0.8 )**2 )
    exp2 = np.exp( -0.2 * ( (z0 + 2)/0.8 )**2 )
    exp  = np.log( exp1 + exp2 )

    return np.exp(  exp - norm1)

def main():

    x, y = np.linspace(-7, 7, 100), np.linspace(-7, 7, 100)
    xx, yy = np.meshgrid( x, y )
    
    z = np.vstack((xx.flatten(), yy.flatten())).T
    rho = targetDensity( z )
    rho = rho.reshape( xx.shape )

    plt.contour( xx, yy, rho, cmap=plt.cm.Blues )
    plt.show()

    return

if __name__ == "__main__":
    main()
    