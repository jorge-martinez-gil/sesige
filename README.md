# Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution

[![arXiv](https://img.shields.io/badge/arXiv-2307.00925-b31b1b.svg)](https://arxiv.org/abs/2307.00925)

## 🌟 Overview

Semantic similarity measures play a pivotal role in natural language processing (NLP) tasks. This repository accompanies the paper [**"Automatic Design of Semantic Similarity Ensembles Using Grammatical Evolution"**](https://arxiv.org/abs/2307.00925), which introduces a **Grammatical Evolution (GE)-based framework** for **automatic design and optimization of semantic similarity ensembles**. The proposed method enables the dynamic creation of highly accurate and interpretable ensembles, outperforming state-of-the-art techniques on benchmark datasets.

---

## ✨ Key Contributions

- **Novel Application of Grammatical Evolution**: First use of GE for designing semantic similarity ensembles.
- **Dynamic Aggregation**: Combines multiple similarity measures to create optimized ensembles.
- **Interpretable and Accurate**: Balances high performance with model interpretability.
- **Benchmark Comparisons**: Demonstrates superiority over existing ensemble methods on MC30 and GeReSiD50 datasets.

---

## 📊 Features

- Automated generation of semantic similarity ensembles guided by Backus-Naur Form (BNF) grammar.
- Support for correlation-based optimization using Pearson and Spearman metrics.
- Integration with the **PonyGE2** framework for evolutionary computation.
- Results validated on standard datasets: **MC30** and **GeReSiD50**.

---

## 🛠️ Installation

To run the experiments, you need to install and set up the **PonyGE2** framework:

1. Clone the [PonyGE2 repository](https://github.com/PonyGE/PonyGE2).
2. Clone this repository:
   ```bash
   git clone https://github.com/<YourRepo>/semantic-similarity-ge.git
   ```
3. Overwrite the **PonyGE2** files with those provided in this repository:
   ```bash
   cp -r ./semantic-similarity-ge/* ./PonyGE2/
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📈 Evaluation Datasets

### 1. MC30
- Contains 30 word pairs with semantic similarity scores based on human judgments.
- Focuses on general-purpose semantic similarity.

### 2. GeReSiD50
- Contains 50 phrase pairs with semantic similarity ratings from geospatial research.
- Includes domain-specific textual data for testing ensemble generalization.

---

## ⚙️ Usage

After setting up the **PonyGE2** framework:

1. Navigate to the `src` directory of **PonyGE2**:
   ```bash
   cd ./PonyGE2/src
   ```
2. Run the grammatical evolution process using the provided parameter file:
   ```bash
   python ponyge.py --parameters ./parameters/semantic_similarity.txt
   ```
3. View results in the output directory specified in the parameters file.

---

## 🧪 Results Summary

**Performance Metrics:**
- Evaluated using Pearson Correlation Coefficient (PCC) and Spearman Rank Correlation Coefficient (SRCC).
- Achieved superior performance on MC30 and GeReSiD50 benchmarks compared to state-of-the-art methods.

| **Dataset** | **Metric** | **GE** | **State-of-the-Art** |
|-------------|------------|--------|----------------------|
| MC30        | PCC        | 0.794  | 0.845 (LGP)         |
|             | SRCC       | 0.859  | 0.822 (LGP)         |
| GeReSiD50   | PCC        | 0.743  | 0.756 (LGP)         |
|             | SRCC       | 0.779  | 0.752 (LGP)         |

---

## 🧬 Technical Details

### Fitness Function
- Optimized for correlation with human judgment using PCC and SRCC.

### Genetic Operators
- **Crossover**: Variable one-point crossover with a probability of 0.8.
- **Mutation**: Integer flip per codon.

### Grammatical Evolution
- Defined using BNF grammar for generating ensemble configurations.

---

## 📚 Citation

If you use this work in your research, please cite:

```bibtex
@article{martinez2003c,
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

This project is licensed under the MIT License. See the LICENSE file for details.