import os
import subprocess
import sys
if __name__=='__main__':

    path=sys.argv[1]
    name=sys.argv[2]

    insertionBed=path+'/te.insertion.bed'

    out_file=path+'/te.insertion.filter.bed'

    if(os.path.exists(insertionBed)):
        open_outfile=open(out_file,'w')
        open_insertionBed=open(insertionBed,'r')
        
        for line in open_insertionBed:
            id_list=[]
            # id_list0=[]
            super_list=[]
            id_list_old=[]
            line_list=line.split('\t')

            id_infor=line.split('\t')[3]
            id_list_old=id_infor.split(',')
            for i in id_list_old:
                id_list.append(i.split(':')[0])
            # id_list=[]
            # id_list=list(set(id_list0))

            if(len(id_list)==1):
                open_outfile.write(line)
            else:
                for j in id_list:
                    # output2 = subprocess.check_output('awk \'/'+j+'/\' /home/ubuntu/data/Arabidopsis_sequence_2/arabidopsis/data/reference/te-famliy.txt', shell=True)
                    output = subprocess.check_output(['awk', '/' + j + '/{print}', '/home/ubuntu/data/Arabidopsis_sequence_2/arabidopsis/data/reference/te-famliy.txt'])
                    if(len(output.decode())>0):                                    
                        family=output.decode().split('\t')[1]
                        super_family=output.decode().split('\t')[2].split('\n')[0]
                        super_list.append(super_family)
                
                        most_common_str = max(set(super_list), key=super_list.count)
                        most_common_index = super_list.index(most_common_str)

                        line_list[3]=id_list_old[most_common_index]
                        time =1
                        for m in line_list:
                            if(len(line_list)==time):
                                open_outfile.write(m)
                            else:
                                open_outfile.write(m+'\t')
                            time+=1

        open_insertionBed.close()
        open_outfile.close()

