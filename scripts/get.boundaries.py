import sys

def getbound(infile, chrlen, resolution):
	res=int(resolution.split("kb")[0])*1000
	chrdict={}
	f=open(chrlen, "r")
	for line in f:
		line=line.strip()
		line=line.split()
		chrdict[line[0]]=int(line[1])
	f.close()

	start=[]
	end=[0]
	f1=open(infile, "r")
	for line in f1:
		line=line.strip()
		line=line.split()
		chromo=line[0]
		start.append(int(line[1]))
		end.append(int(line[2]))
	f1.close()

	for i in range(len(start)):
		b1=end[i]
		b2=start[i]+int(res)
		if b2>chrdict.get(chromo):
			b2=chrdict.get(chromo)
		ss=chromo+"\t"+str(b1)+"\t"+str(b2)+"\tboundary."+str(i)
		print(ss)

	k=len(end)-1
	laststart=end[-1]
	lastend=end[-1]+int(res)
	if lastend<chrdict.get(chromo):
		ss=chromo+"\t"+str(laststart)+"\t"+str(lastend)+"\t"+"boundary."+str(k)
		print(ss)

if __name__=="__main__":
	infile=sys.argv[1]
	chrlen=sys.argv[2]
	res=sys.argv[3]
	getbound(infile, chrlen, res)
