import caffe
import os
import random
import math
from numpy import *
import numpy as np
import cv2



class ReadImageAndPointData_Layer(caffe.Layer):

	def get_param(self):
		param=eval(self.param_str)

		###param
		if 'root_folder' in param.keys():
			self.root_folder=param['root_folder']
		else:
			self.root_folder=''

		self.source=param['source']

		self.state=param['state']

		self.batch_size=param['batch_size']

		if 'color' in param.keys():
			self.color=param['color']
		else:
			self.color=False

		if 'shuffle' in param.keys():
			self.shuffle=param['shuffle']
		else:
			self.shuffle=False

		if 'new_height' in param.keys():
			self.new_height=param['new_height']
		else:
			self.new_height=0
		if 'new_width' in param.keys():
			self.new_width=param['new_width']
		else:
			self.new_width=0

		if 'crop_height' in param.keys():
			self.crop_height=param['crop_height']
		else:
			self.crop_height=0
		if 'crop_width' in param.keys():
			self.crop_width=param['crop_width']
		else:
			self.crop_width=0


		self.sourcepoint=param['sourcepoint']
		if 'sequence_length' in param.keys():
			self.sequence_length=param['sequence_length']
		else:
			self.sequence_length=0

		if 'pointdim' in param.keys():
			self.pointdim=param['pointdim']
		else:
			self.pointdim=0


		###transformimage
		if 'mean_value' in param.keys():
			self.mean_value=param['mean_value']
		else:
			self.mean_value=0

		if 'scale' in param.keys():
			self.scale=param['scale']
		else:
			self.scale=1


		###augmentimage
		if 'probability' in param.keys():
			self.probability=param['probability']
		else:
			self.probability=0

		if 'mirror' in param.keys():
			self.mirror=param['mirror']
		else:
			self.mirror=False

		if 'rotation' in param.keys():
			self.rotation=param['rotation']
			self.maxrotation=param['maxrotation']
		else:
			self.rotation=False
		if 'colorshift' in param.keys():
			self.colorshift=param['colorshift']
			self.maxcolorshift=param['maxcolorshift']
		else:
			self.colorshift=False
