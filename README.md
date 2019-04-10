# ACII19-Apex-Time-Network
A Novel Apex-Time Network for Cross-Dataset Micro-Expression Recognition
  
  
  
# Platforms and dependencies
Ubuntu 16.04  Python 2.7  CUDA8.0 CuDNN6.0+  
Caffe：https://github.com/BVLC/caffe/
  
  
  
# Prepare
* Download the database (option)  
  CASMEII: http://fu.psych.ac.cn/CASME/casme2-en.php  
  SAMM: http://www2.docm.mmu.ac.uk/STAFF/m.yap/dataset.php  
  SMIC: https://www.oulu.fi/cmvs/node/41319  
  
* if you wann't to download the original database, the **Data** fold contain all the needed data for this repositories.  
  1. **Add_python_layers** contain a *.py* scrip that for image and point data load in Caffe.  
  2. **Apex_Cropped_images** contains all the Apex images of three Database (namely: CASMEII   SAMM   SMIC).  **Apex_Cropped_images.txt** contains image root and label in **Apex_Cropped_images** fold.  
  3. **OpticalFlowFeatureData.txt** is the temporal features described in our paper.  
    
  
  
# ATN
This fold is our proposed network for Cross-Dataset Micro-Expression Recognition.  
  
* **CDE** is the Composite Database Evaluation. For CASMEII_sub01, it means all samples (from the full consolidated database) are used for training except sub01 in CASMEII.  
  
* **HDE** is the Holdout-Database Evaluation. For TEST_CASMEII, it means the model is trained on two datasets(SAMM SMIC) and tested on CASMEII.  

* Notice: for each tries, you can use the *get_samples_Train_Test_TXT.py* to get the .txt list.
  
* How to run  
Take the CASMEII_sub01 fold for example, you just need to change your root in ../ACII19-Apex-Time-Network-master/, and then run: sh train_net.sh in the terminal.  
  
  
  
# MicroAttentionNet(Compared)
This fold is the compared method used in our paper.  
  
Micro-Attention outperformed the method described in the paper "From Macro to Micro Expression Recognition: Deep Learning on Small Datasets Using Transfer Learning", the latter one won the first place in the Facial Micro-Expression Grand Challenge (MEGC2018) at FG 2018.
  
  
  
# LBP-TOP(Compared)
This fold is the compared method used in our paper.  
  
Features.zip contained all the LBP-TOP features.   
  
  
# HOOF(Compared)
This fold is the compared method used in our paper.  
  
Features.zip contained all the HOOF features.  
The optical method for HOOF is refer to https://www.researchgate.net/publication/320373402_Dual_Temporal_Scale_Convolutional_Neural_Network_for_Micro-Expression_Recognition
  
  
  
# Citation
  
If it is helpful, please cite:  
  
A Novel Apex-Time Network for Cross-Dataset Micro-Expression Recognition. https://www.researchgate.net/publication/332259425_A_Novel_Apex-Time_Network_for_Cross-Dataset_Micro-Expression_Recognition?_sg=diGU1pnYWL7jyG27PigpTGSgGICMIcJsBVUvzS9L7JnOVYtp5Mc-zzDd45vy3xh0KZH5F67mIPFGFk3yKUlZvshslwHCR9PDB8ncvkNO.RwlNqjQR1J3Gf3mVvxE2nVKVCUIlyY78jnALqP2FlzD_qa_WWG1bUhRSNKPfBQ85rBKOigKyblpeKjQ7HItCLA
  
Micro-Attention for Micro-Expression recognition. Chongyang Wang, Min Peng, Tao Bi, Tong Chen. arXiv preprint arXiv:1811.02360, 2018.  
  
From Macro to Micro Expression Recognition: Deep Learning on Small Datasets Using Transfer Learning. Min Peng, Wu Zhan, Zhihao Zhang, Tong Chen. IEEE International Conference on Automatic Face & Gesture Recognition 2018.  
  
Dual temporal scale convolutional neural network for micro-expression recognition. Min Pen, Chongyang Wang, Tong Chen. Frontiers in psychology.







  
