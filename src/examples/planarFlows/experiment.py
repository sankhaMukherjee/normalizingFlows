import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import Flow
import tensorflow as tf
tf.get_logger().setLevel('WARNING')

import matplotlib.pyplot as plt
import numpy as np 

from datetime import datetime as dt

import matplotlib as mpl
mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['text.usetex'] = True

def plotScatterMany(zks, now, epoch=0, nFlows=1):

    z0 = zks[0]
    angles = np.angle(z0[:, 0] + z0[:, 1]*1j)
    angles = (angles - angles.min())/( angles.max() - angles.min() )
    colors = plt.cm.plasma( angles )

    N = len(zks)

    maxColumns          = 5
    colSize,  rowSize   = 2, 2
    nColumns, nRows     = min(maxColumns, N), N // maxColumns + 1
    delX,     delY      = 1 / nColumns, 1/nRows

    plt.figure( figsize=( colSize*nColumns, rowSize*nRows ))
    axs = []
    for row in range(nRows):
        for col in range(nColumns):
            axs.append( plt.axes([col*delX, (nRows - row -1)*delY , delX, delY], facecolor='None') )

    for i, z in enumerate(zks):
        axs[i].scatter( z[:,0], z[:, 1], c = colors, edgecolors='None', alpha=0.5 )

    for i, ax in enumerate(axs):
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_xticks([])
        ax.set_yticks([])
        label = '$z_{' + f'{i}' + '}$'
        ax.text( -7, 7, label )
    
    plt.savefig(f'results/img/temp/{now}_z_{epoch:06d}_{nFlows:06d}.png')
    plt.close()

    return


def plotScatter(z, colors, now, k=0, epoch=0, nFlows=1):

    plt.figure()
    plt.scatter( z[:,0], z[:, 1], c = colors, edgecolors='None', alpha=0.5 )
    plt.savefig(f'results/img/temp/z{k}_{now}_{epoch:06d}_{nFlows:06d}.png')
    plt.close()

    return

def main():

    now = dt.now().strftime('%Y-%m-%d--%H-%M-%S')
    nFlows = 15

    shape = (10000, 2)
    flow = Flow.Flow(dim=2, nFlows=nFlows, lr=1e-2)

    epochs = 2000

    losses = []

    for epoch in range(epochs):
        totalLoss, logQz0, logQzk, nll = flow.step(shape)
        losses.append( [totalLoss, logQz0, logQzk, nll] )

        print(f'[{epoch:5d}] => total = {totalLoss:7.2f}, Qzo = {logQz0:7.2f}, Qzk = {logQzk:7.2f}, nll = {nll:7.2f}')
    
        if epoch % 50 == 0:
            zks, ldj, mu, logVar = flow(shape)
            plotScatterMany(zks, now, epoch=epoch, nFlows=nFlows)
            

    losses = np.array(losses)



    plt.figure()
    plt.plot( losses[:, 0] )
    plt.savefig( f'results/img/temp/{now}_lossTotal.png' )

    plt.figure()
    plt.plot( losses[:, 2] )
    plt.savefig( f'results/img/temp/{now}_lossTotalQzk.png' )

    plt.figure()
    plt.plot( losses[:, 3] )
    plt.savefig( f'results/img/temp/{now}_lossNll.png' )


    # plt.show()

    return

if __name__ == "__main__":
    main()

