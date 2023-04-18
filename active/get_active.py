import os


if __name__=='__main__':

    input_path='/home/xiaqini/newdata/data'
    lst = os.listdir(input_path)

    out_txt_file='/home/xiaqini/extend_disk/arabidopsis/scripts/statistics/active/get_famliy_active.txt'
    out_csv_file='/home/xiaqini/extend_disk/arabidopsis/scripts/statistics/active/get_famliy_active.csv'
    in_file=open(out_txt_file,'w')

    famliy_list=['RC/Helitron','DNA/MuDR','LTR/Gypsy','LTR/Copia','LINE/L1']

    in_file.write('sample\t')

    count=1
    for i in famliy_list:
        if(count<len(famliy_list)):
            in_file.write(i+'\t')
        else:
            in_file.write(i+'\n')
        count=count+1

    

    for group_number in lst:
        path=input_path+'/'+group_number+'/'


        all_active=path+'te.insertion.all.txt'
        cachetxt=path+'active-famliy-number.txt'
        if(os.path.exists(all_active)):
            
            os.system("bash /home/xiaqini/extend_disk/arabidopsis/scripts/statistics/active/get_active.sh "+all_active+" "+cachetxt)
            in_file.write(str(group_number)+'\t')
            for i in famliy_list:
                open_file=open(cachetxt, 'r')
                for line in open_file:
                    file_famliy=line.split(' ')[0]
                    number=line.split(' ')[1].split('\n')[0]
                    if(i==file_famliy):
                        in_file.write(number+'\t')
                        break
                    else:
                        continue
            in_file.write('\n')
            
        
        else:
            continue


in_file.close()
os.system("cat "+out_txt_file+" | tr -s '[:blank:]' ',' > "+out_csv_file)

os.remove(out_txt_file)
