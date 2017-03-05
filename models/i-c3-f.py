#!/usr/bin/env python

"""MLP model."""

import tensorflow as tf
import tflearn
from tflearn.layers.core import fully_connected


def inference(images, dataset_meta):
    """
    Build a tiny CNN model.

    Parameters
    ----------
    images : tensor
        Images returned from distorted_inputs() or inputs().
    dataset_meta : dict
        Has key 'n_classes'

    Returns
    -------
    logits
    """
    net = tf.reshape(images, [-1,
                              dataset_meta['image_width'],
                              dataset_meta['image_height'],
                              dataset_meta['image_depth']])
    net = tflearn.layers.conv.conv_2d(net,
                                      nb_filter=16,
                                      filter_size=3,
                                      activation='relu',
                                      strides=1,
                                      weight_decay=0.0)
    y_conv = fully_connected(net, dataset_meta['n_classes'],
                             activation='softmax',
                             weights_init='truncated_normal',
                             bias_init='zeros',
                             regularizer=None,
                             weight_decay=0)
    return y_conv
