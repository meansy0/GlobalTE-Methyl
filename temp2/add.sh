
path=$1
name=$2

cd $path/active
infor_file=$name-all-meth-infor.txt
if [ -s "$infor_file" ];then
    output_file=$name-statistics-all-g4.txt

    infor_cache_file=$name-all-cache-infor.txt
    echo -e "sufamliy\tTEactive\ttotalmeth\tCpGmethCHHmeth\tCHGmeth\t" > $output_file
    awk '{if($10>0) print $0}' $infor_file  | tr ' ' '\t' >$infor_cache_file
    awk '{id="All";sum+=$3; a+= $5; b+= $6; c+= $7; d+= $8; count++} END{printf "%s %.3f %.3f %.3f %.3f %.3f\n", id, sum/count,d/count,c/count,b/count,a/count }' $infor_cache_file | tr ' ' '\t' >>$output_file
    awk '{sum[$2] += $3; a[$2] += $5; b[$2] += $6; c[$2] += $7; d[$2] += $8; count[$2]++} END {for (i in sum) {printf "%s %.3f %.3f %.3f %.3f %.3f\n", i, sum[i]/count[i],a[i]/count[i],b[i]/count[i],c[i]/count[i],d[i]/count[i] }}' $infor_cache_file | tr ' ' '\t'  >>$output_file
    rm $infor_cache_file
else
    echo "$name not exists infor fiile,skip!"

fi