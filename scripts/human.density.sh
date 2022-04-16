#!/bin/bash

data=$1
wkdir=$2
slidingwindow=$3
codedir=$4

#make directories
mkdir $wkdir/density/
mkdir $wkdir/density.plot/
mkdir $wkdir/density.tmp/

densitydir=$wkdir/density/
overlapdir=$wkdir/density.tmp/
plotdir=$wkdir/density.plot/

for i in $(seq 1 22) X;
do
	bedtools intersect -a $slidingwindow/sliding.window.coordinates.chr`basename $i`.bed -b $data -wa -wb > $overlapdir/chr`basename $i`.sliding.window.overlap.bed;
	awk '{print $1 "\t" $2 "\t" $3 "\t" $4}' $overlapdir/chr`basename $i`.sliding.window.overlap.bed > $overlapdir/chr`basename $i`.sliding.window.overlap.tmp;
	sort -V $overlapdir/chr`basename $i`.sliding.window.overlap.tmp | uniq -c | awk '{print $2 "\t" $3 "\t" $4 "\t" $5 "\t" $1}' | sort -k 4 -n > $overlapdir/chr`basename $i`.sliding.window.density.tmp;
	python $codedir/remedy.empty.sliding.window.py $slidingwindow/sliding.window.coordinates.chr`basename $i`.bed $overlapdir/chr`basename $i`.sliding.window.density.tmp | sort -k 4 -n > $overlapdir/chr`basename $i`.sliding.window.density.txt;
	python $codedir/plot.customized.res.flanking.py $overlapdir/chr`basename $i`.sliding.window.density.txt $plotdir chr`basename $i`.sliding.window.density 250kb;
done;


cp $overlapdir/*.sliding.window.density.txt $densitydir/
cd $wkdir

tar -czf density.tmp.tar.gz ./density.tmp/
tar -czf density.plot.tar.gz ./density.plot/

rm -f density.tmp.tar.gz
rm -rf ./density.tmp/ ./density.plot/
