# Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution

[![arXiv](https://img.shields.io/badge/arXiv-2307.00925-b31b1b.svg)](https://arxiv.org/abs/2307.00925)

## 🌟 Overview

This repository accompanies the paper [**"Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution"**](https://arxiv.org/abs/2307.00925), which introduces a **Grammatical Evolution (GE)-based framework** for the **automatic design and optimization of semantic similarity ensembles**. Our method uses evolutionary computation to create optimized, interpretable ensembles that outperform state-of-the-art techniques on genetic ensembles when solving benchmark datasets.

---

## ✨ Key Contributions

- **First Application of Grammatical Evolution in Semantic Similarity**: Introducing a novel approach to ensemble design.
- **Dynamic Similarity Aggregation**: Automatically selects and combines multiple similarity measures for optimal performance.
- **Interpretability and Accuracy**: Ensuring high correlation with human judgments while maintaining transparency.
- **Benchmark Validation**: Rigorous evaluation against established datasets (MC30, GeReSiD50, WS353).

---

## 📊 Features

- **Automated Ensemble Learning**: Uses **Backus-Naur Form (BNF) grammar** to guide the evolutionary process.
- **Optimized for Semantic Similarity**: Evaluates ensembles based on **Pearson** and **Spearman** correlation coefficients.
- **Seamless Integration with PonyGE2**: Built on the **PonyGE2** framework for genetic programming.
- **Extensive Benchmarking**: Compared with state-of-the-art methods across multiple datasets.

---

## 🛠️ Installation

To set up the environment and run experiments:

1. Clone the [PonyGE2 repository](https://github.com/PonyGE/PonyGE2):
   ```bash
   git clone https://github.com/PonyGE/PonyGE2.git
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/jorge-martinez-gil/sesige.git
   ```
3. Overwrite **PonyGE2** files with those provided in this repository:
   ```bash
   cp -r ./sesige/* ./PonyGE2/
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📈 Datasets

We evaluate our method using the following benchmark datasets:

- **MC30**: 30 word pairs with human-annotated similarity scores.
- **GeReSiD50**: 50 phrase pairs from geospatial research, assessing domain-specific generalization.
- **WS353**: 353 words widely used for evaluating semantic similarity in NLP.

---

## ⚙️ Usage

To run the **Grammatical Evolution** process:

1. Navigate to the `src` directory of **PonyGE2**:
   ```bash
   cd ./PonyGE2/src
   ```
2. Execute the training script with the provided parameter file:
   ```bash
   python ponyge.py --parameters ./parameters/semantic_similarity.txt
   ```
3. Results are stored in the output directory specified in the parameter file.

---

## 🧪 Experimental Results

We evaluated the **GE-based ensembles** against state-of-the-art methods, using **Pearson (PCC)** and **Spearman (SRCC)** correlation coefficients:

| **Dataset** | **Metric** | **GE** | **State-of-the-Art** |
|------------|-----------|--------|----------------------|
| MC30       | PCC       | 0.794  | 0.845 (LGP)         |
|            | SRCC      | 0.859  | 0.822 (LGP)         |
| GeReSiD50  | PCC       | 0.743  | 0.756 (LGP)         |
|            | SRCC      | 0.779  | 0.752 (LGP)         |
| WS353      | PCC       | 0.827  | 0.817 (LGP)         |
|            | SRCC      | 0.817  | 0.817 (LGP)         |

---

## 🧬 Technical Details

### Fitness Function
- Optimized to maximize correlation with human-annotated similarity judgments (PCC & SRCC).

### Genetic Operators
- **Crossover**: Variable one-point crossover (probability = 0.8).
- **Mutation**: Integer flip per codon.

### Grammatical Evolution
- Utilizes **BNF grammar** to define ensemble configurations.
- Evolves candidate ensembles iteratively through genetic programming.

---

## 📚 Citation

If you use this work in your research, please cite:

```bibtex
@article{martinez2023semanticGE,
  author       = {Jorge Martinez-Gil},
  title        = {Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution},
  journal      = {CoRR},
  volume       = {abs/2307.00925},
  year         = {2023},
  url          = {https://doi.org/10.48550/arXiv.2307.00925},
  doi          = {10.48550/arXiv.2307.00925},
  eprinttype   = {arXiv},
  eprint       = {2307.00925}
}
```

---

## 📄 License

This project is licensed under the **MIT License**. See the LICENSE file for details.
