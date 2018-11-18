import re

fp = open("txt\pg21580.txt","r")
lines = fp.readlines()

for line in lines[0:10]:
    line = line.strip() #removes the newline at the end of the line
    line = line.lower() #converts to lowercase
    
    print(line.strip())
