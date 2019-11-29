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
