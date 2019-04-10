import os
import sys
import cv2
import random

dirs="Data/"
dirs_work="ATN/CDE/CASMEII_sub01/"

Test=[]
Train=[]
for line in open(dirs+'Apex_Cropped_images.txt'):
	Name=line.strip('\r\n').split(' ')[0]
	label=line.strip('\r\n').split(' ')[1]
	database=Name.split('-')[0]
	subject=Name.split('-')[1]
	sample=Name.split('-')[2]
	if database=='casme2' and subject=='sub01':
		Test.append(Name+' '+label+'\r\n')
	else:
		Train.append(Name+' '+label+'\r\n')

f=open(dirs_work+'Test_Apex.txt','a')
f.writelines(Test)
f.close()

### Train Balance
TempTrain_0=[];TempTrain_1=[];TempTrain_2=[]
for line in Train:
	if int(line.strip('\n').split(' ')[1])==0:
		TempTrain_0.append(line)
	if int(line.strip('\n').split(' ')[1])==1:
		TempTrain_1.append(line)
	if int(line.strip('\n').split(' ')[1])==2:
		TempTrain_2.append(line)
MAX=max(len(TempTrain_0),len(TempTrain_1),len(TempTrain_2))
if len(TempTrain_0)<MAX:
	A=[random.randint(0,len(TempTrain_0)-1) for i in range(MAX-len(TempTrain_0))]
	keylines0 = [TempTrain_0[i] for i in A]; del A
	TempTrain_0_eq = TempTrain_0+keylines0
else:
	TempTrain_0_eq=TempTrain_0
if len(TempTrain_1)<MAX:
	A=[random.randint(0,len(TempTrain_1)-1) for i in range(MAX-len(TempTrain_1))]
	keylines1 = [TempTrain_1[i] for i in A]; del A
	TempTrain_1_eq = TempTrain_1+keylines1
else:
	TempTrain_1_eq=TempTrain_1
if len(TempTrain_2)<MAX:
	A=[random.randint(0,len(TempTrain_2)-1) for i in range(MAX-len(TempTrain_2))]
	keylines2 = [TempTrain_2[i] for i in A]; del A
	TempTrain_2_eq = TempTrain_2+keylines2
else:
	TempTrain_2_eq=TempTrain_2
print len(TempTrain_0_eq)
print len(TempTrain_1_eq)
print len(TempTrain_2_eq)
TrainBalance=TempTrain_0_eq+TempTrain_1_eq+TempTrain_2_eq
f=open(dirs_work+'TrainBalance_Apex.txt','a')
f.writelines(TrainBalance)
f.close()











Test_optical=[]
flag=0
OpticalFlowFeatureData=open(dirs+'OpticalFlowFeatureData.txt','r').readlines()
for line in OpticalFlowFeatureData:
	flag=flag+1
	if flag%65==1:
		content=line.replace('\\','/')
		content=content.strip('\r\n').replace('Data/','')
		S=content.split('/')[0] +'-'+ content.split('/')[1] +'-'+ content.split('/')[2]
		for li in Test:
			Ss=li.split('-')[0] +'-'+ li.split('-')[1] +'-'+ li.split('-')[2]
			if S==Ss:
				Test_optical.append(S+'\r\n')
				weizhi=OpticalFlowFeatureData.index(line)
				for i in range(64):
					Test_optical.append(OpticalFlowFeatureData[i+weizhi+1])
				break
f=open(dirs_work+'Test_optical.txt','a')
f.writelines(Test_optical)
f.close()

Train_optical=[]
flag=0
OpticalFlowFeatureData=open(dirs+'OpticalFlowFeatureData.txt','r').readlines()
for line in OpticalFlowFeatureData:
	flag=flag+1
	if flag%65==1:
		content=line.replace('\\','/')
		content=content.strip('\r\n').replace('Data/','')
		S=content.split('/')[0] +'-'+ content.split('/')[1] +'-'+ content.split('/')[2]
		for li in Train:
			Ss=li.split('-')[0] +'-'+ li.split('-')[1] +'-'+ li.split('-')[2]
			if S==Ss:
				Train_optical.append(S+'\r\n')
				weizhi=OpticalFlowFeatureData.index(line)
				for i in range(64):
					Train_optical.append(OpticalFlowFeatureData[i+weizhi+1])
				break
f=open(dirs_work+'Train_optical.txt','a')
f.writelines(Train_optical)
f.close()
