import tensorflow as tf
import numpy as np 

from tensorflow.keras import Model, Sequential
import Planar

class Flow(Model):

    def __init__(self, dim=2, nFlows=10, lr=1e-3, name='PlanarFlow'):

        super(Flow, self).__init__(name=name)

        self.flows  = [Planar.Planar(dim, name=f'Planar_{i:03d}') for i in range(nFlows)]
        self.mu     = tf.Variable( tf.random.normal( [dim], 0, 0.001, tf.float32 ) )
        self.logVar = tf.Variable( tf.random.normal( [dim], 1, 0.001, tf.float32 ) )

        self.optimizer = tf.keras.optimizers.Adam(learning_rate = lr)
        
        return 

    def call(self, shape):

        std = tf.math.exp(0.5 * self.logVar)
        eps = tf.random.normal(shape, 0, 1, tf.float32)  # unit gaussian
        z0 = self.mu + eps * std

        temp = np.array(0).astype(np.float32)
        tupleVal = (z0, temp)

        zks = [z0.numpy()]
        for flow in self.flows:
            tupleVal = flow(tupleVal)
            zks.append( tupleVal[0].numpy() )
        zk, ldj = tupleVal

        return zks, ldj, self.mu, self.logVar

    def targetDensityTF(self, z):

        norm  = tf.norm(z, axis=1)
        norm1 = 0.5 * (( norm - 4 )/0.4)**2

        exp1 = tf.math.exp( -0.2 * ( (z[:,0] - 2)/0.8 )**2 )
        exp2 = tf.math.exp( -0.2 * ( (z[:,0] + 2)/0.8 )**2 )
        exp  = tf.math.log( exp1 + exp2 )

        return tf.math.exp(exp - norm1)

    def targetDensityTFLogit(self, z):

        norm  = tf.norm(z, axis=1)
        norm1 = 0.5 * (( norm - 4 )/0.4)**2

        exp1 = tf.math.exp( -0.2 * ( (z[:,0] - 2)/0.8 )**2 )
        exp2 = tf.math.exp( -0.2 * ( (z[:,0] + 2)/0.8 )**2 )
        exp  = tf.math.log( exp1 + exp2 )

        return (exp - norm1)

    def step(self, shape, beta=1):

        with tf.GradientTape() as tape:

            std = tf.math.exp(0.5 * self.logVar)
            eps = tf.random.normal(shape, 0, 1, tf.float32)  # unit gaussian
            z0 = self.mu + eps * std

            temp = np.array(0).astype(np.float32)
            tupleVal = (z0, temp)

            for flow in self.flows:
                tupleVal = flow(tupleVal)
            zk, ldj = tupleVal

            # Qz0
            logQz0 = -tf.math.reduce_sum(eps**2)
            # Qzk = Qz0 + sum(log det jac)
            logQzk = -tf.math.reduce_sum(ldj)
            # P(x|z)
            target = -tf.math.reduce_sum(self.targetDensityTFLogit(zk) + 1e-7)


            totalLoss = ( logQz0 + logQzk + beta * target) /shape[0]

            # Optimize
            grads = tape.gradient(totalLoss, self.trainable_weights)
            self.optimizer.apply_gradients(zip(grads, self.trainable_weights))

        return totalLoss.numpy(), logQz0.numpy(), logQzk.numpy(), nll.numpy()


