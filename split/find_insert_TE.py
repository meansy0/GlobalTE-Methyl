import os
import pysam
import sys
# tmux
    # tmux kill-session -t session7
    # tmux new-session -d -s session7 \; send-keys "/home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/find_insert_TE.py"
# /home/xiaqini/anaconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/find_insert_TE.py
def IntersectAndSubtractionSame(path,name):
    input_left_bam_intersect=path+'/'+name+'-left-intersect.bam'
    input_right_bam_subtraction=path+'/'+name+'-right-subtraction.bam'

    out_left_TE_location=path+'/'+name+'-left-TE-location.bam'
    out_right_TE_intersect=path+'/'+name+'-right-TE-insert.bam'
    out_TE_insert_information=path+'/'+name+'-TE-insert-location-information.txt'

    left_bam_intersect_file=pysam.AlignmentFile(input_left_bam_intersect,"rb")
    

    right_bam_subtraction_file=pysam.AlignmentFile(input_right_bam_subtraction,"rb")
    left_TE_location_file=pysam.AlignmentFile(out_left_TE_location, "w", template=left_bam_intersect_file)
    right_TE_intersect_file=pysam.AlignmentFile(out_right_TE_intersect, "w", template=right_bam_subtraction_file)
    right_bam_subtraction_file.close()
    TE_insert_information_file=open(out_TE_insert_information,'w')
    TE_insert_information_file.write("reads_name\tChr_name\tTE_start\tTE_end\tmethylation_level\ttotal_C_sites\tinsert_chr_name\tinsert_start\tinsert_end\n")

    for line1 in left_bam_intersect_file:
        right_bam_subtraction_file=pysam.AlignmentFile(input_right_bam_subtraction,"rb")
        
        segement_name1=line1.query_name
        
        # Yf
        Yf_tag=line1.get_tag('Yf',with_value_type=False)
        methylation_level=Yf_tag
        # Zf
        Zf_tag=line1.get_tag('Zf',with_value_type=False)
        total_C=Yf_tag+Zf_tag

        Chr_name=line1.reference_name
        TE_start=line1.reference_start+1
        TE_end=line1.reference_end+1
        # print(Chr_name+ '\t'+str(TE_start)+'\t'+ str(TE_end))
        for line2 in right_bam_subtraction_file:
            insert_start=line2.reference_start+1
            insert_end=line2.reference_end+1
            segement_name2=line2.query_name
            # insert_seq=line2.get_forward_sequence()
            
            # print("1:"+segement_name1+"\t2:"+segement_name2)
            insert_chr_name=line2.reference_name
            if(segement_name1==segement_name2):
                # print(insert_seq)
                print(segement_name2+":success")
                left_TE_location_file.write(line1)
                right_TE_intersect_file.write(line2)
                TE_insert_information_file.write(segement_name1+'\t'+Chr_name+'\t'+str(TE_start)+'\t'+str(TE_end)+'\t'+str(methylation_level)+'\t'+str(total_C)+'\t'+insert_chr_name+'\t'+str(insert_start)+'\t'+str(insert_end)+'\n')
                continue
            if(segement_name1!=segement_name2):
                continue
        right_bam_subtraction_file.close()
    # os.remove(input_left_bam_intersect)
    # os.remove(input_right_bam_subtraction)

    input_left_bam_subtraction=path+'/'+name+'-left-subtraction.bam'
    input_right_bam_intersect=path+'/'+name+'-right-intersect.bam'

    out_left_TE_insert=path+'/'+name+'-left-TE-insert.bam'
    out_right_TE_location=path+'/'+name+'-right-TE-location.bam'
    out_TE_insert_information=path+'/'+name+'-insert-TE-location-information.txt'

    left_bam_subtraction_file=pysam.AlignmentFile(input_left_bam_subtraction,"rb")
    right_bam_intersect_file=pysam.AlignmentFile(input_right_bam_intersect,"rb")


    left_TE_insert_file=pysam.AlignmentFile(out_left_TE_insert, "w", template=left_bam_subtraction_file)
    left_bam_subtraction_file.close()
    right_TE_location_file=pysam.AlignmentFile(out_right_TE_location, "w", template=right_bam_intersect_file)
    TE_insert_information_file=open(out_TE_insert_information,'w')
    TE_insert_information_file.write("reads_name\tChr_name\tTE_start\tTE_end\tmethylation_level\ttotal_C_sites\tinsert_chr_name\tinsert_start\tinsert_end\n")
    for line3 in right_bam_intersect_file:
        segement_name3=line3.query_name
        left_bam_subtraction_file=pysam.AlignmentFile(input_left_bam_subtraction,"rb")
        # Yf
        Yf_tag=line3.get_tag('Yf',with_value_type=False)
        methylation_level=Yf_tag
        # Zf
        Zf_tag=line3.get_tag('Zf',with_value_type=False)
        total_C=Yf_tag+Zf_tag

        Chr_name=line3.reference_name
        TE_start=line3.reference_start+1
        TE_end=line3.reference_end+1
        # print(Chr_name+ '\t'+str(TE_start)+'\t'+ str(TE_end))
        for line4 in left_bam_subtraction_file:

            insert_chr_name=line4.reference_name
            insert_start=line4.reference_start+1
            insert_end=line4.reference_end+1
            segement_name4=line4.query_name
            # print("1:"+segement_name1+"\t2:"+segement_name2)

            if(segement_name3==segement_name4):
                print("success")

                right_TE_location_file.write(line3)
                left_TE_insert_file.write(line4)
                TE_insert_information_file.write(segement_name3+'\t'+Chr_name+'\t'+str(TE_start)+'\t'+str(TE_end)+'\t'+str(methylation_level)+'\t'+str(total_C)+'\t'+insert_chr_name+'\t'+str(insert_start)+'\t'+str(insert_end)+'\n')
                continue
            if(segement_name3!=segement_name4):
                continue
        left_bam_subtraction_file.close()
        
    # os.remove(input_left_bam_subtraction)
    # os.remove(input_right_bam_intersect)
if __name__=='__main__':


    path=sys.argv[1]
    name=sys.argv[2]

    # step1 find the same segements in intersect(left) and subtraction(right) or intersect(right) and subtraction(left)
    IntersectAndSubtractionSame(path,name)