import copy
import os

import cv2
import numpy as np
from PIL import Image as IMG

'''
A container to hold image related data
'''


class Image:

    def __init__(self):
        self.data_dir = None
        self.file_name = None
        self.image_arr = None
        self.working_arr = None
        self.mask = None
        self.ground_truth = None
        self.extra = {}

    def load_file(self, data_dir, file_name):
        try:
            self.data_dir = data_dir
            self.file_name = file_name
            self.image_arr = np.array(IMG.open(os.path.join(self.data_dir, self.file_name)))
        except Exception as e:
            print('### Error Loading file: ' + self.file_name + ': ' + str(e))

    def load_mask(self, mask_dir=None, fget_mask=None):
        try:
            mask_file = fget_mask(self.file_name)
            self.mask = np.array(IMG.open(os.path.join(mask_dir, mask_file)))
        except Exception as e:
            print('### Fail to load mask: ' + str(e))

    def apply_mask(self):
        if self.mask is not None:
            self.working_arr = cv2.bitwise_and(self.working_arr, self.working_arr, mask=self.mask)
        else:
            print('### Mask not applied. ', self.file_name)

    def load_ground_truth(self, gt_dir=None, fget_ground_truth=None):
        try:
            gt_file = fget_ground_truth(self.file_name)
            self.ground_truth = np.array(IMG.open(os.path.join(gt_dir, gt_file)))
        except Exception as e:
            print('Fail to load ground truth: ' + str(e))

    def apply_clahe(self, clip_limit=2.0, tile_shape=(8, 8)):
        enhancer = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_shape)
        if len(self.working_arr.shape) == 2:
            self.working_arr = enhancer.apply(self.working_arr)
        elif len(self.working_arr.shape) == 3:
            self.working_arr[:, :, 0] = enhancer.apply(self.working_arr[:, :, 0])
            self.working_arr[:, :, 1] = enhancer.apply(self.working_arr[:, :, 1])
            self.working_arr[:, :, 2] = enhancer.apply(self.working_arr[:, :, 2])
        else:
            print('### More than three channels')

    def __copy__(self):
        copy_obj = Image()
        copy_obj.data_dir = copy.copy(self.data_dir)
        copy_obj.file_name = copy.copy(self.file_name)
        copy_obj.image_arr = copy.copy(self.image_arr)
        copy_obj.working_arr = copy.copy(self.working_arr)
        copy_obj.mask = copy.copy(self.mask)
        copy_obj.ground_truth = copy.copy(self.ground_truth)
        copy_obj.extra = copy.deepcopy(self.extra)
        return copy_obj
