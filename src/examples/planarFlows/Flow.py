import tensorflow as tf
import numpy as np 

from tensorflow.keras import Model, Sequential
import Planar

class Flow(Model):

    def __init__(self, dim=2, nFlows=10, name='PlanarFlow'):

        super(Flow, self).__init__(name=name)

        self.flows  = [Planar.Planar(dim, name=f'Planar_{i:03d}') for i in range(nFlows)]
        self.mu     = tf.Variable( tf.random.normal( [dim], 0, 0.001, tf.float32 ) )
        self.logVar = tf.Variable( tf.random.normal( [dim], 1, 0.001, tf.float32 ) )
        
        return 

    def call(self, shape):

        std = tf.math.exp(0.5 * self.logVar)
        eps = tf.random.normal(shape, 0, 1, tf.float32)  # unit gaussian
        z0 = self.mu + eps * std

        temp = np.array(0).astype(np.float32)
        tupleVal = (z0, temp)

        for flow in self.flows:
            tupleVal = flow(tupleVal)
        zk, ldj = tupleVal
        
        return z0, zk, ldj, self.mu, self.logVar
