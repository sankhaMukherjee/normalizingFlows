Mathematical background
=======================

The change of variables formula
-----------------------------------

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
