{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# FashioNet ver.2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import h5py\n",
    "from PIL import Image\n",
    "import operator\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import time, pickle, pandas\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "import tensorflow.keras\n",
    "from PIL import Image\n",
	"import glob\n",
    "\n",
    "from keras.preprocessing.image import ImageDataGenerator\n",
    "from keras.models import Sequential, load_model\n",
    "from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D ,Conv2D\n",
    "from keras.layers import Activation, Dropout, Flatten, Dense\n",
    "from keras.callbacks import TensorBoard, ModelCheckpoint\n",
    "from keras.layers import Input\n",
    "from keras.applications import VGG16\n",
    "from keras import backend\n",
    "from keras import optimizers\n",
    "from tensorflow.keras import applications\n",
    "from keras.utils.conv_utils import convert_kernel\n",
    "\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "config = tf.ConfigProto()\n",
    "\n",
    "config.gpu_options.allow_growth = True\n",
    "\n",
    "sess = tf.Session(config=config)"
   ]	
