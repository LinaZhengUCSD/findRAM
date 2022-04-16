import sys
#infile: the summit, start,end from R output directly. The index in this file is start from 1-base. So the 1 means the first bin of the chromosome, chr:0-resolution
#chrlen: chromosome length
#chromo:chr
#res: the resolution binsize, eg: 50000, but resolution as input should be in 50kb
#marginerror: boundary margin of error (specified in number of BINS), added to each side of the boundary, eg: 0,1,2,or 3
def getdomain(infile, chrlen, chromo, resolution, marginerror):
	res=int(resolution.split("kb")[0])*1000
	chrdict={}
	f1=open(chrlen, "r")
	for line in f1:
		line=line.strip()
		line=line.split()
		chrdict[line[0]]=int(line[1])
	f1.close()

	f=open(infile, "r")
	domainindex=0
	for i, line in enumerate(f):
		if i>=1:
			line=line.strip()
			line=line.split()
			start=int(line[2])
			end=int(line[-1])	
			realstart=(start-1+int(marginerror))*int(res)
			realend=(end-1-int(marginerror))*int(res)
			if realstart<realend:
				if realstart<=0:
					realstart=0
				if realend>=chrdict.get(chromo):
					realend=chrdict.get(chromo)
				ss=chromo+"\t"+str(realstart)+"\t"+str(realend)+"\t"+chromo+".domain."+str(domainindex)
				print(ss)
				domainindex=domainindex+1
	f.close()

	laststart=(end-1+int(marginerror))*int(res)
	if laststart <chrdict.get(chromo):
		ss=chromo+"\t"+str(laststart)+"\t"+str(chrdict.get(chromo))+"\t"+chromo+".domain."+str(domainindex)
		print(ss)

if __name__=="__main__":
	infile=sys.argv[1]
	chrlen=sys.argv[2]
	chromo=sys.argv[3]
	res=sys.argv[4]
	marginerror=sys.argv[5]	
	getdomain(infile, chrlen, chromo, res, marginerror)
