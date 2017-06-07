#! /usr/bin/env python

import os
import sys

####################
### Get Help
####################

# print the help and exit the programm

def getHelp() :
        print """matCutPy help
        Usage : python matCutPy.py input_file cutoff

        matCutPy generate a list of IDs with a total of estimated RNA-Seq
        fragment counts above a specified cutoff.
        The output file is named 'input_file'.cut
        """
        sys.exit()

# Is the first argument a call for help ? or is there the amount of required arguments ?

if len(sys.argv)!=3 :
        getHelp()


####################
### Variables
####################

#input file name
inFileName = sys.argv[1]
#output file name
outFileName = inFileName + '.cut'
#cutoff value
cutoff_var = int(sys.argv[2])

#Do the files exist ?
if not os.path.isfile(inFileName) :
        print inFileName, " can't be found \n"
        getHelp()


####################
### Functions
####################


def readMatrix(matrixFile, outFileName, cutoff) :

        readFile = open(matrixFile, 'r')
        outFile = open(outFileName, 'w')

        readFile.readline()
        for line in readFile :
                cols = line.split()
                if keepID(cols,cutoff) :
                        outFile.write(cols[0]+'\n')             

        readFile.close()                
        outFile.close()
        
def keepID(colList,cutoff):

        #Returns True if 1/4 of the values are above the cutoff
        keep = False
        supColNb = 0
        cols = colList[1:]
        #number of col needed to be true
        minColNb = len(cols)/4
        if len(cols)%4 != 0 :
                minColNb += 1
        for col in cols :
                if float(col) > cutoff :
                        supColNb += 1
        if supColNb >= minColNb :
                keep = True
        
        return keep
                

####################
### Main
####################

#printing a line to know that the programm is running. to be removed ?
print "running matCutPy"

readMatrix(inFileName, outFileName, cutoff_var)

#programm is over
print "done matCutPy"
