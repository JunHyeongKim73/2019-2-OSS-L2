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
 },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Declaring the no of classes for the category\n",
    "nb_classes = 5\n",
    "class_name = {\n",
    "    \n",
    "    0: 'Chiffon',\n",
    "    1: 'Cotton',\n",
    "    2: 'Crochet',\n",
    "    3: 'Denim',\n",
    "    4: 'Wool'\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def show_sample(X, y, prediction=-1):\n",
    "    im = X\n",
    "    plt.imshow(im)\n",
    "    if prediction >= 0:\n",
    "        plt.title(\"Class = %s, Predict = %s\" % (class_name[y], class_name[prediction]))\n",
