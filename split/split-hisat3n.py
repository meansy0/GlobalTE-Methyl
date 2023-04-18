import os
import pysam

# infor-split pipeline
# 1 /home/xiaqini/extend_disk/arabidopsis/scripts/split-hisat3n.py
# 2 /home/xiaqini/extend_disk/arabidopsis/scripts/map-split-reads-pipeline.py
# 3 /home/xiaqini/extend_disk/arabidopsis/scripts/find_insert_TE.py
# 4 /home/xiaqini/extend_disk/arabidopsis/scripts/insert_TE_analysis.py

# tmux 
    # tmux kill-session -t session77
    # tmux new-session -d -s session88 \; send-keys "/home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/split-hisat3n.py" Enter

# /home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/split-hisat3n.py
from splitSegemehl import filter_sort_bam 
from splitSegemehl import filter_sort_filter_bam
from splitSegemehl import get_split_infor_from_sort_bam
from splitSegemehl import split_txt_infor
from splitSegemehl import filter_sort_single_bam
from splitSegemehl import split_fastq


def filterNInSamfile(bamfile,path,name):
    bam_with_n_file=path+'/'+name+'-skip-map.bam'
    bam_without_n_file=path+'/'+name+'-filter-Cigar-not-N.bam'

    input_bamfile=pysam.AlignmentFile(bamfile,'rb')
    outfile1=pysam.AlignmentFile(bam_with_n_file, "w", template=input_bamfile)
    outfile2=pysam.AlignmentFile(bam_without_n_file, "w", template=input_bamfile)
    for line in input_bamfile:
        string=str(line.cigarstring)
        if(string.find('N')==-1 and string.find('*')==-1):
            outfile2.write(line)
        if(string.find('N')!=-1):
            outfile1.write(line)

    # os.system("samtools view "+bamfile+" | awk '$6 ~ /N/' | samtools view -bS - > "+bam_with_n_file)
    # os.system("samtools view "+bamfile+" | awk '$6 ~!/N/' | samtools view -bS - > "+bam_without_n_file)
    return bam_with_n_file,bam_without_n_file


def filterFullMap(bam_without_n_file,path,name):
    filter_full_without_N_file=path+'/'+name+'-filter-fullM-without-N.bam'
    save_full_without_N_file=path+'/'+name+'-save-fullM-without-N.bam'
    
    input_bamfile=pysam.AlignmentFile(bam_without_n_file,"rb")
    output_bamfile=pysam.AlignmentFile(filter_full_without_N_file, "w", template=input_bamfile)
    output_bamfile2=pysam.AlignmentFile(save_full_without_N_file, "w", template=input_bamfile)
    for line in input_bamfile:
        cigar=line.cigar
        # print(cigar)
        i=0
        len0=0
        all=0
        while i<len(cigar):
            reads_type=cigar[i][0]
            reads_length=cigar[i][1]
            # print(reads_type)
            # print(name)
            # print(cigar_number)
            if(reads_type==0 or reads_type==7):
                
                len0=reads_length+len0
            if(reads_type!=3):
                all=reads_length+all
            i=i+1
        if(all!=0):
            if(len0/all<=0.7):
                output_bamfile.write(line)
            else:
                output_bamfile2.write(line)
    return filter_full_without_N_file,save_full_without_N_file

if __name__=='__main__':


    path='/home/ubuntu/data/Arabidopsis_sequence_2/arabidopsis/data/4958'
    name='4958'

    # 915.mc.fastq.gz_unmapped_reads.fq
    zip_fastq_file=path+'/'+name+'.mc.fastq.gz_unmapped_reads.fq.gz'

    os.system("gunzip "+zip_fastq_file)
    # step0:hisat-3n mapping
    path_hisat_3n="/home/xiaqini/extend_disk/arabidopsis/software/hisat-3n_allType/hisat-3n"
    index="/home/xiaqini/extend_disk/arabidopsis/data/C2T/hisat-3n-index/Col-0"
# /home/xiaqini/extend_disk/arabidopsis/data/915/915.mc.fastq.gz_unmapped_reads.fq.gz
# /home/xiaqini/extend_disk/arabidopsis/data/915/915.mc.fastq.gz_unmapped_reads.fq
    fastq_file=path+'/'+name+'.mc.fastq.gz_unmapped_reads.fq'
    out_sam_file=path+'/'+name+'-hisat.sam'
    os.system(path_hisat_3n+" -x "+index+" -q "+fastq_file+" -S "+out_sam_file+" --base-change C,T --bowtie2-dp 2 -k 50 --score-min L,0,-1")
    # sam2bam
    bamfile=path+'/'+name+'-hisat.bam'
    os.system("samtools view -bS "+out_sam_file+" > "+bamfile)
    # os.system("samtools sort "+out_sam_file +" -o "+bamfile)]
    if(os.path.exists(out_sam_file)==True):
        os.remove(out_sam_file)


    # step1: divided into two types: with and without N
    # input: hisat3n bamfile
    # output: 1 bamfile N; 2 bamfile withoutN
    
    bam_with_n_file,bam_without_n_file=filterNInSamfile(bamfile,path,name)

    # step2:deal the without n bamfile:
        # step 2.1:filter the full map
    filter_full_without_N_file,save_full_without_N_file=filterFullMap(bam_without_n_file,path,name)
    if(os.path.exists(bam_without_n_file)==True):
        os.remove(bam_without_n_file)
    new_name_save_full_without_N_file=path+'/'+name+'-full-map.bam'
    os.system("mv "+save_full_without_N_file+" "+new_name_save_full_without_N_file)

        # step 2.2:sort the filter_full_without_N_file
    # -@8：8个线程 -o：输出文件
    sortMapFile=path+'/'+name+'-filter-fullM-without-N-sort.bam'
    os.system('samtools sort -@8 -n '+filter_full_without_N_file+' -o '+sortMapFile)
    new_name_filter_full_without_N_file=path+'/'+name+'-not-full-map.bam'
    os.system("mv "+filter_full_without_N_file+" "+new_name_filter_full_without_N_file)
    

    # filter the segment mapping multiple locations
    # output:name-sort-filter.bam
    sort_filter_bamfile=filter_sort_bam(path,name,sortMapFile)

    if(os.path.exists(sortMapFile)==True):
        os.remove(sortMapFile)
    # delete the fullly bame mapping in different locations 
    # output:name-delete-bame-mapping.bam
    delete_bame_mappin_bamfile=filter_sort_filter_bam(path,name,sort_filter_bamfile)
    if(os.path.exists(sortMapFile)==True):
        os.remove(sortMapFile)
    
    # filter the segment mapping multiple locations
    # output:name-sort-filter.bam
    sort_filter_bamfile=filter_sort_bam(path,name,delete_bame_mappin_bamfile)
    if(os.path.exists(delete_bame_mappin_bamfile)==True):
        os.remove(delete_bame_mappin_bamfile)
    

    #  get split infor
    # test data
    # sort_filter_bamfile='/home/xiaqini/extend_disk/test/split-test-sort-filter.bam'
    # output:name-split-infor.txt
    split_txtfile=get_split_infor_from_sort_bam(path,name,sort_filter_bamfile)
    # output:-split-information.txt
    txtfile=split_txt_infor(path,name,split_txtfile)
    if(os.path.exists(split_txtfile)==True):
        os.remove(split_txtfile)

    # bam to fastq
    # filter repeated segment
    # output:name-sort-filter-single.bam
    sort_filter_single_bamfile=filter_sort_single_bam(path,name,sort_filter_bamfile)
    bam_fastqfile=path+"/"+name+"-sort-filter.fastq"
    if(os.path.exists(sort_filter_bamfile)==True):
        os.remove(sort_filter_bamfile)
    # sort bam
    sorted_file=path+"/"+name+"-test-xx.bam"
    os.system("samtools sort -n "+sort_filter_single_bamfile+" -o "+sorted_file)
    os.system("bamToFastq -i "+sorted_file+" -fq "+bam_fastqfile)
    if(os.path.exists(sorted_file)==True):
        os.remove(sorted_file)
    if(os.path.exists(sort_filter_single_bamfile)==True): 
        os.remove(sort_filter_single_bamfile)

    # split
    left_fastqfile1,right_fastqfile=split_fastq(path,name,txtfile,bam_fastqfile)
    if(os.path.exists(bam_fastqfile)==True): 
        os.remove(bam_fastqfile)
    if(os.path.exists(txtfile)==True): 
        os.remove(txtfile)
    if(os.path.exists(fastq_file)==True): 
        os.remove(fastq_file)

    # 2 /home/xiaqini/extend_disk/arabidopsis/scripts/map-split-reads-pipeline.py
    os.system("/home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/map-split-reads-pipeline.py "+path+" "+name)

    # 3 /home/xiaqini/extend_disk/arabidopsis/scripts/find_insert_TE.py
    os.system("/home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/find_insert_TE.py "+path+"/map_split "+name)

    # 4 /home/xiaqini/extend_disk/arabidopsis/scripts/insert_TE_analysis.py
    os.system("/home/ubuntu/miniconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/insert_TE_analysis.py "+path+"/map_split "+name)

    # 5 /home/xiaqini/extend_disk/arabidopsis/scripts/copy_te.py

    os.system("/home/ubuntu/miniconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/copy_te.py "+path+" "+name)