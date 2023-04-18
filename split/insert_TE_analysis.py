import os
import re
import sys
from decimal import Decimal

def count_copy(input,out_file):

    in_file=open(input,'r')
    out=open(out_file,'w')
    te_number_last=0
    count=0
    xx=0
    for line in in_file:
        xx=xx+1
        te_number_now=line.split('\t')[1]
        if(xx==1):
            count=1
            te_number_last=te_number_now
            continue
        
        if(te_number_last!=te_number_now):

            out.write(te_number_last+'\t'+str(count)+'\n')
            count=1

            te_number_last=te_number_now
            continue

        if(te_number_last==te_number_now):
            count=count+1

        te_number_last=te_number_now

    out.write(te_number_last+'\t'+str(count)+'\n')    
    out.close()
    in_file.close()

    os.system("sort -k 1 "+out_file+" -o "+out_file)
    # os.remove(input)

    print("total copy te by ID:")
    os.system("cat "+out_file+" | awk '{print $2}' | awk '{sum+=$1}END{print sum}'")
    return out_file


def getTEInfor(path,name):


    new_fold='insert_TE'
    new_path=path+'/'+new_fold
    if(os.path.exists(new_path)==False):
        os.system("mkdir "+new_path)
    te_insert_txt=path+'/'+name+'-TE-insert-location-information.txt'
    insert_te_txt=path+'/'+name+'-insert-TE-location-information.txt'

    input_te_insert=open(te_insert_txt,'r')
    te_insert_infor=new_path+'/'+name+'-TE-insert-infor.txt'
    out_te_insert_txt=open(te_insert_infor,'w')
    out_te_insert_txt.write('Te_number\tTe_ID&name\tTe_alias\tTe_strain\treads_name\tChr_name\tTe_start\tTe_end\tmethylation_level\ttotal_C_sites\tinsert_start\t insert_end\n')

    input_insert_te=open(insert_te_txt,'r')
    insert_te_infor=new_path+'/'+name+'-insert-TE-infor.txt'
    out_insert_te_txt=open(insert_te_infor,'w')
    out_insert_te_txt.write('Te_number\tTe_ID&name\tTe_alias\tTe_strain\treads_name\tChr_name\tTe_start\tTe_end\tmethylation_level\ttotal_C_sites\tinsert_start\t insert_end\n')

    bedfile='/home/xiaqini/extend_disk/arabidopsis/data/reference/test3.bed'
    
    xx=1
    for line1 in input_te_insert:
        number=0
        
        input_bed=open(bedfile,'r')
        if(xx==1):
            xx=2
            continue
        te_start_txt1=int(line1.split('\t')[2])
        te_end_txt1=int(line1.split('\t')[3])
        len_error_txt1=(te_end_txt1-te_start_txt1)*0.05
        txt_chr=line1.split('\t')[1]
        for line in input_bed:
            number=number+1
            type_string=str(line.split('\t')[9])
            result= re.findall(".*=(.*);.*",type_string)
            te_id=str(result[0])
            bed_chr=line.split('\t')[0]
            # te_name=result[1]
            te_alias0=str(type_string.split('=')[3])
            te_alias=te_alias0[:-1]
            te_strain=str(line.split('\t')[5])
            te_start_bed=int(line.split('\t')[1])
            te_end_bed=int(line.split('\t')[2])
            if((te_start_bed-len_error_txt1)<=te_start_txt1 and (te_end_bed+len_error_txt1)>=te_end_txt1 and txt_chr==bed_chr):
                print("get the insert te:"+str(number))
                out_te_insert_txt.write(str(number)+'\t'+te_id+'\t'+te_alias+'\t'+te_strain+'\t'+line1)
                break
            else:
                continue
        input_bed.close()
    input_te_insert.close()
    bedfile='/home/xiaqini/extend_disk/arabidopsis/data/reference/test3.bed'
    
    yy=1  
    for line2 in input_insert_te:
        
        number=0
        input_bed=open(bedfile,'r')  
        if(yy==1):
            yy=2
            continue
        te_start_txt2=int(line2.split('\t')[2])
        te_end_txt2=int(line2.split('\t')[3])
        len_error_txt2=(te_end_txt2-te_start_txt2)*0.05
        txt_chr=line2.split('\t')[1]
        for line in input_bed:
            number=number+1
            type_string=str(line.split('\t')[9])
            result= re.findall(".*=(.*);.*",type_string)
            te_id=str(result[0])
            # te_name=result[1]
            bed_chr=line.split('\t')[0]
            te_alias0=str(type_string.split('=')[3])
            te_alias=te_alias0[:-1]
            te_strain=str(line.split('\t')[5])
            te_start_bed=int(line.split('\t')[1])
            te_end_bed=int(line.split('\t')[2])
            if((te_start_bed-len_error_txt2)<=te_start_txt2 and (te_end_bed+len_error_txt2)>=te_end_txt2 and txt_chr==bed_chr):
                print("get the insert te:"+str(number))
                out_insert_te_txt.write(str(number)+'\t'+te_id+'\t'+te_alias+'\t'+te_strain+'\t'+line2)
                break
            else:
                continue                
        input_bed.close()
    input_insert_te.close()
    # if(os.path.exists(te_insert_txt)==True): 
    #     os.remove(te_insert_txt)
    # if(os.path.exists(insert_te_txt)==True): 
    #     os.remove(insert_te_txt)

    return new_path,te_insert_infor,insert_te_infor




def filterSameTeAndInsert(new_path,name,txtinfor,tag):
    in_txtinfor=open(txtinfor,'r')
    txtfile=new_path+'/'+name+'-'+tag+'-filter-same.txt'
    # txtfile2=new_path+'/'+name+'-'+tag+'-filter-same-tag.txt'
    # txtfile3=new_path+'/'+name+'-'+tag+'-filter-same-tags.txt'
    te_number=0
    insert_start=0
    inser_end=0
    out_txt=open(txtfile,'w')
    # out_txt2=open(txtfile2,'w')
    line_number=0
    for line in in_txtinfor:
        segement_name=line.split('\t')[5]
        line_number=line_number+1
        if(line_number==1):
            continue

        if(te_number==int(line.split('\t')[0]) or line_number==2):
            insert_chr_0=line.split('\t')[10]
            insert_start_0=int(line.split('\t')[11])
            inser_end_xx_0=str(line.split('\t')[12])
            inser_end_0=int(inser_end_xx_0.split('\n')[0])

            if(abs(insert_start_0-insert_start)<=50 and abs(inser_end_0-inser_end)<=50 and insert_chr_0==insert_chr):
                # out_txt2.write(line.split('\t')[0]+'\t'+segement_name+'\t'+insert_chr_0+'\t'+str(insert_start_0)+'\t'+str(inser_end_0)+'\n')
                print('this segement is repeated')
            else:
                out_txt.write(line)


        else:
            out_txt.write(line)
        insert_chr=line.split('\t')[10]
        te_number=int(line.split('\t')[0])
        insert_start=int(line.split('\t')[11])
        inser_end_xx=str(line.split('\t')[12])
        inser_end=int(inser_end_xx.split('\n')[0])
    # if(os.path.exists(txtinfor)==True): 
    #     os.remove(txtinfor)
    # out_txt2.close()
    # out_txt2=open(txtfile2,'r')
    # out_txt3=open(txtfile3,'w')
    # te_number=0
    # sege_name=''
    # insert_start=0
    # insert_end=0
    # insert_chr=''
    # for line2 in out_txt2:
    #     te_number0=int(line2.split('\t')[0])
    #     sege_name0=line2.split('\t')[1]
    #     insert_chr_0=line2.split('\t')[2]
    #     insert_start_0=int(line2.split('\t')[3])
    #     insert_end_xx_0=str(line2.split('\t')[4])
    #     insert_end_0=int(insert_end_xx_0.split('\n')[0])

    #     if(abs(insert_start_0-insert_start)<=50 and abs(insert_end_0-insert_end)<=50 and insert_chr_0==insert_chr and te_number0==te_number and sege_name0==sege_name):
    #         continue
    #     else:
    #         out_txt3.write(line2)

    # os.remove(txtfile2)

    # out_txt3.close()

    # return txtfile,txtfile3
    return txtfile

    
def sortBy1p(new_path,te_insert_infor):
    test=str(te_insert_infor)
    file_name=new_path+'/'+name+'xxxx.txt'
    os.system("sed -i '1d' "+te_insert_infor)
    os.system("sort -t '\t' -k 1n,1 "+te_insert_infor+" > "+file_name)
    if(os.path.exists(te_insert_infor)==True): 
        os.remove(te_insert_infor)
    os.system('mv '+file_name+" "+test)
    os.system("sed -i '1 i Te_number\tTe_ID&name\tTe_alias\tTe_strain\treads_name\tChr_name\tTe_start\tTe_end\tmethylation_level\ttotal_C_sites\tinsert_start\t insert_end' "+te_insert_infor)


def countNewTeByFamily(txtfile,new_path,name,infor):

    # txtfile1=new_path+'/'+name+'-'+infor+'-countNewTeByTeNum.txt'    
    txtfile2=new_path+'/'+name+'-'+infor+'-countNewTeByFamily.txt'
    # outfile1=open(txtfile1,'w')
    outfile2=open(txtfile2,'w')
    # delte 1p 
    os.system("sed -i '1d' "+txtfile)
    
    infile=open(txtfile,'r')

    # te_re_number_list=[]
    # count_te_re_number_list=[]
    # methylation_level_list=[]
    # total_C_list=[]
    # te_len_list=[]
    

    te_family_list=[]
    count_te_family_list=[]
    methylation_level_list2=[]
    total_C_list2=[]
    te_len_list2=[]
    
    for line in infile:
        number=0
        number1=0
        number3=0
        number2=0
        # te_reference_number=line.split('\t')[0]
        te_family=line.split('\t')[2]
        te_start=line.split('\t')[6]
        te_end=line.split('\t')[7]
        te_len=int(te_end)-int(te_start)
        methylation_level=line.split('\t')[8]
        total_C=line.split('\t')[9]

        # if te_reference_number not in te_re_number_list:
        #     te_re_number_list.append(te_reference_number)
        #     count_te_re_number_list.append(1)
        #     methylation_level_list.append(methylation_level)
        #     total_C_list.append(total_C)
        #     te_len_list.append(te_len)
        # else:
        #     location=te_re_number_list.index(te_reference_number)
        #     number=int(count_te_re_number_list[location])
        #     number=number+1
        #     count_te_re_number_list[location]=number 
            
        #     number=int(methylation_level_list[location])
        #     number=number+int(methylation_level)
        #     methylation_level_list[location]=number             

        #     number=int(total_C_list[location])
        #     number=number+int(total_C)
        #     total_C_list[location]=number    

        #     number=int(te_len_list[location])
        #     number=number+int(te_len)
        #     te_len_list[location]=number    

        if te_family not in te_family_list:
            te_family_list.append(te_family)
            count_te_family_list.append(1)
            methylation_level_list2.append(methylation_level)
            total_C_list2.append(total_C)
            te_len_list2.append(te_len)
        else:
            location=te_family_list.index(te_family)
            number=int(count_te_family_list[location])
            number=number+1
            count_te_family_list[location]=number 
            
            number1=int(methylation_level_list2[location])
            number1=number1+int(methylation_level)
            methylation_level_list2[location]=number1             

            number2=int(total_C_list2[location])
            number2=number2+int(total_C)
            total_C_list2[location]=number2   

            number3=int(te_len_list2[location])
            number3=number3+int(te_len)
            te_len_list2[location]=number3  


    # outfile1.write('te_re_number\tnumber\tmethylation_level\ttotal_C\tmethylation_rate\tte_len\ttotal_rate\n')
    # for a,b,c,d,e in zip(te_re_number_list,count_te_re_number_list,methylation_level_list,total_C_list,te_len_list):
    #     if(int(c)==0):
    #         outfile1.write(a+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\t'+str('0')+'\t'+str(e)+str('0')+'\n')
    #     else:
    #         outfile1.write(a+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\t'+str(int(c)/int(d))+'\t'+str(e)+'\t'+str(int(c)/int(e))+'\n')
    # outfile1.close()

    outfile2.write('te_family\tnumber\tmethylation_level\ttotal_C\tmethylation_rate\tte_len\ttotal_rate\n')
    for a,b,c,d,e in zip(te_family_list,count_te_family_list,methylation_level_list2,total_C_list2,te_len_list2):
        if(int(c)==0):
            outfile2.write(a+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\t'+str('0')+'\t'+str(e)+str('0')+'\n')
        else:
            outfile2.write(a+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\t'+str(int(c)/int(d))+'\t'+str(e)+'\t'+str(int(c)/int(e))+'\n')
    outfile2.close()

    return txtfile2



def mapTeHeadAndTail(new_path,name,te_insert_txtfile,insert_te_txtfile):

    infile_te_insert=open(te_insert_txtfile,'r')
    infile_insert_te=open(insert_te_txtfile,'r')

    out_te_insert_txtfile=new_path+'/'+name+'-TE-insert-map-headTail.txt'
    out_insert_te_txtfile=new_path+'/'+name+'-insert-te-map-headTail.txt'

    out1=open(out_te_insert_txtfile,'w')
    out2=open(out_insert_te_txtfile,'w')
    reads_num=-1
    for line in infile_te_insert:
        xx=0
        if(reads_num==-1):
            reads_num=reads_num+1
            continue
        reads_num=reads_num+1

        te_insert_re_number=line.split('\t')[0]
        te_insert_insert_chr=line.split('\t')[10]

        te_insert_insert_start=int(line.split('\t')[11])
        te_insert_insert_end=int(line.split('\t')[12])
        
        infile_insert_te=open(insert_te_txtfile,'r')

        for line2 in infile_insert_te:
            insert_te_re_number=line2.split('\t')[0]
            insert_te_insert_chr=line2.split('\t')[10]

            insert_te_insert_start=int(line2.split('\t')[11])
            insert_te_insert_end=int(line2.split('\t')[12])    
            

            if(te_insert_re_number==insert_te_re_number):
                xx=1
                if(te_insert_insert_chr==insert_te_insert_chr):
                    if(abs(te_insert_insert_end-insert_te_insert_end)<100 or abs(te_insert_insert_start-insert_te_insert_start)<100):
                        out1.write(line)
                        out2.write(line2)
                        break
            if(te_insert_re_number!=insert_te_re_number and xx==1):
                break

    # if(os.path.exists(te_insert_txtfile)==True):
    #     os.remove(te_insert_txtfile)
    # if(os.path.exists(te_insert_txtfile)==True):
    #     os.remove(te_insert_txtfile)

    return out_te_insert_txtfile,out_insert_te_txtfile


def countNewTeBySuperFamliy(new_path,name,te_insert_by_family_txtfile,tags):
    outfile=new_path+'/'+name+'-'+tags+'-NewTeByFamilyinfor.txt'
    outfile2=new_path+'/'+name+'-'+tags+'-count-NewTeByFamilyinfor.txt'
    out=open(outfile,'w')
    infile=open(te_insert_by_family_txtfile,'r')
  
    for line in infile:
        family_name=line.split('\t')[0]
        super_infor=open('/home/xiaqini/extend_disk/arabidopsis/scripts/te_superfamily.txt','r')

        for line2 in super_infor:
            super_name=line2.split('\t')[1].split('\n')[0]

            if(line2.split('\t')[0]==family_name):
                out.write(super_name+'\t'+line.split('\t')[1]+'\t'+line.split('\t')[2]+'\t'+line.split('\t')[3]+'\t'+line.split('\t')[5]+'\n')
                break
            else:
                continue
    out.close()
    out=open(outfile,'r')
    super_fam_list=[]
    for linex in out:
        super=linex.split('\t')[0]
        if super not in super_fam_list:
            super_fam_list.append(super)
    out.close()

    out2=open(outfile2,'w')
    for i in super_fam_list:
        out1 =open(outfile,'r')
        sum_num=0
        sum_me_C=0
        sum_C=0
        sun_total=0

        for lines in out1:
        
            if(lines in ['\n','\r\n']):
                continue

            sufa_name=lines.split('\t')[0]
            if(sufa_name==i):
                sum_num+=int(lines.split('\t')[1])
                sum_me_C+=int(lines.split('\t')[2])
                sum_C+=int(lines.split('\t')[3])
                sun_total+=int(lines.split('\t')[4])
            else:
                continue
        if(sun_total!=0):
            if(sum_me_C!=0):
                me_C_coverage=str(Decimal(str(sum_me_C/sum_C)).quantize(Decimal("0.001"), rounding = "ROUND_HALF_UP"))
                me_total_coveage=str(Decimal(str(sum_me_C/sun_total)).quantize(Decimal("0.001"), rounding = "ROUND_HALF_UP"))
            if(sum_me_C==0):
                me_C_coverage='0.00'
                me_total_coveage='0.00'
            out2.write(i+'\t'+str(sum_num)+'\t'+str(sum_me_C)+'\t'+str(sum_C)+'\t'+me_C_coverage+'\t'+str(sun_total)+'\t'+me_total_coveage+'\n')
        # cat  
        # \| awk '{if($1=="ATREP") {sum1+=$2;sum2+=$3}} END {print "ATREP",sum1,sum2}'
        # print(i)
        # os.system("cat "+outfile+" | awk '{if($1== "+'$i'+") {sum2+=$2;sum3+=$3;sum4+=$4}} END {print "+"$1,sum2,sum3,sum4}' >> "+outfile2)
        # os.system("cat "+outfile+ " |awk '{if($1=='"+super+"') {sum+=$1}}'")
    os.remove(outfile)

    return outfile2


def stasticALL(new_path,name,only_te_insert_by_family_txtfile,only_insert_te_by_family_txtfile,both_te_insert_by_family_txtfile,both_insert_te_by_family_txtfile):


    both_te_insert=open(both_te_insert_by_family_txtfile,'r')
    

    stastic_txtfile=new_path+'/'+name+'-'+'-stastic-insert-test1.txt'
    both_insert_te=open(both_insert_te_by_family_txtfile,'r')
    # os.system("cp ")
    out_txt=open(stastic_txtfile,'w')
    # out_txt.write('super_family\tnumber\tmethylation_level\ttotal_C\tmethylation_rate\tte_len\ttotal_rate\n')
    # out_txt.close()
    for line1 in both_te_insert:
        # flag=0
        # out_txt=open(stastic_txtfile,'a+')
    
        # only_te_insert=open(only_te_insert_by_family_txtfile,'r')
        # only_insert_te=open(only_insert_te_by_family_txtfile,'r')

        famliy1=line1.split('\t')[0]
        number=int(line1.split('\t')[1])
        mel_C1=int(line1.split('\t')[2])
        total_C1=int(line1.split('\t')[3])
        total_len1=int(line1.split('\t')[5])

        for line2 in both_insert_te:
            famliy2=line2.split('\t')[0]

            mel_C2=int(line2.split('\t')[2])
            total_C2=int(line2.split('\t')[3])
            total_len2=int(line2.split('\t')[5])
            if(famliy1==famliy2):
                out_txt.write(famliy1+'\t'+str(number)+'\t'+str(mel_C1+mel_C2)+'\t'+str(total_C1+total_C2)+'\t0\t'+str(total_len1+total_len2)+'\t0\n')
                break
            # if(famliy1==famliy2):
            #     for line3 in only_te_insert:
            #         famliy3=line3.split('\t')[0]
            #         number3=int(line3.split('\t')[1])
            #         mel_C3=int(line3.split('\t')[2])
            #         total_C3=int(line3.split('\t')[3])
            #         total_len3=int(line3.split('\t')[5])

            #         if(famliy3==famliy2):
            #             for line4 in only_insert_te:
            #                 famliy4=line4.split('\t')[0]
            #                 number4=int(line4.split('\t')[1])
            #                 mel_C4=int(line4.split('\t')[2])
            #                 total_C4=int(line4.split('\t')[3])
            #                 total_len4=int(line4.split('\t')[5])

            #                 if(famliy3==famliy4):
            #                     flag=1
            #                     me_C_coverage=str(Decimal(str((mel_C1+mel_C2+mel_C3+mel_C4)/(total_C1+total_C2+total_C3+total_C4))).quantize(Decimal("0.001"), rounding = "ROUND_HALF_UP"))
            #                     me_total_coveage=str(Decimal(str((mel_C1+mel_C2+mel_C3+mel_C4)/(total_len1+total_len2+total_len3+total_len4))).quantize(Decimal("0.001"), rounding = "ROUND_HALF_UP"))
            #                     out_txt.write(famliy1+'\t'+str(number+number3+number4)+'\t'+str(mel_C1+mel_C2+mel_C3+mel_C4)+'\t'+str(total_C1+total_C2+total_C3+total_C4)+'\t'+me_C_coverage+'\t'+str(total_len1+total_len2+total_len3+total_len4)+'\t'+me_total_coveage+'\n')
            #                     break
            #                 else:
                    
            #                     continue
            #         if(flag==1):
            #             break
            #         else:
            #             continue
                # out_txt.write(famliy1+'\t'+number+'\t'+str(mel_C1+mel_C2)+'\t'+str(total_C1+total_C2)+'\t'+str(total_len1+total_len2)+'\n')
            # if(flag==1):
            #     break
                            
            else:
                continue
    os.system("cat "+only_te_insert_by_family_txtfile+" >> "+stastic_txtfile)    
    os.system("cat "+only_insert_te_by_family_txtfile+" >> "+stastic_txtfile)   

    new1_stastic_txtfile=new_path+'/'+name+'-'+'new1-stastic-insert-te.txt'
    new2_stastic_txtfile=new_path+'/'+name+'-'+'new2-stastic-insert-te.txt'
    new3_stastic_txtfile=new_path+'/'+name+'-'+'new3-stastic-insert-te.txt'
    new4_stastic_txtfile=new_path+'/'+name+'-'+'new4-stastic-insert-te.txt'
    out_stastic_txtfile=new_path+'/'+name+'-'+'xx-stastic-insert-te.txt'
    output_stastic_txtfile=new_path+'/'+name+'-'+'stastic-insert-te.txt'
    os.system("cat "+stastic_txtfile+"  | awk '{sum1[$1]+=$2}END{for(i in sum1)print i,sum1[i]}' > "+new1_stastic_txtfile)
    os.system("cat "+stastic_txtfile+"  | awk '{sum2[$1]+=$3}END{for(j in sum2) print sum2[j]}' >"+new2_stastic_txtfile)
    os.system("cat "+stastic_txtfile+"  | awk '{sum3[$1]+=$4}END{for(k in sum3)print sum3[k]}' > "+new3_stastic_txtfile)
    os.system("cat "+stastic_txtfile+"  | awk '{sum4[$1]+=$6}END{for(m in sum4)print sum4[m]}' > "+new4_stastic_txtfile)
    os.system("paste "+new1_stastic_txtfile+" "+new2_stastic_txtfile+" "+new3_stastic_txtfile+" "+new4_stastic_txtfile+">"+out_stastic_txtfile)
    os.remove(stastic_txtfile)
    os.remove(new1_stastic_txtfile)
    os.remove(new2_stastic_txtfile)
    os.remove(new3_stastic_txtfile)
    os.remove(new4_stastic_txtfile)

    os.system("sort -r -k 2 -n "+out_stastic_txtfile+" -o "+out_stastic_txtfile)

    os.system("cat "+ out_stastic_txtfile+"| awk '{sum=$3/$4}{sum2=$3/$5} {print $0,sum,sum2}' >"+output_stastic_txtfile)
    os.remove(out_stastic_txtfile)
    print("the total insert te is:")
    os.system("cat  "+output_stastic_txtfile+" |awk '{a+=$2}END{print a}'")
    os.system("sed -i '1isuper_family\tnumber\ttotal_me_C\ttotal_C\tte_len\tmethylation_rate\ttotal_rate\n' "+output_stastic_txtfile)


def countBysuFamliy(all_input,count_by_sufamliy_txt):
    outfile=open(count_by_sufamliy_txt,'w')
    os.system("sort -k 3 "+all_input+" -o "+all_input)
    input_file=open(all_input,'r')
    super_famliy_list=[]
 
    count_list=[]
    mel_C_list=[]
    total_C_list=[]
    len_list=[]
    
    for line in input_file:
        infor_file=open('/home/xiaqini/extend_disk/arabidopsis/scripts/te_superfamily.txt','r')
        famliy_name=line.split('\t')[2]
        mel_C=int(line.split('\t')[8])
        total_C=int(line.split('\t')[9])
        len=int(line.split('\t')[7])-int(line.split('\t')[6])

        for lines in infor_file:
            infor_fa_name=lines.split('\t')[0]
            infor_super_famliy=lines.split('\t')[1].split('\n')[0]

            if(infor_fa_name==famliy_name):
                super_famliy=infor_super_famliy
                break
            else:
                continue

        if super_famliy not in super_famliy_list:
            super_famliy_list.append(super_famliy)

            count_list.append(1)
            mel_C_list.append(mel_C)
            total_C_list.append(total_C)
            len_list.append(len)
        else:
            location=super_famliy_list.index(super_famliy)
            count_list[location]+=1
            mel_C_list[location]+=mel_C
            total_C_list[location]+=total_C
            len_list[location]+=len

    outfile.write('te_family\tnumber\tmethylation_level\ttotal_C\tte_len\n')
    for a,b,c,d,e in zip(super_famliy_list,count_list,mel_C_list,total_C_list,len_list):

        outfile.write(a+'\t'+str(b)+'\t'+str(c)+'\t'+str(d)+'\t'+str(e)+'\n')
    outfile.close()
    print("total copy te by super famliy:")
    os.system("cat "+out_file+" | awk '{print $2}' | awk '{sum+=$1}END{print sum}'")
if __name__=='__main__':
   
# /home/ubuntu/miniconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/insert_TE_analysis.py 

    # test data
    #  /home/ubuntu/miniconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/insert_TE_analysis.py /home/xiaqini/extend_disk/arabidopsis/data/C2T/test-more/map_split 1662

    # # #########################################################
    path=sys.argv[1]
    name=sys.argv[2]


    # step 1 get TE infor:TE number in reference and TE_type and TE location(+/-)
    new_path=path+'/'+'insert_TE'
    te_insert_infor=new_path+'/'+name+'-TE-insert-infor.txt'
    insert_te_infor=new_path+'/'+name+'-insert-TE-infor.txt'
    # new_path+'/'+name+'-TE-insert-infor.txt'
    if(os.path.exists(te_insert_infor)==False or os.path.exists(insert_te_infor)==False):
        new_path,te_insert_infor,insert_te_infor=getTEInfor(path,name)
    
        sz1 = os.path.getsize(te_insert_infor)
        sz2 = os.path.getsize(insert_te_infor)
        if not sz1 or sz2:
            new_path,te_insert_infor,insert_te_infor=getTEInfor(path,name)


    # # test data:
    # # new_path='/home/xiaqini/extend_disk/arabidopsis/data/C2T/split-hisat-pipeline-test/map_split/insert_TE'
    # # te_insert_infor='/home/xiaqini/extend_disk/arabidopsis/data/C2T/split-hisat-pipeline-test/map_split/insert_TE/1662-insert-TE-infor.txt'
    # step 2.1 sort by 1p
    sortBy1p(new_path,te_insert_infor)
    sortBy1p(new_path,insert_te_infor)
    # step2 filter this which has the same TE and insert location
    # te_insert_txtfile,te_insert_txt_tags=filterSameTeAndInsert(new_path,name,te_insert_infor,'te_insert')
    # insert_te_txtfile,insert_te_txt_tags=filterSameTeAndInsert(new_path,name,insert_te_infor,'insert_te')

    te_insert_txtfile=filterSameTeAndInsert(new_path,name,te_insert_infor,'te_insert')
    insert_te_txtfile=filterSameTeAndInsert(new_path,name,insert_te_infor,'insert_te')

    if(os.path.exists(te_insert_infor)==True):
        os.remove(te_insert_infor)
    if(os.path.exists(insert_te_infor)==True):
        os.remove(insert_te_infor)


    # # step2.1 filter this same segements
    filter_te_insert_txtfile=new_path+'/'+name+'-te-insert'+'-filter-same-reads.txt'
    # os.system(" cat "+te_insert_txtfile+" | awk '!a[$5]++{print}' > "+filter_te_insert_txtfile)
    # os.remove(te_insert_txtfile)

    filter_insert_te_txtfile=new_path+'/'+name+'-insert-te'+'-filter-same-reads.txt'
    # os.system(" cat "+insert_te_txtfile+" | awk '!a[$5]++{print}' > "+filter_insert_te_txtfile)
    # os.remove(insert_te_txtfile)

    # # step 3.1 map the te_head and te_tail
    out_te_insert_txtfile,out_insert_te_txtfile=mapTeHeadAndTail(new_path,name,filter_te_insert_txtfile,filter_insert_te_txtfile)



    # step3.2 get the subtraction 
    # step2.1_out_txt-(1662-insert-te-map-headTail)
    only_TailorHead_te_insert_txtfile=new_path+'/'+name+'-only_TailorHead_te_insert.txt'
    os.system("grep -F -v -f  "+out_te_insert_txtfile+" "+filter_te_insert_txtfile+" > "+ only_TailorHead_te_insert_txtfile)
    
    only_TailorHead_insert_te_txtfile=new_path+'/'+name+'-only_TailorHead_insert_te.txt'
    os.system("grep -F -v -f  "+out_insert_te_txtfile+" "+filter_insert_te_txtfile+" > "+ only_TailorHead_insert_te_txtfile)

    # # step3  stastic different family te number
    # only_te_insert_by_family_txtfile=countNewTeByFamily(only_TailorHead_te_insert_txtfile,new_path,name,'te_insert_only_tail_head')    
    # only_insert_te_by_family_txtfile=countNewTeByFamily(only_TailorHead_te_insert_txtfile,new_path,name,'insert_te_only_tail_head')

    # both_te_insert_by_family_txtfile=countNewTeByFamily(out_te_insert_txtfile,new_path,name,'te_insert_both_tail_head')    
    # both_insert_te_by_family_txtfile=countNewTeByFamily(out_insert_te_txtfile,new_path,name,'insert_te_both_tail_head')

    # # step3  stastic different super_family te number
    # only_te_insert_by_family_txtfile_infor=countNewTeBySuperFamliy(new_path,name,only_te_insert_by_family_txtfile,'te_insert_only_tail_head')
    # only_insert_te_by_family_txtfile_infor=countNewTeBySuperFamliy(new_path,name,only_insert_te_by_family_txtfile,'insert_te_only_tail_head')
    # both_te_insert_by_family_txtfile_infor=countNewTeBySuperFamliy(new_path,name,both_te_insert_by_family_txtfile,'te_insert_both_tail_head')
    # both_insert_te_by_family_txtfile_infor=countNewTeBySuperFamliy(new_path,name,both_insert_te_by_family_txtfile,'insert_te_both_tail_head')

    # if(os.path.exists(only_te_insert_by_family_txtfile)==True):
    #     os.remove(only_te_insert_by_family_txtfile)

    # if(os.path.exists(only_insert_te_by_family_txtfile)==True):
    #     os.remove(only_insert_te_by_family_txtfile)
    # if(os.path.exists(both_te_insert_by_family_txtfile)==True):
    #     os.remove(both_te_insert_by_family_txtfile)
    # if(os.path.exists(both_insert_te_by_family_txtfile)==True):
    #     os.remove(both_insert_te_by_family_txtfile)
 
    all_input=new_path+'/'+name+'-all-map-headTail.txt'
    out_file=new_path+'/'+name+'-copy-count-infor.txt'

    #  step 1 cat
    os.system("cat "+out_insert_te_txtfile+" "+only_TailorHead_te_insert_txtfile+" "+only_TailorHead_insert_te_txtfile+" > " +all_input)
    os.system("sort -n -k 1 "+all_input+" -o "+all_input)

    count_by_sufamliy_txt=new_path+'/'+name+'-stastic-insert-te.txt'
    count_copy(all_input,out_file)
    countBysuFamliy(all_input,count_by_sufamliy_txt)
    


    # step 4 stastic all
    # stasticALL(new_path,name,only_te_insert_by_family_txtfile_infor,only_insert_te_by_family_txtfile_infor,both_te_insert_by_family_txtfile_infor,both_insert_te_by_family_txtfile_infor)