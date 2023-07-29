# Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Introduction

Semantic similarity measures are widely used in natural language processing to catalyze various computer-related tasks. However, no single semantic similarity measure is the most appropriate for all tasks, and researchers often use ensemble strategies to ensure performance. This research work proposes a method for automatically designing semantic similarity ensembles. In fact, our proposed method uses grammatical evolution, for the first time, to automatically select and aggregate measures from a pool of candidates to create an ensemble that maximizes correlation to human judgment.

The method is evaluated on several benchmark datasets and compared to state-of-the-art ensembles, showing that it can significantly improve similarity assessment accuracy and outperform existing methods in some cases. As a result, our research demonstrates the potential of using grammatical evolution to automatically compare text and proves the benefits of using ensembles for semantic similarity tasks.

# Features

- Automatic design of semantic similarity ensembles using grammatical evolution.
- Selection and aggregation of measures from a pool of candidates to create an ensemble.
- Evaluation on benchmark datasets and comparison with state-of-the-art ensembles.
- Significant improvements in similarity assessment accuracy.

# Install
``` pip install -r requirements.txt```

# Datasets
The approach has been tested on the benchmark datasets MC30 and GeReSiD50. For more information, please refer to the paper.

# Use
This approach uses mostly the Pony2GE framework. It is necessary to install this framework and overwrite the files with the files from this repository.

# Citation
If you use this approach, please cite:

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
  
## License
MIT