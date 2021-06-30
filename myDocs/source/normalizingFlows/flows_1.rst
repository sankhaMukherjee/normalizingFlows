Single flow
===============

In this first example, consider that you want to transform a latent variable :math:`\mathbf y` 
which has a PDF :math:`q_{\mathbf y}(\mathbf y)` to another latent variable :math:`\mathbf z` 
that has a probability PDF :math:`q_{\mathbf z}(\mathbf z)` closer to the density that we 
desire, which happens to be :math:`p_{\mathbf y}(\mathbf y)`. 
For this, we should be able to create a function mapping :math:`f_{\mathbf\theta}` 
parametrized by :math:`\mathbf \theta` such that

1. :math:`\mathbf z = f_{\mathbf \theta}(\mathbf y)`
2. :math:`\mathbf y = f_{\mathbf \theta}^{-1}(\mathbf z)`

We know that the KL divergence between our desired distribution and the new distribution is
:math:`D_{KL}( p_{\mathbf y}(\mathbf y) || q_{\mathbf z}(\mathbf z) )`

Note that we can, due to the change of variable formula, represent :math:`q_{\mathbf z}(\mathbf z)` in 
terms of :math:`q_{\mathbf y}(\mathbf y)` as:

.. math::

    q_{\mathbf z}(\mathbf z) = q_{\mathbf y}(\mathbf y)
                \left|
                    \det \mathbf \nabla_{\mathbf y} f_{\theta}(\mathbf y)
                \right|^{-1}

This means that we should be able to find a set of parameters :math:`\theta` such that, minimizing the
parameters will allow us to find the best-case functional mapping for this new latent space. If we 
substitute this form in the KL divergence, we get the formula

.. math::

    D_{KL}( p_{\mathbf y}(\mathbf y) || q_{\mathbf z}(\mathbf z) )
    = D_{KL} \left( 
        p_{\mathbf y}(\mathbf y) || 
        q_{\mathbf y}(\mathbf y)
                    \left|
                        \det \mathbf \nabla_{\mathbf y} f_{\theta}(\mathbf y)
                    \right|^{-1}
    \right)


Single Planar Flow 
------------------------

An example function for such a flow is given by what is called a planar flow. 

Discussion on `Planar Flow Intuition`_ provides valuable intuition to planar flows. 


.. _Planar Flow Intuition: https://stats.stackexchange.com/questions/465184/planar-flow-in-normalizing-flows

