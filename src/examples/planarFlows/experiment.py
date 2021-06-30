import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import Flow
import tensorflow as tf
tf.get_logger().setLevel('WARNING')

def main():


    shape = (10, 2)
    flow = Flow.Flow(dim=2, nFlows=10)
    print(flow(shape))

    return

if __name__ == "__main__":
    main()

