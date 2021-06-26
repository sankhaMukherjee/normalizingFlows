import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['text.usetex'] = True

def get2Ddensity(ys, mean, cov):
    '''given a set of values, generate the PDF function for each point

    Given a particular Gaussian density, this function is going to
    calcualte the value of the PDF for each point passed. The values
    for the mean and covariance matrices should also be passed. The
    assumption here is that this is a 2D distribution, although there
    is nothing preventing thsi function to be extended to a more
    generalized function.

    Parameters
    ----------
    ys : numpy.ndarray (N,2)
        This contains samples form a multivariate normal distribution.
        Each row corresponds to a new sample, and each column corresponds
        to an element of the vector.
    mean : numpy.ndarray (2,)
        This is the mean value of the array
    cov : numpy.ndarray (2,2)
        This is the covariance matrix of the array
    '''

    N = len(ys)

    ysC   = ys.reshape( (N, 2, 1) ) # This is a series of column vectors -> y
    ysR   = ys.reshape( (N, 1, 2) ) # This is a series of row vectors    -> yT
    mu    = mean.reshape((1,2,1))   # The mean to be ssubtracted
    muT   = mean.reshape((1,1,2))   # The mean to be ssubtracted
    sigma = cov.reshape((1,2,2))  # A 2x2 vector that will expand in the N dimension

    pDist  = ((ysR - muT) @ np.linalg.inv(sigma) @ (ysC - mu)).flatten()
    pDist  = np.exp(-0.5 * pDist)
    pDist  = pDist / np.sqrt( (2*np.pi)**2 * np.linalg.det( cov ) )

    return pDist

def plotGaussianDensity(xx, yy, vals, ys, colors, outFile):

    plt.figure(figsize=(6, 3))
    axs = [
        plt.axes([0,0,0.5,1]   , facecolor='None' ),
        plt.axes([0.5,0,0.5,1] , facecolor='None' ),
        plt.axes([0,0,1,1]     , facecolor='None' ),
    ]

    for ax in axs:
        for s in ['right', 'top', 'left', 'bottom']:
            ax.spines[s].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    axs[0].contour( xx, yy, vals, levels=10, cmap='Blues', zorder=10 )
    axs[0].text(-2.5, 1.5, r'$p_{\mathbf y}( \mathbf y) = \mathcal N(\mathbf y| \mathbf 0, \mathbf \Sigma)$')
    axs[0].text(-2.5, 2, r'(a)')

    axs[1].scatter(ys[:,0], ys[:,1], marker='.', c = colors, alpha=0.5, edgecolors='none', zorder=20)
    axs[1].text(-2.5, 1.5, r'$\mathbf y \sim p_{\mathbf y}( \mathbf y)$')
    axs[1].text(-2.5, 2, r'(b)')

    for i in range(2):
        axs[i].set_xlim([-3,3])
        axs[i].set_ylim([-3,3])
        
        axs[i].arrow(0, -2.5, 0,  5, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.1, fc='k')
        axs[i].arrow(0,  2.5, 0, -5, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.1, fc='k')
        axs[i].text(2.7, 0, '$y_0$', ha='center', va='center')
        axs[i].text(0, 2.7, '$y_1$', ha='center', va='center')

        axs[i].arrow(-2.5, 0,  5, 0, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.1, fc='k')
        axs[i].arrow( 2.5, 0, -5, 0, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.1, fc='k')

        for j in np.linspace(-2, 2, 5):
            axs[i].plot( [j, j], [0.1, -0.1], 'k' )
            axs[i].plot( [0.1, -0.1], [j, j], 'k' )

            if j:
                axs[i].text(j, -0.2, f'{j}', ha='center', va='top', zorder=200)
                axs[i].text( 0.2, j, f'{j}', ha='left', va='center', zorder=200)
        
    axs[2].set_xlim([0,1])
    axs[2].set_xlim([0,1])

    plt.savefig(outFile)

    return

def main():
    print('banana distribution')

    N    = 1000
    mean = np.array([0, 0])
    cov  = np.array([
        [1, 0.95],
        [0.95, 1]
    ])
    
    #----------------------------------------------------------------
    # Generate N Samples from the Gaussian distribution
    #----------------------------------------------------------------
    ys  = np.random.multivariate_normal(mean, cov, N) # (N,2)
    
    pDist  = get2Ddensity(ys, mean, cov)
    maxPD  = pDist.max()
    colors = [plt.cm.viridis(p/maxPD) for p in pDist]

    #-------------------------------------------------------------------------
    # Generate a uniform grid of points and find the distributions for
    # each point
    #-------------------------------------------------------------------------
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    xx, yy = np.meshgrid(x, y, sparse=False)
    xxf    = xx.flatten()
    yyf    = yy.flatten()
    vals   = np.vstack((xxf, yyf)).T
    vals   = get2Ddensity(vals, mean, cov)
    vals   = vals.reshape(xx.shape)
    
    
    z0 = ys[:, 0]
    z1 = ys[:, 1]
    z1 = z1 - z0**2 -1
    z  = np.vstack((z0, z1)).T
    print(z.shape)

    plt.figure(figsize=(3, 3))
    axs = [
        plt.axes([0,0,1,1], facecolor='None' ),
        plt.axes([0,0,1,1], facecolor='None' ),
    ]
    axs[1].scatter(z[:,0], z[:,1], marker='.', c = 'blue', alpha=0.1, edgecolors='none', zorder=20)
    axs[1].set_xlim([-4,4])
    axs[1].set_ylim([-12, 2])

    axs[1].arrow(0,  -11, 0,  12.5, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')
    axs[1].arrow(0,  1.5, 0, -12.5, length_includes_head = True, zorder=100, head_length = 0.5, head_width=0.12, fc='k')
    axs[1].arrow(-3, 0,  6, 0, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.2, fc='k')
    axs[1].arrow( 3, 0, -6, 0, length_includes_head = True, zorder=100, head_length = 0.25, head_width=0.2, fc='k')

    for j in np.linspace(-10, -2, 5):
        axs[1].plot([-0.15, 0.15], [j,j], color='k')
        axs[1].text( 0.3, j, f'{j}', ha='left', va='center' )

    for j in np.linspace(-2, 2, 5):
        if j:
            axs[1].plot([j, j], [-0.2, 0.2], color='k')
            axs[1].text( j, -0.35, f'{j}', ha='center', va='top' )

    axs[1].text(3.2, 0, '$z_0$', ha='center', va='center')
    axs[1].text(0, 1.7, '$z_1$', ha='center', va='center')


    outFile = 'results/img/0001_banana.png'
    plt.savefig(outFile)

    # -------------------------------------
    # Plot the results
    # -------------------------------------
    outFile = 'results/img/0001_gaussian.png'
    plotGaussianDensity(xx, yy, vals, ys, colors, outFile)
    


    return

if __name__ == "__main__":
    main()
