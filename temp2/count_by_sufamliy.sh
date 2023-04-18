path=$1
name=$2

cd $path/active

input_file=$name-all-infor.txt


# AT2TE61100 LTR/Gypsy 0 394 0 10 0 27 0 34 0 71 ATHILA6A 26 0.870 4
# CHG+CHH+CpG+total
# ID\tsuperFamliy\ttransTimecoverage\tTE_len\tCHG\CHG_total\tCHH\tCHH_total\tCpG\CpG_total\ttall\ttotal_total\tfamliy\tg4Count\tg4abundece\tg4_bp


# deal input_file
all_meth_file=$name-all-meth-infor.txt
if [ -s "$input_file" ];then
    # if sufamliy transtimes te_length CHG CHH CpG total famliy g4_count g4_abundance g4_bp
    awk '{if($12!=0) print $1,$2,$3,$4,($6!=0?$5/$6:0),($8!=0?$7/$8:0),($10!=0?$9/$10:0),($12!=0?$11/$12:0),$13,$14,$15,$16}' $input_file | tr ' ' '\t' > $all_meth_file
else
    echo "all-infor file not exists"
fi


# 按g4富集程度分类
if [ -s "$all_meth_file" ];then
    files=("g4-0-1.txt" "g4-1-10.txt" "g4-10-100.txt" "g4-null.txt")

    awk '{bin=$11; if(bin>0 && bin<0.01) print $0 > "g4-0-1.txt"; else if(bin>=0.01 && bin<0.1) print $0 > "g4-1-10.txt"; else if(bin>=0.1 && bin<1) print $0 > "g4-10-100.txt"; else if(bin==0) print $0 > "g4-null.txt"}' $all_meth_file

    # awk '{if ($2 in arr) {arr[$2]++; val[$2]+=$3; a[$2]+=$5; b[$2]+=$6; c[$2]+=$7; d[$2]+=$8; e[$2]+=$9; f[$2]+=$10} else {arr[$2]=1; val[$2]=$3; a[$2]=$5; b[$2]=$6; c[$2]=$7; d[$2]=$8; e[$2]=$9; f[$2]=$10}} END {for (i in arr) {if (arr[i] == 0) {print i"\t0\t0\t0\t0"} else {print i"\t"val[i]/arr[i]"\t"a[i]+b[i]+c[i]+d[i]+e[i]+f[i]*5/6/(arr[i]?arr[i]:1)"\t"a[i]+b[i]+c[i]+d[i]+e[i]+f[i]*7/8/(arr[i]?arr[i]:1)"\t"a[i]+b[i]+c[i]+d[i]+e[i]+f[i]*9/10/(arr[i]?arr[i]:1)}}}' file.txt > result.txt

    # 循环处理文件
    for file in "${files[@]}"
    do
        if [ -s "$file" ];then
            strings=""${file%????}""
            output_file=$2-statistics-$strings.txt

            echo -e "sufamliy\tTEactive\ttotalmeth\tCpGmethCHHmeth\tCHGmeth\t" > $output_file
            # all
            awk '{id="All";sum+=$3; a+= $5; b+= $6; c+= $7; d+= $8; count++} END{printf "%s %.3f %.3f %.3f %.3f %.3f\n", id, sum/count,d/count,c/count,b/count,a/count }' $file | tr ' ' '\t' >>$output_file
            # by famliy
            awk '{sum[$2] += $3; a[$2] += $5; b[$2] += $6; c[$2] += $7; d[$2] += $8; count[$2]++} END {for (i in sum) {printf "%s %.3f %.3f %.3f %.3f %.3f\n", i, sum[i]/count[i],a[i]/count[i],b[i]/count[i],c[i]/count[i],d[i]/count[i] }}' $file | tr ' ' '\t'  >>$output_file
            rm $file
        fi
    done

else
    echo "all-meth-infor file not exists"
fi




# 按照甲基化程度分类

if [ -s "$all_meth_file" ];then
    # lower=$(awk '{print $8}' $all_meth_file | sort -nr | tail -n1)
    # lower=$(printf "%.3f" $lower)
    # higher=$(awk '{print $8}' $all_meth_file | sort -n | tail -n1)
    # echo "$lower"
    # echo "$higher"
    # grad_1=$(echo "scale=3; ($higher-$lower) / 4+$lower" | bc)
    # grad_1=$(printf "%.3f" $grad_1)

    # grad_2=$(echo "scale=3; ($higher-$lower)*2 / 4+$lower" | bc)
    # grad_2=$(printf "%.3f" $grad_2)

    # grad_3=$(echo "scale=3; ($higher-$lower)*3 / 4+$lower" | bc)
    # grad_3=$(printf "%.3f" $grad_3)


    # files=("meth-grade-1.txt" "meth-grade-2.txt" "meth-grade-3.txt" "meth-grade-4.txt")
    files=("meth-0-20.txt" "meth-20-80.txt" "meth-80-100.txt")

    # awk -v grad_1="$grad_1" -v grad_2="$grad_2" -v grad_3="$grad_3" '{bin=$11;ebin=$12; if(ebin>0 && bin/ebin<grad_1) print $0 > "meth-grade-1.txt"; else if(ebin>0 && bin/ebin>grad_1 &&  bin/ebin<grad_2) print $0 > "meth-grade-2.txt" ; else if(ebin>0 && bin/ebin>grad_2 &&  bin/ebin<grad_3) print $0 > "meth-grade-3.txt" ; else if(ebin>0 && bin/ebin>grad_3) print $0 > "meth-grade-4.txt" }' $all_meth_file
    awk '{bin=$8; if(bin>0 && bin<0.2) print $0 > "meth-0-20.txt"; else if (bin>0.2 &&  bin<0.8) print $0 > "meth-20-80.txt"; else if(bin>0.8 && bin<1) print $0 > "meth-80-100.txt"}' $all_meth_file
    # 循环处理文件
    for file in "${files[@]}"
    do
        if [ -s "$file" ];then
            strings=""${file%????}""
            output_file=$2-statistics-$strings.txt

            echo -e "sufamliy\tTEactive\ttotalmeth\tCpGmethCHHmeth\tCHGmeth\tG4gratitude" > $output_file
            # all
            awk '{id="All";sum+=$3; a+= $5; b+= $6; c+= $7; d+= $8;e+=$11; count++} END{printf "%s %.3f %.3f %.3f %.3f %.3f %.3f\n", id, sum/count,d/count,c/count,b/count,a/count,e/count }' $file | tr ' ' '\t' >>$output_file
            # awk '{id="All";sum+=$3; a+= $5; b+= $6; c+= $7; d+= $8; e+= $9; f+= $10;g+=$11;h+=$12;j+=$16;k+=$4; count++} END{printf "%s %.3f %.3f %.3f %.3f %.3f %.3f\n", id, sum/count, (b!=0?a/b:0), (d!=0?c/d:0), (f!=0?e/f:0), (h!=0?g/h:0),(k!=0?j/k:0)}' $file | tr ' ' '\t' >>$output_file
            # by famliy
            # awk '{sum[$2] += $3; a[$2] += $5; b[$2] += $6; c[$2] += $7; d[$2] += $8; e[$2] += $9; f[$2] += $10;g[$2]+=$11;h[$2]+=$12;j[$2]+=$16;k[$2]+=$4; count[$2]++} END {for (i in sum) {printf "%s %.3f %.3f %.3f %.3f %.3f %.3f\n", i, sum[i]/count[i], (b[i]!=0?a[i]/b[i]:0), (d[i]!=0?c[i]/d[i]:0), (f[i]!=0?e[i]/f[i]:0), (h[i]!=0?g[i]/h[i]:0),(k[i]!=0?j[i]/k[i]:0)}}' $file | tr ' ' '\t'  >>$output_file
            awk '{sum[$2] += $3; a[$2] += $5; b[$2] += $6; c[$2] += $7; d[$2] += $8;e[$2]+=$11; count[$2]++} END {for (i in sum) {printf "%s %.3f %.3f %.3f %.3f %.3f %.3f\n", i, sum[i]/count[i],a[i]/count[i],b[i]/count[i],c[i]/count[i],d[i]/count[i],e[i]/count[i] }}' $file | tr ' ' '\t'  >>$output_file
            rm $file
        fi
    done

else
    echo "all-meth-infor file not exists"
fi