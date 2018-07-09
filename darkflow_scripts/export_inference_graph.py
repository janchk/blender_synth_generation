r"""Saves out a GraphDef containing the architecture of the model."""

from __future__ import print_function

import argparse
import os
import sys
import time

import tensorflow as tf
from tensorflow.python.platform import gfile

# from model import ICNet_BN
# from tools import decode_labels, prepare_label, inv_preprocess
# from image_reader import ImageReader
# from inference import preprocess, check_input

# from hyperparams import *

tf.app.flags.DEFINE_boolean(
    'is_training', False,
    'Whether to save out a training-focused version of the model.')

# tf.app.flags.DEFINE_integer(
#    'image_size', None,
#    'The image size to use, otherwise use the model default_image_size.')

tf.app.flags.DEFINE_integer(
    'batch_size', None,
    'Batch size for the exported model. Defaulted to "None" so batch size can '
    'be specified at model runtime.')

tf.app.flags.DEFINE_string(
    'output_file', '', 'Where to save the resulting file to.')

output_file = '/media/jan/ubuntuHD/YOLO/built_graph/frozen_graph.pb'


def main(_):
    # if not FLAGS.output_file:
    #     raise ValueError('You must supply the path to save to with --output_file')

    tf.logging.set_verbosity(tf.logging.INFO)

    with tf.Graph().as_default() as graph:
        graph = tf.Graph()
        with graph.as_default():
            graph_def = tf.GraphDef()
            frozen_path = '/home/jan/PycharmProjects/darkflow/built_graph/yolo_auto.pb'
            with tf.gfile.GFile(frozen_path, 'rb') as fid:
                serialized_graph = fid.read()
                graph_def.ParseFromString(serialized_graph)

                tf.import_graph_def(graph_def, name='')
                label_names = ['bulldozer', 'excavator', 'backhoe', 'tractor', 'truck', 'grader',
                               'loader', 'car', 'person']
                tf.constant(label_names, name="label_names")
                shape = [416, 416]

                shape = (int(shape[0]), int(shape[1]), 3)
                tf.constant(shape, name='input_size')
                tf.constant(['input:0'], name="input_name")
                tf.constant(['output:0'], name="output_name")

            graph_def = graph.as_graph_def()
            with gfile.GFile(output_file, 'wb') as f:
                f.write(graph_def.SerializeToString())
                print('Successfull written to', output_file)


if __name__ == '__main__':
    tf.app.run()
