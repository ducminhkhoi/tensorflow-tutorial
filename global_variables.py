import tensorflow as tf
from keras import backend as K
import numpy as np


def eval(x):
    with tf.Session() as sess:
        return sess.run(x)
