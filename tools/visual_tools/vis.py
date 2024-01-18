import math
import os
import uuid
import time

from matplotlib import cm
import matplotlib.animation as animation
import matplotlib.pyplot as plt

import numpy as np
from IPython.display import HTML
import itertools
import tensorflow as tf

from google.protobuf import text_format
from waymo_open_dataset.metrics.ops import py_metrics_ops
from waymo_open_dataset.metrics.python import config_util_py as config_util
from waymo_open_dataset.protos import motion_metrics_pb2


# dataset = tf.data.TFRecordDataset(FILENAME, compression_type='')
# data = next(dataset.as_numpy_iterator())
# parsed = tf.io.parse_single_example(data, features_description)
print("hello")