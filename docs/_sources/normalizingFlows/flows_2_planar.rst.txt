Planar Flow
===============

An example function for such a flow is given by what is called a planar flow. 

Discussion on `Planar Flow Intuition`_ provides valuable intuition to planar flows. The mathematical
details are present in the paper `Variational Inference with Normalizing Flows`_, wherein the authors
discuss a aprticular 

Planar flows rely on invertible planar transformations. See Section 4.1. of `Variational Inference with Normalizing Flows`_.
This comprises of the transformations

.. math::

    f(\mathbf z) = \mathbf z + \mathbf u h( \mathbf w^T\mathbf z + b )

here, :math:`\mathbf w \in \mathbb R^n`, :math:`\mathbf u \in \mathbb R^n`, and :math:`b \in \mathbb R`.
:math:`h(\cdot)` is a nonlinearity such as :math:`\mathrm {tanh}(\cdot)`. 

The important thing about this specific transformation is that the matrix determinant is invertible under certain
circumstances, and it is possible to find a closed-form solution to this. Given that :math:`h'()` is the derivative
of the function :math:`h()`, the derivative can be calculated as:

.. math::

    \nabla_{\mathbf z} f( \mathbf z ) = 
            \mathbf I + \mathbf u h'( \mathbf w ^T \mathbf z + b) \mathbf w

Fnally, the determinant can be calculated using the amtrix determinant lemma 
:math:`\det (\mathbf I + \mathbf u \mathbf v^T) = (1 + \mathbf u^T \mathbf v)`:

.. math::

    \left| \det \nabla_{\mathbf z} f( \mathbf z )  \right| &=
        | \det 
                \left(
                    \mathbf I + \mathbf u h'( \mathbf w^T \mathbf z + b ) \mathbf w^T
                \right) 
        | \\ &=
        | 
            \left(
                1 +  \mathbf u ^T h'( \mathbf w^T \mathbf z + b ) \mathbf w
            \right) 
        |

Depending upon the nonlinearity chosen, it is possible that the function to not be invertible. However, this
condition can be satsified if :math:`\mathbf w^T \mathbf u \ge -1`. Rather than using this equation then, 
a slight modification of the equation is used wherein, instead of using the vector :math:`\mathbf u`, a 
slightly modified version of :math:`\mathbf u` given by :math:`\hat {\mathbf u}(\mathbf u, \mathbf w)` is
used, given by the equations
:math:`\hat {\mathbf u}(\mathbf u, \mathbf w) = \mathbf u + \left[ m(\mathbf w^T \mathbf u) - \mathbf w^T \mathbf u \right]`,
where :math:`m(x) = -1 + \log( 1 + e^x )`. See Appendix A for all the mathematical details.

Just like what has been shown above, one can apply one function after another as shown below:

.. math::

    \mathbf z_K = f_{K} \circ f_{K-2} \circ \cdots \circ f_1 (\mathbf z)


The log-likelihood of such a distribution is then simply given by the equation

.. math::

    \log q_K(\mathbf z_K) = \log q_0( \mathbf z ) 
        - \sum_{k=1}^{K} {
            \log \left|
                1 +  \hat {\mathbf u}_k ^T h'( \mathbf w_k^T \mathbf z_{k-1} + b ) \mathbf w_k
            \right|
        }


.. _Planar Flow Intuition: https://stats.stackexchange.com/questions/465184/planar-flow-in-normalizing-flows
.. _Variational Inference with Normalizing Flows: https://arxiv.org/pdf/1505.05770.pdf

