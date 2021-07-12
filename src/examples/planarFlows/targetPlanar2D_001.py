import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf


import matplotlib as mpl

mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['text.usetex'] = True



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

    plt.figure(figsize=(3, 3))
    axs = [
        plt.axes([0,0,1,1], facecolor='None' ),
        plt.axes([0,0,1,1], facecolor='None' ),
    ]


    axs[0].contour( xx, yy, rho, cmap=plt.cm.Blues )
    axs[1].arrow(-6,  0, 12,  0, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')
    axs[1].arrow( 6,  0,-12,  0, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')
    axs[1].arrow( 0, -6,  0, 12, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')
    axs[1].arrow( 0,  6,  0,-12, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')

    for i in [4, 2, -2, -4]:
        axs[1].plot( [i, i], [-0.1, 0.1], 'k' )
        axs[1].plot( [-0.1, 0.1], [i, i], 'k' )
        axs[1].text( i, -0.2, f'{i}', ha='center', va='top' )
        axs[1].text( 0.2, i, f'{i}', ha='left', va='center' )
    
    
    for ax in axs:
        for s in ['right', 'top', 'left', 'bottom']:
            ax.spines[s].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim([-8, 8])
        ax.set_ylim([-8, 8])

    plt.savefig('results/img/target.png')
    # plt.show()

    return

if __name__ == "__main__":
    main()
