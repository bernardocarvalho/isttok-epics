#!/bin/bash

# RENAME DATA FILES AND CREATE .CFG FILE
shopt -s extglob
dirA="$1"
dirB="/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/data"

echo $dirA

cd $dirA
echo "Preparing..."
rm !(*.bin)
echo "Executing... please wait..."
for file in *
do
    if [ -f "$file" ]; then
        newfile=${file:0:11}".bin"
        tfile=${file:0:8}".bin"
        if [ "$tfile" = "timeBase.bin" ]; then
            date=${file:9:10}
	        mkdir -p $dirB/$date
			time1=${file:21:1}
		    if [ "$time1" = "_" ]; then
				time1="0"${file:20:1}
				time2=${file:23:1}
 				if [ "$time2" = "_" ]; then
					time2="0"${file:22:1}
				fi
			else
				time1=${file:20:2}
				time2=${file:24:1}
				if [ "$time2" = "_" ]; then
					time2="0"${file:23:1}
				else
					time2=${file:23:2}
				fi
			fi
			time=$time1"_"$time2
	        mkdir -p $dirB/$date/$time
            mv -f $file $dirB/$date/$time/$tfile
        else
            date=${file:12:10}
	        mkdir -p $dirB/$date

			time1=${file:24:1}
		    if [ "$time1" = "_" ]; then
				time1="0"${file:23:1}
				time2=${file:26:1}
				if [ "$time2" = "_" ]; then
					time2="0"${file:25:1}
				fi
			else
				time1=${file:23:2}
				time2=${file:27:1}
				if [ "$time2" = "_" ]; then
					time2="0"${file:26:1}
				else
					time2=${file:26:2}
				fi
			fi

	        time=$time1"_"$time2
	        mkdir -p $dirB/$date/$time

            mv -f $file $dirB/$date/$time/$newfile
        fi
        cp -f /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/cfg-files/template.cfg $dirB/$date/$time
        sed -i 's/newdate/'$date'/g' $dirB/$date/$time/template.cfg
        sed -i 's/newtime/'$time'/g' $dirB/$date/$time/template.cfg
        mv -f $dirB/$date/$time/template.cfg /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/cfg-files/$date.$time.cfg
    fi
done
echo "Cleaning..."
rm -rf $dirA

echo "Sending files..."
sshpass -p "ipfnist0" scp -r /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/data/$date pricardofc@192.168.1.172:/home/pricardofc/CSS-Workspaces/sys-mng-opi/CSS/data
sshpass -p "ipfnist0" scp -r /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/cfg-files/$date* pricardofc@192.168.1.172:/home/pricardofc/CSS-Workspaces/sys-mng-opi/CSS/cfg-files
echo "Done!"
