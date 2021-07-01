import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import Flow
import tensorflow as tf
tf.get_logger().setLevel('WARNING')

import matplotlib.pyplot as plt
import numpy as np 

from datetime import datetime as dt

def plotScatter(z, colors, now, k=0, epoch=0, nFlows=1):

    plt.figure()
    plt.scatter( z[:,0], z[:, 1], c = colors, edgecolors='None', alpha=0.5 )
    plt.savefig(f'results/img/z{k}_{now}_{epoch:06d}_{nFlows:06d}.png')
    plt.close()

    return

def main():

    now = dt.now().strftime('%Y-%m-%d--%H-%M-%S')
    nFlows = 10

    shape = (10000, 2)
    flow = Flow.Flow(dim=2, nFlows=nFlows, lr=1e-2)

    epochs = 1001

    losses = []

    for i in range(epochs):
        totalLoss, logQz0, logQzk, nll = flow.step(shape)
        losses.append( [totalLoss, logQz0, logQzk, nll] )

        print(f'[{i:5d}] => total = {totalLoss:7.2f}, Qzo = {logQz0:7.2f}, Qzk = {logQzk:7.2f}, nll = {nll:7.2f}')
    
        if i % 50 == 0:
            z0, zk, ldj, mu, logVar = flow(shape)
            z0 = z0.numpy()
            zk = zk.numpy()

            angles = np.angle(z0[:, 0] + z0[:, 1]*1j)
            angles = (angles - angles.min())/( angles.max() - angles.min() )
            colors = plt.cm.viridis( angles )

            plotScatter(z0, colors, now, k='0', epoch=i, nFlows=nFlows)
            plotScatter(zk, colors, now, k='k', epoch=i, nFlows=nFlows)


    losses = np.array(losses)



    plt.figure()
    plt.plot( losses[:, 0] )
    plt.savefig( 'results/img/lossTotal.png' )

    plt.figure()
    plt.plot( losses[:, 2] )
    plt.savefig( 'results/img/lossTotalQzk.png' )

    plt.figure()
    plt.plot( losses[:, 3] )
    plt.savefig( 'results/img/lossNll.png' )


    # plt.show()

    return

if __name__ == "__main__":
    main()

