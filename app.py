import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import tensorflow as tf
from keras import layers, models, datasets

import tensorflow_datasets as tfds

ds, ds_info = tfds.load('food101', shuffle_files=True, as_supervised=True, with_info=True)

train_ds, valid_ds = ds["train"], ds["validation"]

fig = tfds.show_examples(train_ds, ds_info)

def main():
    print("=====")
    print(fig)
    print("=====")


if __name__ == "__main__":
    main()
