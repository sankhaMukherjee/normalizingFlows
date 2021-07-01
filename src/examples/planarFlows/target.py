import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf


def targetDensity(z):

    norm  = np.linalg.norm(z, axis=1)
    norm1 = 0.5 * (( norm - 4 )/0.4)**2

    exp1 = np.exp( -0.2 * ( (z[:,0] - 2)/0.8 )**2 )
    exp2 = np.exp( -0.2 * ( (z[:,0] + 2)/0.8 )**2 )
    exp  = np.log( exp1 + exp2 )

    return np.exp(  exp - norm1)

def targetDensityTF(z):

    norm  = tf.norm(z, axis=1)
    norm1 = 0.5 * (( norm - 4 )/0.4)**2

    exp1 = tf.math.exp( -0.2 * ( (z[:,0] - 2)/0.8 )**2 )
    exp2 = tf.math.exp( -0.2 * ( (z[:,0] + 2)/0.8 )**2 )
    exp  = tf.math.log( exp1 + exp2 )

    return tf.math.exp(  exp - norm1)


def main():

    x, y = np.linspace(-7, 7, 100), np.linspace(-7, 7, 100)
    xx, yy = np.meshgrid( x, y )
    
    z = np.vstack((xx.flatten(), yy.flatten())).T
    # rho = targetDensity( z )
    rho = targetDensityTF( z )
    rho = rho.numpy()
    rho = rho.reshape( xx.shape )

    plt.contour( xx, yy, rho, cmap=plt.cm.Blues )
    plt.savefig('results/img/target.png')
    plt.show()

    return

if __name__ == "__main__":
    main()
