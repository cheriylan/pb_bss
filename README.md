# Blind Source Separation (BSS) algorithms

[![Build Status](https://dev.azure.com/fgnt/fgnt/_apis/build/status/fgnt.pb_bss?branchName=master)](https://dev.azure.com/fgnt/fgnt/_build/latest?definitionId=1&branchName=master)
[![Azure DevOps tests](https://img.shields.io/azure-devops/tests/fgnt/fgnt/1)](https://dev.azure.com/fgnt/fgnt/_build/latest?definitionId=1&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/fgnt/fgnt/1)](https://dev.azure.com/fgnt/fgnt/_build/latest?definitionId=1&branchName=master)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/fgnt/pb_bss/master/LICENSE)

__Fork note__ : The original repo has been modified to allow a partial 
release of the evaluation utilities on PyPI under the name 
`pb_bss_eval`. All the credits goes to the original authors 
(see [here](https://github.com/fgnt/pb_bss)).  
As can be seen in the [Manifest.in](./MANIFEST.in), only the 
evaluation sub-package can be installed and is released on PyPI.
To install it, just run :
```
pip install numpy Cython  # required for pesq install
pip install pb_bss_eval
```

This repository covers EM algorithms to separate speech sources in 
multi-channel recordings.  

In particular, the repository contains methods to integrate 
Deep Clustering (a neural network-based source separation algorithm) 
with a probabilistic spatial mixture model as proposed in the Interspeech paper "Tight integration of spatial and spectral features for BSS with Deep Clustering embeddings" presented at Interspeech 2017 in Stockholm.

```BibTex
@InProceedings{Drude2017DeepClusteringIntegration,
  Title                    = {Tight integration of spatial and spectral features for {BSS} with Deep Clustering embeddings},
  Author                   = {Drude, Lukas and and Haeb-Umbach, Reinhold},
  Booktitle                = {INTERSPEECH 2017, Stockholm, Sweden},
  Year                     = {2017},
  Month                    = {Aug}
}
```

# Installation
Install it directly from source
```bash
git clone https://github.com/fgnt/pb_bss.git
cd pb_bss
pip install --editable .
```
We expect that `numpy`, `scipy` and `cython` are installed (e.g. `conda install numpy scipy cython` or `pip install numpy scipy cython`).

The default option is to install only the necessary dependencies.
When you want to run the tests or execute the notebooks, use the one of the following commands for the installation:
```bash
pip install --editable .[all]  # Without a whitespace between `.` and `[all]`
pip install git+https://github.com/fgnt/pb_bss.git#egg=pb_bss[all]
```
