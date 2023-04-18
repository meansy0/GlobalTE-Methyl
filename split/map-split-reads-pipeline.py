import os
import pysam
import sys
# tmux
    # tmux kill-session -t session-map-split
    # tmux new-session -d -s session-map-split \; send-keys "/home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/map-split-reads-pipeline.py" Enter


def split_fq_map(path,name):


    new_fold='map_split'

    new_path=path+'/'+new_fold

    if(os.path.exists(new_path)==False):
        os.system("mkdir "+new_path)
   
    path_hisat_3n="/home/xiaqini/extend_disk/arabidopsis/software/hisat-3n_allType/hisat-3n"
    index="/home/xiaqini/extend_disk/arabidopsis/data/C2T/hisat-3n-index/Col-0"    
    
    # left
    left_fastq_file=path+'/'+name+'-left-split.fastq'
    left_out_sam_file=new_path+'/'+name+'-left-split.sam'
    
    os.system(path_hisat_3n+" -x "+index+" -q "+left_fastq_file+" -S "+left_out_sam_file+" --base-change C,T  --base-change C,T --bowtie2-dp 1 -k 30 --score-min L,0,-0.5")

    # sam2bam
    left_bamfile=new_path+'/'+name+'-left-split.bam'
    os.system("samtools view -b "+left_out_sam_file+" > "+left_bamfile)
    if(os.path.exists(left_out_sam_file)==True): 
        os.remove(left_out_sam_file)

    # right
    right_fastq_file=path+'/'+name+'-right-split.fastq'
    right_out_sam_file=new_path+'/'+name+'-right-split.sam'
    # os.system(path_hisat_3n+" -x "+index+" -q "+right_fastq_file+" -S "+right_out_sam_file+" --base-change C,T --bowtie2-dp 2 -k 50 --score-min L,0,-1")
    os.system(path_hisat_3n+" -x "+index+" -q "+right_fastq_file+" -S "+right_out_sam_file+" --base-change C,T  --base-change C,T --bowtie2-dp 1 -k 30 --score-min L,0,-0.5")
    
    # os.system(path_hisat_3n+" -x "+index+" -q "+right_fastq_file+" -S "+right_out_sam_file+" --base-change C,T --no-repeat-index")
    # sam2bam
    right_bamfile=new_path+'/'+name+'-right-split.bam'
    os.system("samtools view -b "+right_out_sam_file+" > "+right_bamfile)
    if(os.path.exists(right_out_sam_file)==True): 
        os.remove(right_out_sam_file)
    if(os.path.exists(left_fastq_file)==True): 
        os.remove(left_fastq_file)
    if(os.path.exists(right_fastq_file)==True): 
        os.remove(right_fastq_file)

    return new_path,left_bamfile,right_bamfile


def filter_unmap_reads(new_path,name,left_bamfile,right_bamfile):
    left_map_bam=new_path+'/'+name+'-left-map.bam'
    os.system("samtools view -b -h -F 4 "+left_bamfile+" > "+left_map_bam)
    if(os.path.exists(left_bamfile)==True): 
        os.remove(left_bamfile)

    right_map_bam=new_path+'/'+name+'-right-map.bam'
    os.system("samtools view -b -h -F 4 "+right_bamfile+" > "+right_map_bam)
    if(os.path.exists(right_bamfile)==True): 
        os.remove(right_bamfile)

    return left_map_bam, right_map_bam


def intersecet_bed_bam(new_path,name,left_map_bam, right_map_bam):
    bedfile='/home/xiaqini/data/reference/test3.bed'


    # sort
    left_sort_bam=new_path+'/'+name+'-left-sort-map.bam'
    os.system("samtools sort -@8 "+left_map_bam+ " -o "+left_sort_bam)
    # left
    left_intersect_bam=new_path+'/'+name+'-left-intersect.bam'
    left_subtraction_bam=new_path+'/'+name+'-left-subtraction.bam'
    os.system("bedtools intersect -a "+left_sort_bam+" -b "+bedfile+" -f 0.95 > "+left_intersect_bam) 
    os.system("bedtools intersect -a "+left_sort_bam+" -b "+bedfile+" -f 0.95 -v > "+left_subtraction_bam)
    # os.system("samtools view -hb -L "+bedfile+" "+left_intersect_bam+" > "+left_intersect_bam)
    if(os.path.exists(left_sort_bam)==True): 
        os.remove(left_sort_bam)

    # sort
    right_sort_bam=new_path+'/'+name+'-right-sort-map.bam'
    os.system("samtools sort -@8 "+right_map_bam+ " -o "+right_sort_bam)
    # right
    right_intersect_bam=new_path+'/'+name+'-right-intersect.bam'
    right_subtraction_bam=new_path+'/'+name+'-right-subtraction.bam'
    # os.system("samtools view -b -L "+bedfile+" "+right_intersect_bam+" > "+right_intersect_bam)
    os.system("bedtools intersect -a "+right_sort_bam+" -b "+bedfile+" -f 0.95 > "+right_intersect_bam) 
    os.system("bedtools intersect -a "+right_sort_bam+" -b "+bedfile+" -f 0.95 -v > "+right_subtraction_bam)
    if(os.path.exists(right_sort_bam)==True): 
        os.remove(right_sort_bam)
    return left_intersect_bam,right_intersect_bam

def filterNotFullMap(new_path,name,left_map_bam, right_map_bam):
    out_left_map_path=new_path+'/'+name+'-left-full-map.bam'
    out_right_map_path=new_path+'/'+name+'-right-full-map.bam'
    input_bamfile1=pysam.AlignmentFile(left_map_bam,'rb')
    input_bamfile2=pysam.AlignmentFile(right_map_bam,'rb')
    out_left_map=pysam.AlignmentFile(out_left_map_path, "w", template=input_bamfile1)
    out_right_map=pysam.AlignmentFile(out_right_map_path, "w", template=input_bamfile2)

    for line1 in input_bamfile1:
        cigar=line1.cigar
        # print(cigar)
        i=0
        len0=0
        all=0
        N_type1=0
        while i<len(cigar):
            reads_type=cigar[i][0]
            reads_length=cigar[i][1]
            # print(reads_type)
            # print(name)
            # print(cigar_number)
            # match
            if(reads_type==0 or reads_type==7):
                len0=reads_length+len0
            if(reads_type!=3):
                all=reads_length+all
            if(reads_type==3):
                N_type1=8
            i=i+1
        if(all!=0):
            if(len0/all>=0.90 and N_type1!=8):
                out_left_map.write(line1)


    for line2 in input_bamfile2:
        cigar=line2.cigar
        # print(cigar)
        i=0
        len0=0
        all=0
        N_type2=0
        while i<len(cigar):
            reads_type=cigar[i][0]
            reads_length=cigar[i][1]
            # print(reads_type)
            # print(name)
            # print(cigar_number)
            # match
            if(reads_type==0 or reads_type==7):
                len0=reads_length+len0
            if(reads_type!=3):
                all=reads_length+all
            if(reads_type==3):
                N_type2=8
            i=i+1
        if(all!=0):
            if(len0/all>=0.95 and N_type2!=8):
                out_right_map.write(line2)
    if(os.path.exists(left_map_bam)==True): 
        os.remove(left_map_bam)
    if(os.path.exists(right_map_bam)==True): 
        os.remove(right_map_bam)
    return out_left_map_path,out_right_map_path        


if __name__=='__main__':


    # path='/home/xiaqini/extend_disk/arabidopsis/data/C2T/new_te_test'
    # name='1662'
    path=sys.argv[1]
    name=sys.argv[2]
    print(path)
    # step 1 map the split left and right fastq
    new_path,left_bamfile,right_bamfile=split_fq_map(path,name)

    # step2 filter unmap
    left_map_bam, right_map_bam=filter_unmap_reads(new_path,name,left_bamfile,right_bamfile)

    # step 2.1 filter map<0.90
    out_left_map_path,out_right_map_path=filterNotFullMap(new_path,name,left_map_bam, right_map_bam)

    # step3 intersect bam bed
    left_intersect_bam,right_intersect_bam=intersecet_bed_bam(new_path,name,out_left_map_path, out_right_map_path)

