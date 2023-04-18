# graduationPro
# date:from 2022-10 to 2023-4
# author:qinixia

# folder:split
## enviroment:python3.7(packages:pysam,os,numpy)
## tools:bedtools v2.27.1, samtools v1.10 (using htslib 1.10.2-3)
## use: input the path and name of the ecotype
## description:It is worth noting that this should include a fastq file, to which the predicted results will be output in txt format. 
  + In addition, the results were automatically counted by superfamily, including the transposon activity, insertion site and transpose number of each superfamily.

# folder:temp2
## enviroment:python2.7(packages:os)
## tools:temp2:input the path and name of the ecotype
## description:Used to detect non-reference transposons

# folder:genomesize
## enviroment:R 4.0.5
## tools:kmergenie:input the path and name of the ecotype
## description:Using the genome sequencing fastq file, the genome size was predicted by kmer's principle

# folder:active
## enviroment:python3.7
## description:All results are summarized

# folder:active
## enviroment:R 4.0.5
## description:Contains all the code for plotting and statistical analysis

