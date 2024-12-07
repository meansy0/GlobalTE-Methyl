### GlobalTE-Methyl  
**Date**: From 2022-10 to 2023-06  
**Author**: Qinixia  
**Current Status**: Manuscript in progress  

---

### Project Overview
This project focuses on the global dataset of **Arabidopsis thaliana** from the **1001 Genomes Project**, which includes approximately **500 different ecotypes** of **Arabidopsis** genomes and bisulfite sequencing data. A novel method for detecting active **Transposable Elements (TEs)** was developed (version 1.0), with the aim to investigate the relationship between **G4 quadruplex**-forming TEs and **DNA methylation**. The project explores how **environmental factors** influence the evolution of these elements globally. **Note**: The code for the TE detection method (version 1.0) is still under development and has not yet been uploaded.

### Tools and Technologies
- **FastQC**: For quality control of sequencing data.
- **BEDTools v2.27.1**: For genomic interval manipulation and analysis.
- **Samtools v1.10**: For working with SAM/BAM files.
- **Kmergenie**: For genome size estimation based on k-mer distributions.
- **Python 3.7**: For data processing and analysis.
- **R 4.0.5**: For statistical analysis and plotting.

---

### Folder Structure and Descriptions

#### 1.    **split**
- **Environment**: Python 3.7
- **Dependencies**: `pysam`, `os`, `numpy`
- **Tools**: **bedtools v2.27.1**, **samtools v1.10** (using htslib 1.10.2-3)
- **Description**: This folder is used for processing **FastQ** files of Arabidopsis ecotypes.    After inputting the path and name of the ecotype, predicted results are output as text files.    Results are automatically summarized by superfamily, including details on transposon activity, insertion sites, and the number of transposes for each superfamily.

#### 2.    **temp2**
- **Environment**: Python 2.7
- **Tools**: Custom Python scripts for detecting non-reference transposons.
- **Description**: This folder contains scripts for identifying **non-reference TEs**, focusing on the detection of active transposable elements that are not present in the reference genome.

#### 3.    **genomesize**
- **Environment**: R 4.0.5
- **Tools**: **kmergenie**
- **Description**: Using the genome sequencing **FastQ** files, this tool estimates the **genome size** based on the k-mer distribution, a common approach for genome size prediction.

#### 4.    **active**
- **Environment**: Python 3.7
- **Description**: This folder summarizes all the results related to active transposons, including the identification of active TEs across different ecotypes, and their relationship to methylation patterns and environmental factors.

#### 5.    **active** (R-based)
- **Environment**: R 4.0.5
- **Description**: Contains all the code for **statistical analysis** and **visualization** of the data, including plotting methylation patterns, TE activity, and environmental influences on evolution.

---

### Project Focus
- **Objective**: Investigate the relationship between **G4 quadruplexes** and **DNA methylation** in transposable elements (TEs) across a global sample of Arabidopsis ecotypes.
- **Key Questions**:
1.    How do environmental factors affect the evolution of TEs?
2.    What role does DNA methylation play in regulating TE activity, specifically in relation to G4-forming TEs?
3.    Can global datasets shed light on the evolutionary mechanisms shaping transposon dynamics?

- **Limitations**: The current version of the TE detection method (v1.0) is still under development and may have accuracy limitations due to the constraints of short-read sequencing technology.

---

### Notes
- This project utilizes data from **the 1001 Genomes Project**, which includes a diverse range of ecotypes, providing a rich dataset for analyzing global variations in transposon dynamics and methylation patterns.
