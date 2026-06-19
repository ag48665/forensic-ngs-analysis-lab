# Forensic NGS Analysis Lab

Bioinformatics project exploring core next-generation sequencing (NGS) concepts including FASTQ generation, quality assessment, variant detection, and experimental evaluation.

## Overview

Next-generation sequencing (NGS) has become an important technology in modern genomics, enabling large-scale DNA analysis, variant discovery, and forensic applications.

This project simulates core steps of an NGS analysis workflow using Python, including sequencing read generation, quality assessment, variant detection, and experimental evaluation.

The framework provides an educational introduction to bioinformatics concepts commonly used in genomic and forensic laboratories.

---
## Project Highlights

✔ FASTQ read simulation

✔ Quality control using Phred scores

✔ Sequencing error simulation

✔ Variant calling workflow

✔ SNP detection experiments

✔ Monte Carlo simulation framework

✔ Reproducible Python-based genomics analysis

---

## Scientific Motivation

NGS technologies are increasingly used in:

* Forensic genomics
* Human identification
* Missing persons investigations
* Disaster victim identification
* Population genetics
* Medical genomics
* Variant discovery

This project demonstrates simplified computational approaches for processing sequencing data and identifying genetic variation.

---

## FASTQ Simulation

The project generates synthetic sequencing reads in FASTQ format.

Example FASTQ structure:

```text
@read_0
ACGTACGTACGTACGT
+
IIIIIIIIIIIIIIII
```

Each read contains:

* Read identifier
* DNA sequence
* Separator line
* Quality score string

---

## Quality Control

Sequencing quality is assessed using simplified Phred quality scores.

Example result:

| Metric                | Value |
| --------------------- | ----- |
| Average Phred Quality | 40.0  |

High-quality sequencing data improves confidence in downstream variant detection.

---

## Variant Calling

The project implements a simplified variant calling approach.

A known SNP variant is introduced into a reference sequence and sequencing reads are generated from the modified genome.

The variant caller compares sequencing reads to the reference sequence and counts observed nucleotide differences.

Example detected variant:

```text
(20, 'A', 'T') count = 99
```

This indicates strong support for a true SNP at position 20.

---

## NGS Variant Detection Experiment

The experiment evaluates how consistently a simulated SNP variant can be detected across multiple sequencing runs.

![NGS Experiment](reports/ngs_experiment.png)

Example result:

| Metric                  | Value |
| ----------------------- | ----- |
| Average Variant Support | 77.01 |

Results demonstrate reliable detection of true variants despite sequencing noise and random sampling effects.

---

## Key Results

| Analysis                | Result     |
| ----------------------- | ---------- |
| Average Phred Quality   | 40.0       |
| Average Variant Support | 77.01      |
| Variant Detection       | Successful |

The experiment demonstrates that true variants can be reliably detected despite sequencing noise introduced during read generation.

---
## Key Takeaway

This project demonstrates how sequencing quality, read sampling, and variant support influence SNP detection within a simplified NGS environment.

Although educational in scope, the workflow reproduces several key concepts used in real-world genomic and forensic sequencing pipelines.

---

## Research Questions

1. How does sequencing quality affect variant detection?
2. How do sequencing errors influence forensic interpretation?
3. How can NGS support forensic genomics?
4. How can variant calling be simulated computationally?
5. How can sequencing noise be distinguished from true genetic variation?

---
## Skills Demonstrated

### Bioinformatics

- FASTQ processing
- Quality control concepts
- Variant detection
- Sequencing error modelling
- NGS workflow design
- Genomic data analysis

### Programming

- Python
- Data simulation
- Statistical analysis
- Data visualization
- Reproducible workflows

### Genomics

- DNA sequencing
- SNP identification
- Variant interpretation
- Forensic genomics

---
## Methods

* FASTQ simulation
* DNA read generation
* Sequencing error simulation
* Phred quality assessment
* Variant calling
* SNP detection
* Monte Carlo experiments
* Data visualization using Python

---

## Project Structure

```text
forensic-ngs-analysis-lab/
│
├── reports/
│   ├── ngs_experiment.png
│   └── ngs_results.csv
│
├── src/
│   ├── fastq_simulator.py
│   ├── quality_control.py
│   ├── variant_calling.py
│   ├── ngs_experiment.py
│   └── plot_ngs_results.py
│
├── data/
├── notebooks/
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
```

Run analyses:

```bash
python src/fastq_simulator.py
python src/quality_control.py
python src/variant_calling.py
python src/ngs_experiment.py
```

Generate visualization:

```bash
python src/plot_ngs_results.py
```

---
Future Work 

* Read alignment using BWA
* SAM/BAM processing
* Variant calling with bcftools
* VCF generation and parsing
* Integration with publicly available genomic datasets
---

## Disclaimer

This project is intended for educational and research-training purposes only.

It is not validated for forensic casework and must not be used in real investigations.

---

## Author

**Agata Gabara**

Incoming MSc Bioinformatics Student

Research Interests:

- Cancer Genomics
- Computational Biology
- NGS Analysis
- Population Genetics
- Machine Learning for Genomics

GitHub: https://github.com/ag48665

LinkedIn: https://www.linkedin.com/in/agatha-gabara-06494a37/
