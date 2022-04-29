# findRAM: Identify the modular organization of 3D genome from histone modifications
![ram github use](https://user-images.githubusercontent.com/32208663/163657693-0a571016-e56f-467d-a27e-b59d4bad6919.png)

## Computational Environment setup
### 0. Requirements
[Miniconda3](https://docs.conda.io/en/latest/miniconda.html) for python3.8  

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
Download the **findRAM** package from github and activate findRAM environment:   
```
git clone https://github.com/LinaZhengUCSD/findRAM.git
cd findRAM
conda env create -p YOUR_findRAM_PATH/findRAM.env/ -f YOUR_findRAM_PATH/findRAM.yml
```
Then you will see an environment folder named "findRAM.env" under your findRAM path. You have to activate this environment before you run findRAM package:   
```
conda activate YOUR_findRAM_PATH/findRAM.env/
```

### 2. findRAM package commands
**findRAM** takes the H3K27ac narrowpeaks file as input file format to calculate the RAM modules. The tools now provide genome version as hg19, hg38 and mm10.    
   
#### Commands and Options
```
bash RAMcall.sh -I <input(.narrowpeaks bed)> -O <output dir> -P <findRAM path> -C <conda installed path> -g <genome> [-s <spanvalue> -d <minPeak> -m <marginalerror>]

OPTIONS:
	-I input histone marks narrow peaks file (absolute path)
	-O output directory (absolute path)
	-P directory where findRAM package located (absolute path)
	-C directory where conda installed (absolute path, eg: /.local/share/miniconda3/)
	-g genome version, choose from hg19, hg38, mm10
	-s span value, choose from 0.025, 0.05, 0.1. Optional. Default=0.025.
	-d minimum height for a captured peak, choose from 0-1. Optional. Default=0.1.
	-m marginal error to add to each side of boundary, choose from 0,1,2,3. Optional.Default=0 
```

#### Get Help
```
bash RAMcall.sh --help
```

#### Example
```
bash RAMcall.sh -I YOUR_findRAM_PATH/EXAMPLE/testdata/E116-H3K27ac.narrowPeak -O YOUR_findRAM_PATH/EXAMPLE/testhuman/ -P YOUR_findRAM_PATH -C YOUR_conda_installed_PATH -g hg19
```
The outputs are located in:
```
YOUR_findRAM_PATH/EXAMPLE/testhuman/RAM.results/
```
