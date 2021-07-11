Flow Basics
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


Concateanted Flows 
------------------------

When multiple flows are concatenated one after another, we arrive at what is called multiple flows. Instead of
mapping from :math:`\mathbf y` to :math:`\mathbf z`, we shall make a series of mappings from :math:`\mathbf z`
to :math:`\mathbf z_1`, then to :math:`\mathbf z_2`, all the way to :math:`\mathbf z_K`, in the manner shown below.

.. math::

    \mathbf z_K = f_{K} \circ f_{K-2} \circ \cdots \circ f_1 (\mathbf z_0)

It is then trivial to see that the expression for the distribution function will be given by

.. math::

    q(\mathbf z_K) = q(\mathbf z)
                    \prod_{k=1}^{K} 
                    |
                        \det \mathbf \nabla_{\mathbf z_{k}} f_{\theta}(\mathbf z_k)
                    | ^{-1}

Generally though, this is written after taking a :math:`\log` on both sides, wherin the product becomes a sum. This
form is typically favoured for numerical stability. For the case of the flow, the KL divergence then becomes

.. math::

    D_{KL}( p(\mathbf z) || q(\mathbf z) )
    = D_{KL} \left( 
        p(\mathbf z) || 
        q(\mathbf z)
                    \prod_{k=1}^{K} 
                    |
                        \det \mathbf \nabla_{\mathbf z_{k}} f_{\theta}(\mathbf z_k)
                    | ^{-1}
    \right)
