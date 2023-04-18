# need run the g4 code first
# $1:path
# $2:name

# need run in conda-temp2
bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/temp2.sh $1 $2

bash /home/xiaqini/extend_disk/arabidopsis/scripts/g4/All.sh $1 $2

bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/deal_temp2.sh $1 $2

bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/count_by_sufamliy.sh $1 $2

bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/add.sh $1 $2