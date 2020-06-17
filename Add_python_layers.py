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



	def transformimage(self,img): ###img C H W
		if self.state=='train':
			C=img.shape[0]
			rs_height=img.shape[1]
			rs_width=img.shape[2]
			if self.new_height>0:
				rs_height=self.new_height
			if self.new_width>0:
				rs_width=self.new_width
			resized_img=zeros((C,rs_height,rs_width))
			for k in range(C):
				resized_img[k,:,:] = cv2.resize(img[k,:,:], (rs_height, rs_width))

			cr_height=resized_img.shape[1]
			cr_width=resized_img.shape[2]
			if self.crop_height>0:
			 	cr_height=self.crop_height
			if self.crop_width>0:
				cr_width=self.crop_width
			position=random.randint(0,4)
			border_h=int(math.ceil((rs_height-cr_height)/2));mod_h=int((rs_height-cr_height)%2)
			border_w=int(math.ceil((rs_width-cr_width)/2));mod_w=int((rs_width-cr_width)%2)
			tran_img=zeros((C,cr_height,cr_width))
			if position==0:
				tran_img=resized_img[:,border_h:rs_height-border_h+mod_h,border_w:rs_width-border_w+mod_w]
			if position==1:
				tran_img=resized_img[:,0:rs_height-2*border_h+mod_h,0:rs_width-2*border_w+mod_w]
			if position==2:
				tran_img=resized_img[:,0:rs_height-2*border_h+mod_h,2*border_w-mod_w:]
			if position==3:
				tran_img=resized_img[:,2*border_h-mod_h:,0:rs_width-2*border_w+mod_w]
			if position==4:
				tran_img=resized_img[:,2*border_h-mod_h:,2*border_w-mod_w:]

		if self.state=='test':
			C=img.shape[0]
			rs_height=img.shape[1]
			rs_width=img.shape[2]
			if self.new_height>0:
				rs_height=self.new_height
			if self.new_width>0:
				rs_width=self.new_width
			resized_img=zeros((C,rs_height,rs_width))
			for k in range(C):
				resized_img[k,:,:] = cv2.resize(img[k,:,:], (rs_height, rs_width))

			cr_height=resized_img.shape[1]
			cr_width=resized_img.shape[2]
			if self.crop_height>0:
				cr_height=self.crop_height
			if self.crop_width>0:
				cr_width=self.crop_width
			border_h=int(math.ceil((rs_height-cr_height)/2));mod_h=int((rs_height-cr_height)%2)
			border_w=int(math.ceil((rs_width-cr_width)/2));mod_w=int((rs_width-cr_width)%2)
			tran_img=zeros((C,cr_height,cr_width))
			tran_img=resized_img[:,border_h:rs_height-border_h+mod_h,border_w:rs_width-border_w+mod_w]

		tran_img=(tran_img-self.mean_value)*self.scale

		return tran_img



	def augmentimage(self,img): ###img C H W
		C=img.shape[0]
		H=img.shape[1]
		W=img.shape[2]
		aug_img=img

		if random.random()<self.probability:
			if self.mirror is True:
				for k in range(C):
					aug_img[k,:,:]=np.fliplr(np.squeeze(aug_img[:,:,k]))

		if random.random()<self.probability:
			if self.rotation is True:
				degree=random.randint(0,self.maxrotation)
				M=cv2.getRotationMatrix2D((H/2,W/2),degree,1)
				for k in range(C):
					aug_img[k,:,:]=cv2.warpAffine(aug_img[k,:,:],M,(H,W))

		if random.random()<self.probability:
			if self.colorshift is True:
				num=random.randint(0,self.maxcolorshift)	
				aug_img=aug_img-num

		return aug_img



	def img_shape(self):
		if self.color is True:
			img = cv2.imread(os.path.join(self.root_folder,self.image_total_listname[0].strip('\n').split(' ')[0]))
			img=img.transpose((2,0,1))
		else:
			img = cv2.imread(os.path.join(self.root_folder,self.image_total_listname[0].strip('\n').split(' ')[0]),cv2.IMREAD_GRAYSCALE)
			img=img[np.newaxis,:,:]

		if (self.crop_height>0) and (self.crop_width>0):
			return [img.shape[0],self.crop_height,self.crop_width]
		elif (self.new_height>0) and (self.new_width>0):
			return [img.shape[0],self.new_height,self.new_width]
		else:
			return [img.shape[0],img.shape[1],img.shape[2]]






	def do_setup(self):
		self.get_param()

		image_total_listname=[]
		total_num=[]
		point_total=[]
		
		self.image_total_listname = open(self.source,'r').readlines()
		if self.shuffle:
			random.shuffle(self.image_total_listname)
		self.total_num=len(self.image_total_listname)

		Points = open(self.sourcepoint,'r').readlines()
		temp=[x.strip('\n') for x in Points]
		self.point_total=dict()
		for i in range(len(temp)):
			if i%(self.sequence_length+1)==0:
				key=temp[i]
				Value=np.zeros((self.sequence_length,self.pointdim)) ###T D
				for j in range(self.sequence_length):
					AAA=temp[i+j+1].strip('\r\n').split(' ')
					value=np.array(temp[i+j+1].strip('\r\n').split(' '))
					Value[j,:]=value[1:]
					Value = np.array(Value,dtype=np.float32)
				self.point_total[key]=Value


	def setup(self,bottom,top):
		self.do_setup()
		self.idx=0
		self.img_shape = self.img_shape()

	def reshape(self,bottom,top):
		top[0].reshape(self.batch_size,self.img_shape[0],self.img_shape[1],self.img_shape[2])###image N C H W
		top[1].reshape(self.batch_size,1)###label N 1
		top[2].reshape(self.sequence_length,self.batch_size,self.pointdim)###point T N D
		top[3].reshape(self.sequence_length,self.batch_size)###index T N

	def forward(self,bottom,top):
		for i in range(self.batch_size):
			if self.color is True:
				img = cv2.imread(os.path.join(self.root_folder,self.image_total_listname[self.idx].strip('\n').split(' ')[0]))
				img=img.transpose((2,0,1))
			else:
				img = cv2.imread(os.path.join(self.root_folder,self.image_total_listname[self.idx].strip('\n').split(' ')[0]),cv2.IMREAD_GRAYSCALE)
				img=img[np.newaxis,:,:]
			img = np.array(img,dtype=np.float32)
			label=int(self.image_total_listname[self.idx].strip('\n').split(' ')[1]); label = np.array(label,dtype=np.uint8)

			S=self.image_total_listname[self.idx].strip('\n').split(' ')[0].split('-')
			Key=S[0]+'-'+S[1]+'-'+S[2]
			point = self.point_total[Key]
			#print(point)###T D
			###################
			indexisyes=[]
			newpoint=point
			for t in range(self.sequence_length):
				if np.sum(point[t,:])!=0:
					indexisyes.append(t)
			if len(indexisyes)>0:
				newpoint=np.zeros([self.sequence_length,self.pointdim])
				newpoint[self.sequence_length-len(indexisyes):self.sequence_length,:]=point[indexisyes,:]
			###################
			fixed = np.ones(self.sequence_length,dtype=np.uint8); fixed[0]=0
			if img is not None and point is not None:
				img=self.transformimage(img)
				img=self.augmentimage(img)
				top[0].data[i,:,:,:]=img
				top[1].data[i,0]=label
				top[2].data[:,i,:]=newpoint
				top[3].data[:,i]=fixed

			self.idx = self.idx + 1
			if self.idx == self.total_num:  
				self.idx = 0
				if self.shuffle:
					random.shuffle(self.image_total_listname)
			#print(top[2].data[:,i,:])



	def backward(self,top,propagate_down,bottom):
		pass
