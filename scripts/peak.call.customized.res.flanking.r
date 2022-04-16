#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
#please use the correct R version

#args1:the chipseq density cleanup file:/home/lina/loops.domain.project/chipseq.test/A549/A549.H3K27ac.chipseq.chr/A549.H3K27ac.chipseq.density.res.50kb.flanking.500kb/*.density.cleanup.txt
#args2: chromosome
#args3; span
#args4: resolution
#args5:flanking
#args6: the peakcall summit and boundary location save file
#args7: the peakcall plot save file
#args8: the minimum height you want to get the peaks and valley

spanvalue=as.numeric(args[3])
depthvalue=as.numeric(args[8])
#print(spanvalue)
#print(depthvalue)

set.seed(4)
library(pracma)
data=read.table(args[1], header=F, row.names=NULL)
colnames(data)=c("chr", "start", "end", "bin", "density")
normdensity=data$density/max(data$density)
newdata=data.frame(seq(1, dim(data)[1]),normdensity)
colnames(newdata)=c("bin", "density")

#smoothing
defaultW <- getOption("warn") 
options(warn = -1) 
loessMod10 <- loess(newdata$density~newdata$bin, data=newdata, span=spanvalue)
yf <- predict(loessMod10)
options(warn = defaultW)
peaksinitial=findpeaks(yf, nups=1, minpeakheight=depthvalue)
colnames(peaksinitial)=c("height", "summit", "start", "end")
write.table(peaksinitial, args[6], sep="\t", quote=F, row.names=F)


#plot
pdf(args[7], width=50, height = 10)
last=dim(newdata)[1]-1
plotname=paste( args[2], "res", args[4], "flanking", args[5], sep=".")
plot(newdata$density,type="h", lwd=3, col="blue", ylab="Peak Density", xlab=args[2], 
     main=plotname, xlim=c(0, last),
     cex.lab=3, cex.axis=2, cex.main=5)
lines(x=seq(0, last), lwd=5, y=yf, col="red")
xtick<-seq(0,last, by=100)
axis(side=1, at=xtick, labels = FALSE)
dev.off()
