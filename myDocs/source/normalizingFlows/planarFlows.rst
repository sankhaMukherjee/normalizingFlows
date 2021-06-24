planarFlows
===========

The change of variables formula
-------------------------------

Assume that there are random variables :math:`\mathbf y \in \mathbb R^n`, and :math:`\mathbf z \in \mathbb R^n`, such that 
:math:`\mathbf y = [y_0, y_1, \ldots,y_{n-1}]^T`, where :math:`\mathbf y^T` represents the transpose of :math:`\mathbf y`. 
Similarly, assume that :math:`\mathbf z = [z_0, z_1, \ldots,z_{n-1}]^T`. 

Now, assume that there is a mapping function :math:`f: \mathbb R^d \Rightarrow \mathbb R^d` such 
that :math:`\mathbf z =f(\mathbf y)`. Such a mapping function can be represented as:

.. math::

       z_0 &=  f_0(\mathbf y) \\
       z_1 &=  f_1(\mathbf y) \\
       \vdots &=  \vdots \\
       z_{n-1} &=  f_{n-1}(\mathbf y)

Notice that any element of :math:`\mathbf z` is dependent upon all elements of the
vector :math:`\mathbf y` in the general case. Also, assume that the PDF of :math:`\mathbf y`
is given by the function :math:`q_y(\mathbf y)`, and the PDF of :math:`\mathbf z` is given by the
function :math:`q_z(\mathbf z)`. The most important question is that, if we know the distribution
:math:`q_y(\mathbf y)` well, will we be able to determine the distribution of  :math:`q_z(\mathbf z)`. 
We know  :math:`q_y(\mathbf y)`. Given this information, and the function :math:`f`, will be be able to
determine :math:`q_z(\mathbf z)` in terms of  :math:`q_y(\mathbf y)` and the function :math:`f`?

As it turns out, this is possible using the Jacobian determinant :math:`\nabla_{\mathbf y}`. The relationship
is given as:

.. math::

    q_{\mathbf z}(\mathbf z) = q_{\mathbf y}(\mathbf y) \left|  \det \nabla_{\mathbf y}f(\mathbf y)  \right|^{-1}

Let's make sure that we understand what this Jacobian determinant means with regard to the function :math:`f`.
Under these circumstances, the equation :math:`\nabla_{\mathbf y}f(\mathbf y)` can be represented as:

.. math::

       \nabla_{\mathbf y}f( \mathbf y  ) = 
       \begin{bmatrix}
       \frac {\partial f_0} {\partial y_0} & \frac {\partial f_0} {\partial y_1} & \ldots & \frac {\partial f_{0}} {\partial y_{n-1}} \\
       \frac {\partial f_1} {\partial y_0} & \frac {\partial f_1} {\partial y_1} & \ldots & \frac {\partial f_{1}} {\partial y_{n-1}} \\
       \vdots & \cdots & & \vdots \\
       \frac {\partial f_{n-1}} {\partial y_0} & \frac {\partial f_{n-1}} {\partial y_1} & \ldots & \frac {\partial f_{n-1}} {\partial y_{n-1}} \\
       \end{bmatrix}

Calculating the determinant of this is significantly difficult in general. We shall look at some simple examples in the subsequent sections.

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
trivial to visualize, and is shown below.

