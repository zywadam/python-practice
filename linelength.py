# -problem3_6.py *- coding: utf-8 -*-

import sys
filename = sys.argv[1]
outfilename = sys.argv[2]
# print("\n",filename,"\n")  # You can check that the filename is correct
    
text_file = open(filename)     # open the file for reading
outfile = open(outfilename,'w')

# initialize line, word, and char counters to 0


for line in text_file:           # step through each line in the text file
    print(len(line))
    line.strip("\n")
    outfile.write(len(line)+" \n")

outfile.close
text_file.close() 

# add your code here