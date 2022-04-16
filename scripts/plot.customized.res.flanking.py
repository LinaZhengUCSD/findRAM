import sys
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot(infile, outdir, sample,res):
	density=[]
	binname=[]
	f=open(infile, "r")
	for line in f:
		line=line.strip()
		line=line.split()
		bname=int(line[3])
		value=int(line[-1])
		density.append(value)
		binname.append(bname)
	f.close()

	resvalue=int(res.split("k")[0])
	tickstep=int(5000/int(resvalue))
	plotfile=outdir+"/"+str(sample)+".plot.pdf"
	pos=np.arange(len(density))
	titlename=sample
	plt.figure(figsize=(50,10))
	plt.bar(pos, density)
	plt.xticks(np.arange(0, len(density), tickstep))
	plt.title(titlename,fontsize=50)
	plt.yticks(fontsize=30)
	plt.savefig(plotfile)

if __name__=="__main__":
	infile=sys.argv[1]
	outdir=sys.argv[2]
	sample=sys.argv[3]
	res=sys.argv[4]
	plot(infile, outdir, sample,res)
