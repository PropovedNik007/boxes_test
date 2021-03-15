import cv2
import numpy as np
import time
from tracker_utils import distinct_colors
from process_classes.utils import display_box, calculate_centr_box

import torch
import random
import pandas as pd

class counter(object):
    between_frame_counter = 0
    current_rails_detected = 0
