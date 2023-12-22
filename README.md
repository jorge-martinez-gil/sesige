# Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution

[![arXiv](https://img.shields.io/badge/arXiv-2307.00925-b31b1b.svg)](https://arxiv.org/abs/2307.00925)

## 🌟  Introduction

Semantic similarity measures are essential in natural language processing, aiding a myriad of computer-related tasks. Our research introduces an innovative method for **automatically designing semantic similarity ensembles** using grammatical evolution, marking its first-time application in this domain.

##  📊 Features

- **Automatic Ensemble Design**: Utilizes grammatical evolution for ensemble creation.
- **Dynamic Measure Selection**: Aggregates various measures to form an optimized ensemble.
- **Benchmark Evaluations**: Tested against top-tier ensembles on standard datasets.
- **Accuracy Improvements**: Demonstrates notable enhancements in similarity assessments.

## 🛠️ Install

This research is heavily based in this work:

    Fenton, M., McDermott, J., Fagan, D., Forstenlechner, S., Hemberg, E., and O'Neill, M. 
    PonyGE2: Grammatical Evolution in Python. arXiv preprint, arXiv:1703.08535, 2017.

Therefore, for making it running it is necessary to install the PonyGE2 framework first:

1. Install [PonyGE2](https://github.com/PonyGE/PonyGE2).
2. Clone this repository.
3. Overwrite the PonyGE2 files with the files from this repository.

## 📈 Datasets
We evaluated our approach on MC30 and GeReSiD50 datasets. For more details, refer to our paper.

## ⚙️ Usage
After installing the Pony2GE framework:

```bash
cd ./PonyGE2/src
python ponyge.py --parameters <your_parameter_file>
```

## 📚 Citation
If you use our work, please cite:

```
@article{martinez2003c,
  author       = {Jorge Martinez-Gil},
  title        = {Automatic Design of Semantic Similarity Ensembles Using Grammatical
                  Evolution},
  journal      = {CoRR},
  volume       = {abs/2307.00925},
  year         = {2023},
  url          = {https://doi.org/10.48550/arXiv.2307.00925},
  doi          = {10.48550/arXiv.2307.00925},
  eprinttype   = {arXiv},
  eprint       = {2307.00925}
}

```
## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.