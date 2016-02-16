#!/usr/bin/python
# CharGer - Characterization of Germline variants
# author: Adam D Scott (ascott@genome.wustl.edu) & Kuan-lin Huang (khuang@genome.wustl.edu)
# version: v0.0 - 2015*12

import sys
import getopt
import glob
from scipy import stats

def main():
	# get and store all expression
	fileNames = glob.glob("Data_files/All_gene_RNASeq/*txt")
	for fileName in fileNames:
		print fileName
		inFile = open( fileName , "r" )
		header = inFile.readline()
		samples = header.split( "\t" )
		for line in inFile:
			fields = line.split( "\t" )
			gene = fields[0]
			gene_exp = [ toFloat(x) for x in fields[1:]] # manage potential NA strings that may cause errors
			gene_exp_p = (stats.rankdata(gene_exp, 'min')-1)/len(gene_exp) # convert to percentile
			gene_exp_p
			for i in range(1,len(gene_exp_p)):
						self.userExpression[samples[i+1]][gene] = gene_exp_p[i]
			#for i in range(1,len(gene_exp_p)):
				#print samples[i], gene, gene_exp_p[i]
					#self.userExpression[samples[i]][gene] = fields[i]

	# loop through file to annotate each sample based on their truncation effect
	# what to do when a sample has 2 truncations in the same gene?

def toFloat(x):
	try:
		float(x)
		return float(x)
	except:
		return "nan"


if __name__ == "__main__":
	main()