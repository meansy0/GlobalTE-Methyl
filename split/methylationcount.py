
import os

def MethylationCount(path,name):

    bedname=path+'/'+name+'.check2.bed'
    txtname=path+'/'+name+'.mergepos.txt'
    out_txtname=path+'/'+name+'.methylationcount.txt'

    input_bed=open(bedname,'r')
    out_txt=open(out_txtname,'w')

    #give a row number for txtfile
    row_num=0
    
    #read bed file
    for line1 in input_bed:

        #read TE_ID
        TE_ID=str(line1.split('\t')[3])
        #read chr-number
        chr_num1=str(line1.split('\t')[0] )
        #calculate TE_length
        start=int(line1.split('\t')[1])
        end=int(line1.split('\t')[2])
        TE_len=str(end-start+1)

        #initialize
        CHG=0
        CHH=0
        CpG=0
        MC_count=0
        C_count=0
        total=0

        #input_txt=open(txtname,'r')
        # with open(txtname, 'rt') as filehandle:
        #     input_txt= filehandle.readlines()[row_num-1:]

        input_txt=open(txtname,'r')

        #read txtfile
        # for line in input_txt.readlines()[row_num-1:]:
        for line in input_txt:
            row_num=row_num+1
            #read chr-number
            chr_num2=str(line.split('\t')[2] )
            #raed type of c
            c_type=str(line.split('\t')[4].split('\n')[0])
            # print(c_type[0])
            #read methylation pos
            pos=int(line.split('\t')[3])
        
            if(chr_num1[3]==chr_num2 and start<=pos and pos<=end):
                
                # print('xx')
                if(c_type=='X'):
                    CHG=CHG+1
                    # print(CHG)
                if(c_type=='H'):
                    CHH=CHH+1
                    # print(CHH)
                if(c_type=='Z'):
                    CpG=CpG+1
                    # print(CpG)
                if(c_type=='z' or c_type=='x' or c_type=='h'):
                    C_count=C_count+1 
                    # print(C_count) 
                
                continue

            if(chr_num1[3]==chr_num2 and pos>end):
                input_txt.close()
                break
            else:
                
                continue   
            
            
        MC_count=CHG+CHH+CpG
        total=MC_count+C_count
        # print(TE_ID)
        
        if(total>0):
            print("success:"+TE_ID)
            out_txt.write(TE_ID+'\t'+TE_len+'\t'+str(CHG)+'\t'+str(CHH)+'\t'+str(CpG)+'\t'+str(MC_count)+'\t'+str(total)+'\n')
    
            
    input_bed.close()
    out_txt.close()

if __name__=='__main__':

    #test data
    path='/home/ubuntu/data/Arabidopsis_sequence_2/arabidopsis/data/915'
    name='915'
    MethylationCount(path,name)
