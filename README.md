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
For the exsample of CASMEII_sub01 fold, you just need to change your root in ../ACII19-Apex-Time-Network-master/, and then run: sh train_net.sh in the terminal.



  
