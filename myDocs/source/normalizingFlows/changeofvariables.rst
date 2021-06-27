Mapping distributions between two random variables
=====================================================

Let us suppose that we have two variables :math:`\mathbf y` and :math:`\mathbf z`. Both of these random variables
span the :math:`\mathbb R^n` space. Furthermore, there is an invertible mapping :math:`f` such that
:math:`\mathbf z = f(\mathbf y)` and :math:`\mathbf y = f^{-1}(\mathbf z)`. Each of these random variables have 
a probability density function (PDF) :math:`p_{\mathbf y}(\mathbf y)` and :math:`p_{\mathbf z}(\mathbf z)` over the 
:math:`\mathbb R^n` space.

If we know :math:`p_{\mathbf y}(\mathbf y)` very well, and the function :math:`f` and :math:`f^{-1}`, can we then
figure out :math:`p_{\mathbf z}(\mathbf z)` easily? The following subsections will explore this idea.

The change of variables formula
-----------------------------------

Assume that there are random variables :math:`\mathbf y \in \mathbb R^n`, and :math:`\mathbf z \in \mathbb R^n`, such that 
:math:`\mathbf y = [y_0, y_1, \ldots,y_{n-1}]^T`, where :math:`\mathbf y^T` represents the transpose of :math:`\mathbf y`. 
Similarly, assume that :math:`\mathbf z = [z_0, z_1, \ldots,z_{n-1}]^T`. 

Now, assume that there is a mapping function :math:`f: \mathbb R^n \Rightarrow \mathbb R^n` such 
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

Special Case 1
----------------

Suppose that the function :math:`f` is of a special form shown below

.. math::

       z_0     &=  f_0(y_0)               \\
       z_1     &=  f_1(y_0, y_1)          \\
       z_2     &=  f_1(y_0, y_1, y_2)     \\
       \vdots  &=  \vdots                 \\
       z_{n-1} &=  f_{n-1}(y_0, y_1, \cdots, y_{n-1})

where the :math:`i`:sup:`th` element of :math:`\mathbf z` only depends in :math:`y_{j \le i}`. Under such circumstances, the
Jacobian resembles the following

.. math::

       \nabla_{\mathbf y}f( \mathbf y  ) = 
       \begin{bmatrix}
              \frac {\partial f_0} {\partial y_0} &
              0                                   &
              0                                   &
              0                                   &
              \cdots                              &
              0
       \\
              \frac {\partial f_1} {\partial y_0} & 
              \frac {\partial f_1} {\partial y_1} &
              0                                   &
              0                                   &
              \cdots                              &
              0
       \\
              \frac {\partial f_1} {\partial y_0} & 
              \frac {\partial f_1} {\partial y_1} &
              \frac {\partial f_2} {\partial y_2} &
              0                                   &
              \cdots                              &
              0                                   
       \\
              \vdots                              & 
              \cdots                              &
              \cdots                              &
              \cdots                              &
              \cdots                              &
              0
       \\
              \frac {\partial f_1} {\partial y_0} & 
              \frac {\partial f_1} {\partial y_1} & 
              \cdots                              &  
              \cdots                              &  
              \cdots                              &  
              \frac {\partial f_{n-1}} {\partial y_{n-1}}  
       \\
       \end{bmatrix}


Since this is a lower-triangualr matrix, the determinant is simply the product of the diagonal elements.
Hence, the determinant can be written in this form

.. math::

       \det \nabla_{\mathbf y} f(\mathbf y) = 
       \prod_{i=0}^{n-1} {
              \frac {\partial f_i} {\partial y_i}
       }

The compute requirements for this scales as :math:`\mathcal O(n)` rather than  :math:`\mathcal O(n^3)`, and
is something that makes normalizing flows practicable.
