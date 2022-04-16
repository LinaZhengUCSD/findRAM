#!/bin/bash

datadir=$1
wkdir=$2
codedir=$3

#parameters setting
span=$4
depth=$5
marginerror=$6
chromosize=$7
res=250kb
flanking=500kb

#save output
peakdir=$wkdir/peakcall/
peakplotdir=$wkdir/peakcall.plot/
RAMdir=$wkdir/RAM.results/

mkdir $peakdir
mkdir $peakplotdir
mkdir $RAMdir
mkdir $RAMdir/modules
mkdir $RAMdir/boundary

for i in $(seq 1 19) X;
do
	Rscript $codedir/peak.call.customized.res.flanking.r $datadir/chr`basename $i`.sliding.window.density.txt chr`basename $i` $span $res $flanking $peakdir/chr`basename $i`.sliding.window.peakcall.txt $peakplotdir/chr`basename $i`.sliding.window.module.plot.pdf $depth;
done;

for i in $(seq 1 19) X;
do
	python $codedir/get.module.py $peakdir/chr`basename $i`.sliding.window.peakcall.txt $chromosize chr`basename $i` $res $marginerror > $RAMdir/modules/chr`basename $i`.sliding.window.RAM.txt;
	python $codedir/get.boundaries.py $RAMdir/modules/chr`basename $i`.sliding.window.RAM.txt $chromosize $res > $RAMdir/boundary/chr`basename $i`.sliding.window.boundary.txt;
done;
 
cd $wkdir
tar -czf peakcall.plot.tar.gz ./peakcall.plot/
tar -czf peakcall.tar.gz ./peakcall/

rm -rf ./peakcall/ ./peakcall.plot/
