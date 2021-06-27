K-L Divergence
=================

The Kullback-Leibler (K-L) Divergence is a measure of the dissimilarity of two
probability density functions. In this case, we shall concern ourselves with
the continuous probability distributions. These span the same :math:`n`-dimensional
real space :math:`\mathbb R^n`. For the case of discrete distributions, please
consult relevant literature.

In this case, we shall assume that there are two probability distributions 
:math:`p(\mathbf y)` and :math:`q(\mathbf y)`, where :math:`\mathbf y \in \mathbb R^n`.
Let us also suppose that we wish to approximate :math:`p(\mathbf y)` with 
:math:`q(\mathbf y)`. Under these circumstances, the K-L divergence will provide
us with a measure of the information lost when we use :math:`q(\mathbf y)` instead
of :math:`p(\mathbf y)`. This is given by the formula:

.. math::

    D_{KL}\left( p(\mathbf y) || q( \mathbf y ) \right) = 
        \int_{-\infty}^{\infty} { 
            p(\mathbf y) \ln 
            \frac {p(\mathbf y)} {q(\mathbf y)} 
            d {\mathbf y}
        }

Special Case 1
----------------

Suppose you have two multivariate normal distributions :math:`\mathcal N_0(\mathbf \mu_0, \mathbf \Sigma_0)`
and :math:`\mathcal N_1(\mathbf \mu_1, \mathbf \Sigma_1)`, with non-singular covariance matrices. Under these
circumstances, the KL divergence between the two matrices are given as follows:

.. math::

    D_{KL}( \mathcal N_0 || \mathcal N_1 ) = \frac 1 2 \left( 
        \mathrm {tr} \left( \mathbf \Sigma_1^{-1} \mathbf \Sigma_0   \right) + 
        (\mu_1 - \mu_0)^T \mathbf \Sigma_1^{-1} (\mu_1 - \mu_0)       - k +
        \ln \left( 
            \frac {\det \mathbf \Sigma_1} {\det \mathbf \Sigma_0}
        \right)
    \right)

Special Case 2
----------------

This is a more specific case of Special Case 1. This is the KL divergence between a diagonal multivariate normal
distribution and a standard normal distribution of the same dimensions is given by

.. math::

    D_{KL}\left( 
        \mathcal N \left( 
            \left( \mu_0, \ldots, \mu_{n-1}  \right), 
            \mathrm{diag} \left( \sigma_1^2, \ldots, \sigma_{n-1}^2  \right)  
        \right) || 
        \mathcal N ( \mathbf 0, \mathbf I )
    \right) = \frac 1 2 \sum_{i=0}^{n-1} {\left( 
        \sigma_i^2 + \mu_i^2 - 1 - \ln( \sigma_i^2 )
    \right)}

This is often used with regard to variational inference, in many places including the variational autoencoder.