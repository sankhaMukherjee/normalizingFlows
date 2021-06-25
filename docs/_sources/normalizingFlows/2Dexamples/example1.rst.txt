Gaussian to banana distributions
================================

We shall look at the following distribution:

1. :math:`\mathbf y \in \mathbb R^2` and is defined (has support) over the entire 2D plane
2. :math:`\mathbf y \sim p_{\mathbf y}(\mathbf y) = \mathcal N( \mathbf y | \mathbf 0, \mathbf \Sigma )`
3. We have a transformation function :math:`\mathbf z = f(\mathbf y)` such that 

.. math::

       \mathbf z = f(\mathbf y) = 
       \begin{bmatrix}
       y_0 \\
       y_1 - y_0^2 -1
       \end{bmatrix}

Let us follow the computations as we had done earlier:

1. Calculation of the Jacobian. 

.. math::

       \nabla_{\mathbf y}f(\mathbf y) = 
       \begin{bmatrix}
       \frac {\partial y_0}              {\partial y_0}    & \frac {\partial y_0}              {\partial y_1} \\
       \frac {\partial (y_1 - y_0^2 -1)} {\partial y_0}    & \frac {\partial (y_1 - y_0^2 -1} {\partial y_1}
       \end{bmatrix} 
       =
       \begin{bmatrix}
       1        & 0 \\
       -2 y_0    & 1
       \end{bmatrix}  

1. Calculating the determinant of this matrix. Thankfully, this is an lower-triangular matrix and its
   determinant is just the product of its diagonals. (Remember this informaiton. This will become very
   important later when we discuss normalizing flows).

.. math::

       \det \nabla_{\mathbf y}f(\mathbf y) = \det 
       \begin{bmatrix}
       1        & 0 \\
       -2 y_0    & 1
       \end{bmatrix}  
       = 1

1. Calculating the absolute value of the determinant of this matrix:

.. math::

       \left |\det \nabla_{\mathbf y}f(\mathbf y) \right| = 1

4. Calculating the inverse of the absolute value of the determinant of this matrix:

.. math::

       \left |\det \nabla_{\mathbf y}f(\mathbf y) \right|^{-1} = 1

This simple function is independent of :math:`y` indicating that the density of :math:`z` is also going
to be uniform. The definition of the density function can thus be represented as:

.. math::

    q_{\mathbf z}(\mathbf z) &= q_{\mathbf y}(\mathbf y) \left|  \det \nabla_{\mathbf y}f(\mathbf y)  \right|^{-1} \\
                             &= q_{\mathbf y}(\mathbf y) \times 1   \\

5. Calculate the inverse function :math:`\mathbf y = f^{-1}(\mathbf z)`. This is given by the transformation:

.. math::
       \mathbf y = f^{-1}(\mathbf z) = 
       \begin{bmatrix}
       z_0 \\
       z_0^2 + z_1 + 1
       \end{bmatrix}

Given this inverse transform, it should be possible to transform densities as:


.. math::

    q_{z}(z)  &= q_{y}(y) \left|  \det \nabla_{y}f(y)  \right|^{-1} \\
              &= q_{y}(y) \times 1   \\
              &= q_{y}\left( 
              \begin{bmatrix}
              z_0 \\
              z_0^2 + z_1 + 1
              \end{bmatrix}
              \right) 


Results 
++++++++++

We shall now specifically calcualte the distributions for :math:`\mathbf z` in two different ways.
Specifically, first, we are going to sample from the distribution for :math:`\mathbf y` and then transform
these points into :math:`\mathbf z`. 

The distribution for :math:`\mathbf y` is given by 

.. math::

       \mathbf y = \mathcal N \left( \mathbf y | \mathbf 0, \mathbf \Sigma = 
       \begin{bmatrix}
              1    & 0.95 \\
              0.95 & 1
       \end{bmatrix}
       \right)