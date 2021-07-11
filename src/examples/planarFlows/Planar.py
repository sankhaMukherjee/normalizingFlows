import tensorflow as tf

from tensorflow.keras import layers

class Planar(layers.Layer):

    def __init__(self, size=1, initSigma=0.01, name='Planar'):

        super(Planar, self).__init__(name=name)

        self.u = tf.Variable( tf.random.normal( [1, size], 0, initSigma, tf.float32 ) )
        self.w = tf.Variable( tf.random.normal( [1, size], 0, initSigma, tf.float32 ) )
        self.b = tf.Variable( 0.0, tf.float32 )

        return

    def psi(self, z):
        '''calculation of psi

        ψ(z)=h′( wT z + b )w

        In this case, h(m) = tanh(m)
        so, h'(m) = 1 - tanh2(m)

        Parameters
        ----------
        z : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        '''

        result = z @ tf.transpose(self.w) + self.b
        result = 1 - tf.math.tanh( result )**2
        result = result @ self.w
        
        return result

    def call(self, z):

        z, sumLogAbsDetJac = z

        # Calculate f(z)
        wu    = self.w @ tf.transpose(self.u)
        unitW = self.w / tf.norm(self.w) **2
        unitU = self.u + (tf.math.softplus(wu) - 1 - wu) * unitW
        wzb   = z @ tf.transpose(self.w) + self.b
        fz    = z + (unitU * tf.math.tanh(wzb))

        # Calculate the log of the jacobian
        detJac          = 1 + self.psi(z) @ tf.transpose(unitU)
        logAbsDetJac    = tf.math.log( tf.math.abs( detJac ) + 1e-6)
        sumLogAbsDetJac = sumLogAbsDetJac + logAbsDetJac


        return fz, sumLogAbsDetJac

