import sys

def remedysliding(sliding, infile):
	windowdict={}
	f1=open(sliding, "r")	
	for line in f1:
		line=line.strip()
		line=line.split()
		name="\t".join(str(x) for x in line)
		windowdict[name]=0
	f1.close()

	f2=open(infile, "r")
	for line in f2:
		line=line.strip()
		line=line.split()
		keyname="\t".join(str(x) for x in line[0:4])
		value=line[-1]
		if keyname in windowdict:
			windowdict[keyname]=value
		else:
			print(keyname+" no.found!")
			break
	f2.close()

	for key, value in windowdict.items():
		ss=key+"\t"+str(value)
		print(ss)

if __name__=="__main__":
	sliding=sys.argv[1]
	infile=sys.argv[2]
	remedysliding(sliding, infile)
