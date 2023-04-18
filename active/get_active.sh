# echo " $1"
awk '{count[$2]+=$3} END {for (c in count) print c, count[c]}' $1 | sort -k2nr > $2