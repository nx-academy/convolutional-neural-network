import tensorflow as tf
import tensorflow_datasets as tfds


ds, ds_info = tfds.load('food101', shuffle_files=True, as_supervised=True, with_info=True)
