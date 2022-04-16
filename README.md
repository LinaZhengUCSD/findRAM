# findRAM: Identify the modular organization of 3D genome from histone modifications
![ram github use](https://user-images.githubusercontent.com/32208663/163657693-0a571016-e56f-467d-a27e-b59d4bad6919.png)

## Computational Environment setup
### 0. Requirements
[Miniconda3](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) for python3.8  

Install Miniconda3 or Anaconda according to their website instructions. 
   
Make sure you set up conda in your bashrc file before running findRAM package by commands below:  

To activate conda's base environment in your current shell session:   
```
eval "$(YOUR_miniconda3_PATH/bin/conda shell.YOUR_SHELL_NAME hook)"
```

To install conda's shell functions for easier access, first activate, then:   
```
conda init
```
Alternatively, if you do not set up "conda init", then you could source your conda installed before activating findRAM environment:   
```
source YOUR_miniconda3_PATH/etc/profile.d/conda.sh
```
   
### 1. Activate findRAM conda environment
Download the findRAM package from github and activate findRAM environment:   
```
git clone https://github.com/LinaZhengUCSD/findRAM.git
cd findRAM
conda activate ./RAM.env/
```

