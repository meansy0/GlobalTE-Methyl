
folder_path=/home/xiaqini/extend_disk/arabidopsis/data3

for path in $folder_path/*
do
(
    cd $path
    name=$(basename $path)

    if [ -d "active" ];then
        rm -r active

        bash /home/xiaqini/extend_disk/arabidopsis/scripts/g4/All.sh $path $name

        bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/deal_temp2.sh $path $name

        bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/count_by_sufamliy.sh $path $name

        bash /home/xiaqini/extend_disk/arabidopsis/scripts/temp2/add.sh $path $name

    fi
) & wait
done


