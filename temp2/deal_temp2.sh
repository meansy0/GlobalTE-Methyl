path=$1
name=$2

cd $path
te_famliy=/home/ubuntu/data/Arabidopsis_sequence_2/arabidopsis/data/reference/te-famliy1.txt
cp_file1=$name-output/$name-1.all.fastq.gz.insertion.bed
insert_txt=te.insertion.all.txt
if [ -s "$cp_file1" ];then
    cp $path/$name-output/$name-1.all.fastq.gz.insertion.bed $path
    rm -r $path/$name-output
fi

orign_bed=$name-1.all.fastq.gz.insertion.bed
if [ -s "$orign_bed" ];then
    cache_txt=te.insertion.txt
    insert_bed=te.insertion.bed
    awk '{if($7 ~ /p/ && $1 ~/Chr/ && $7!="Type") print $0} ' $orign_bed > $insert_bed

    /home/ubuntu/miniconda3/bin/python /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/deal_insertionBed.py $path $name

    final_insert_bed=te.insertion.filter.bed
    cut -f 4 $final_insert_bed | cut -d ':' -f 1 | awk '{a[$1]++}END{for(i in a)print i,a[i]}' | tr ' ' '\t'|sort -k1,1 > $cache_txt

    join $cache_txt -v2 $te_famliy | awk '{print $0,0}'| tr ' ' '\t' > $insert_txt
    join $cache_txt  $te_famliy | awk '{print $1,$3,$2}'| tr ' ' '\t' >> $insert_txt
    sort -k1 $insert_txt -o $insert_txt
    echo "test"
    rm $cache_txt
fi

if [ -d "active" ];then
    echo "file folder exsits"
else
    mkdir active
fi


methAndg4=active/$name-meth-and-g4-infor.txt
alltxt=active/$name-all-infor.txt
if [ -s "$methAndg4" ];then
    echo "have get infor"
else
    have_file=g4-infor/$name-have-cache.txt
    nog4_file=g4-infor/$name-no-cache.txt
    if [ -s "$have_file" ];then
        sort -k1 $have_file -o $have_file
        cat $have_file > $methAndg4
        sort -k1 $nog4_file -o $nog4_file
        cat $nog4_file >> $methAndg4
        sort -k1,1 $methAndg4 -o $methAndg4

        join $insert_txt $methAndg4 | tr ' ' '\t' |cut -f 1-12,14,16,17,18 > $alltxt


        # string=$(echo -e "ID\tsuperFamliy\ttransTimecoverage\tTE_len\tCHG\CHG_total\tCHH\tCHH_total\tCpG\CpG_total\ttall\ttotal_total\tfamliy\tg4Count\tg4abundece\n")
        
        # sed -i "1i $string" $alltxt
        rm $methAndg4

    fi

fi


