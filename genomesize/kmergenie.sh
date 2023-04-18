# $folder:$1
# input father folder

# export PATH="/usr/local/bin:$PATH"

folder=$1

for path in $folder/*
do
(
    if [ -d "${path}" ]; then
        cd $path
        fastq_list=fastq-list.txt
        name=$(basename $path)
        q=0

        if [ -s "histograms_report.html" ];then
            echo "have done,skip:$name"

        else

            if [ -s "${name}-1.all.fastq.gz" ] && [ -s "${name}-2.all.fastq.gz" ];then
                q=1
                echo "${name}-1.all.fastq.gz" > $fastq_list
                echo "${name}-2.all.fastq.gz" >> $fastq_list
                chmod  777 $fastq_list
            fi

            if [ -s "${name}_1.all.fastq.gz" ] && [ -s "${name}_2.all.fastq.gz" ];then
                q=1
                echo "${name}_1.all.fastq.gz" > $fastq_list
                echo "${name}_2.all.fastq.gz" >> $fastq_list
                chmod  777 $fastq_list
            fi

            if [ $q -eq 1 ];then
                echo "start :$name"
                kmergenie=/home/xiaqini/extend_disk/arabidopsis/software/kmergenie-1.7051/kmergenie
                $kmergenie $fastq_list -l 17 -k 37 -s 10 -t 4 > sample.log1.txt > sample.log2.txt

                rm histograms-*.histo.pdf
                rm fastq-list.txt
                rm histograms-*.histo
                rm histograms.dat*
                rm sample.log*.txt

            
            else
                echo "$name-fastq file not exists!"
            fi
        fi    
    fi
) &
done
wait

