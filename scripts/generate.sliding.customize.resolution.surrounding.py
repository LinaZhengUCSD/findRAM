import sys
#chrlen is the chromosome length file
#chrid is ie. chr1
#res: resolution to move the step, for example, if we want to use 50kb as one step to move the window, then res=50000
#window: the window size up and down stream centered to the resolution bin, for example if you want flanking window 1Mbp, then window=1000000

def sliding(chrlen, chrid, res, window):
	chrdict={}
	f=open(chrlen, "r")
	for line in f:
		line=line.strip()
		line=line.split()
		chrdict[line[0]]=int(line[1])
	f.close()
	
	total=0
	if chrid in chrdict:
		total=chrdict.get(chrid)
	else:
		sys.exit("ERROR: check chromosome "+str(chrid))	
	
	totalbin=int(total/int(res))+1
	for i in range(totalbin):
		lowerbin=i*int(res)
		upperbin=(i+1)*int(res)
		lowerwindow=lowerbin-int(window)
		upperwindow=upperbin+int(window)
		if lowerwindow<0:
			lowerwindow=0
		if upperwindow>total:
			upperwindow=total
		ss=chrid+"\t"+str(lowerwindow)+"\t"+str(upperwindow)+"\t"+str(i)
		print(ss)
	

if __name__=="__main__":
	chrlen=sys.argv[1]
	chrid=sys.argv[2]
	res=sys.argv[3]
	window=sys.argv[4]
	sliding(chrlen, chrid, res, window)
