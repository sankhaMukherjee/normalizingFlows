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
       z_1 &=  f_0(\mathbf y) \\
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

    q_{\mathbf z}(\mathbf z) = q_{\mathbf y}(\mathbf y) \left|  \det \nabla_{\mathbf y}f(\mathbf y)  \right|

