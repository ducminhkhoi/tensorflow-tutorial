import tensorflow as tf
tf.reset_default_graph()
from keras import backend as K
import numpy as np

def eval(x):
    with tf.Session() as sess:
        return sess.run(x)
