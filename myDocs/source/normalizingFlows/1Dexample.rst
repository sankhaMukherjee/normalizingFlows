1D Example
----------

Now, we shall look at a very simple 1D example. The details are as follows

1. :math:`y \in \mathbb R^1`, and is uniformly distributed from 0-1. i.e. :math:`y \in [0,1]`
2. :math:`q_y(y) = 1` in the range :math:`[0,1]` and :math:`q_y(y) = 0` everywhere else.
3. We have a function mapping :math:`z = f(y) = 1 + 3y`

Let's calculate all the values mentioned above:

1. Calculation of the Jacobian. Since there is only a single value, we will only need to calculate
   the partial derivative with respect to a single variable

.. math::

       \nabla_{\mathbf y}f(\mathbf y) = [\frac {\partial (1+3y)} {\partial y}]  = [3]

2. Calculating the determinant of this matrix:

.. math::

       \det \nabla_{\mathbf y}f(\mathbf y) = 3

3. Calculating the absolute value of the determinant of this matrix:

.. math::

       \left |\det \nabla_{\mathbf y}f(\mathbf y) \right| = 3

4. Calculating the inverse of the absolute value of the determinant of this matrix:

.. math::

       \left |\det \nabla_{\mathbf y}f(\mathbf y) \right|^{-1} = \frac 1 3

This simple function is independent of :math:`y` indicating that the density of :math:`z` is also going
to be uniform. The definition of the density function can thus be represented as:

.. math::

    q_{\mathbf z}(\mathbf z) &= q_{\mathbf y}(\mathbf y) \left|  \det \nabla_{\mathbf y}f(\mathbf y)  \right|^{-1} \\
                             &= q_{\mathbf y}(\mathbf y) \frac 1 3   \\

5. Calculate the inverse function :math:`y = f^{-1}(z) = \frac z 3 - \frac 1 3`. Given this inverse transform, it should
   be possible to transform the densities as:


.. math::

    q_{z}(z)  &= q_{y}(y) \left|  \det \nabla_{y}f(y)  \right|^{-1} \\
              &= q_{y}(y) \frac 1 3   \\
              &= q_{y}( \frac z 3 - \frac 1 3 ) \frac 1 3


For :math:`z \in [1,4]`, the value of :math:`q_y(z)` is :math:`1`, and :math:`0` elsewhere. The transformation is
trivial to visualize, and is shown below. [`reference <https://cs.uwaterloo.ca/~ppoupart/teaching/cs480-spring19/slides/cs480-lecture23.pdf>`_]

.. image:: https://raw.githubusercontent.com/sankhaMukherjee/normalizingFlows/master/results/img/1d_normalizing_flow.png

