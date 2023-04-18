
# list
all_sh=/home/xiaqini/extend_disk/arabidopsis/scripts/temp2/All.sh

log=/home/xiaqini/extend_disk/arabidopsis/scripts/temp2/log.txt


folder_path=/home/xiaqini/extend_disk/arabidopsis/data6


number=$(($1))

i=0
for path in $folder_path/*
do
    cd $path
   
    name=$(basename $path)
 
    if [ -s "te.insertion.filter.bed" ];then 
        echo " skip:$name" 
    
    else
        if [ -s "${name}_1.all.fastq.gz" ];then
            mv ${name}_1.all.fastq.gz ${name}-1.all.fastq.gz
            mv ${name}_2.all.fastq.gz ${name}-2.all.fastq.gz
        fi
        if [ -s "${name}-2.all.fastq.gz" ];then
            if [ -s "${name}-all-inactive-sufamliy-meth.txt" ];then
                if [ $i -le $number ];then
                    echo "start:$name"
                    bash $all_sh $path $name > temp2.log 2>&1
                    i=$(($i+1))

                else
                    break
                fi   
            fi
        else
            echo " all fastq not exists:$name" >> $log    
        fi
    fi 

done


