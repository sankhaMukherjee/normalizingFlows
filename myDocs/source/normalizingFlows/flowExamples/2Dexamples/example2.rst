2D Planar Flow Example
========================

In this section, we shall see how we can start with one funciton :math:`f(\mathbf z)`, and through a
series of transformations defined by

.. math::

    \mathbf z_K = f_{K} \circ f_{K-2} \circ \cdots \circ f_1 (\mathbf z_0)

obtain a :math:`\mathbf z_K` such that the probability density of these points :math:`p(\mathbf z_K)` approaches
the probability of the target density :math:`q(\mathbf z_K)`. The target distribution that we are trying to approximate
is given by the following formula.

.. math::

    q_1(\mathbf z_K) &= \log \left[
        \exp \left(
            -0.2 * \frac {\left( z_0 - 2 \right)^2} {0.8^2}
        \right) + 
        \exp \left(
            -0.2 * \frac {\left( z_0 + 2 \right)^2} {0.8^2}
        \right)
    \right] \\
    q_2(\mathbf z_K) &= \frac 1 2
        \left[
            \frac {\|z\| - 4} {0.4}
        \right] ^ 2 \\
    q(\mathbf z_K) &= \exp \left( q_2(\mathbf z_K) - q_1(\mathbf z_K) \right)


And is plotted in the figure below.

.. figure:: https://raw.githubusercontent.com/sankhaMukherjee/normalizingFlows/master/results/img/target.png
    :align: center
    :name: target

    A contour plot of the target distribution :math:`q(\mathbf z)` that we are trying to approximate 
    has been plotted.

In this case, the target density will be a fairly complex density. This is shown in :numref:`target`. we shall
start with an initial distribution :math:`p(\mathbf z) = \mathcal N( \mathbf I, \mathbf 0 )`, which happens to
be a unit normal distribution. The reason for using this distribiution is that the distribution characteristics
are pretty easy to calculate.

Now, as mentioned in the Section :ref:`Planar Flow` that the distribution of the flow after the transformation is givn by 

.. math::

    \log p(\mathbf z_K) = \log p( \mathbf z ) 
        - \sum_{k=1}^{K} {
            \log |
                1 +  \hat {\mathbf u}_k ^T h'( \mathbf w_k^T \mathbf z_{k-1} + b ) \mathbf w_k
            |
        }

The TensorFlow 2 implementation of a planar layer is described in 
`Planar.py <https://github.com/sankhaMukherjee/normalizingFlows/blob/master/src/examples/planarFlows/Planar.py>`_, while
that of the planar flow model is described in 
`Flow.py <https://github.com/sankhaMukherjee/normalizingFlows/blob/master/src/examples/planarFlows/Flow.py>`_. The entire
example is present in the 
`folder <https://github.com/sankhaMukherjee/normalizingFlows/tree/master/src/examples/planarFlows>`_. To approximate the
function :math:`q( \mathbf z )` with the approximate density :math:`p(\mathbf z_K)`, we shall just reduce the variational
free energy between the two quantities, and minimize the loss function

.. math::

    \mathcal L = \mathbb E \left[ \log q(\mathbf z_K) - \log p( \mathbf z_K ) \right]



