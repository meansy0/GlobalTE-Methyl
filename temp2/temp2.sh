# path=$1 
# name=$2

cd $1
# export PATH="/usr/local/bin:$PATH"


# need
# export PATH=/bin:$PATH
# export SAMTOOLS_BINARY=/bin/samtools
bwa_index=/home/xiaqini/extend_disk/arabidopsis/g4/index/Col-0.fa
fa=/home/xiaqini/extend_disk/arabidopsis/g4/index/Col-0.fa
te_fa=/home/xiaqini/newdata/reference/masked/te.fa
bed=/home/xiaqini/newdata/reference/masked/Col-0.fa-filter.bed

# fq_rm="${2}-1.all.fastq.gz"
# if [ -s "$fq_rm" ]; then
#     mv "${2}_1.all.fastq.gz" "${2}-1.all.fastq.gz"
#     mv "${2}_2.all.fastq.gz" "${2}-2.all.fastq.gz"
# fi

fq1=$2-1.all.fastq.gz
fq2=$2-2.all.fastq.gz
if [ -s "$fq1" ] && [ -s "$fq2" ];then
    samfile=$2-output/$2-1.all.fastq.gz.sam
    bamfile=$2-output/$2-1.all.fastq.gz.bam

    TEMP2 insertion -l $fq1 -r $fq2 -I $bwa_index -g $fa -R $te_fa -t $bed -o $2-output -c 6
fi
# TEMP2 insertion -l 9895-1.all.fastq.gz -r 9895-2.all.fastq.gz -I 
# /home/xiaqini/extend_disk/arabidopsis/g4/index/Col-0.fa -g 
# /home/xiaqini/extend_disk/arabidopsis/g4/index/Col-0.fa -R 
# /home/xiaqini/newdata/reference/masked/te.fa -t 
# /home/xiaqini/newdata/reference/masked/Col-0.fa-filter.bed -o 
# output -c 2


# export PATH=/bin:$PATH
# export PATH=/bin/:$PATH
# export SAMTOOLS_BINARY=/bin/samtools