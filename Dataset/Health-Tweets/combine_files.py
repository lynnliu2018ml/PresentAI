import re

input_files = ["bbchealth.txt", "cbchealth.txt", "cnnhealth.txt", "everydayhealth.txt", "foxnewshealth.txt", "gdnhealthcare.txt", "goodhealth.txt", "KaiserHealthNews.txt", "latimeshealth.txt", "msnhealthnews.txt", "NBChealth.txt", "nprhealth.txt", "nytimeshealth.txt", "reuters_health.txt", "usnewshealth.txt", "wsjhealth.txt"]
combined = "combined.csv"
error_lines = "error.txt"

ferr = open(error_lines,"w")
fout = open(combined, "w")
for file in input_files:
	print(file)
	with open(file, "r") as fp:
		lines = fp.readlines()
		for line in lines:
			line = re.sub(r'[^\x00-\x7F]',' ', line)
			#uncomment the following lines to remove http links from the data
			#line = re.sub("http:[a-zA-Z/\.0-9?=-]+", " ", line)
			#line = re.sub("https:[a-zA-Z/\.0-9?=-]+", " ", line)
			if len(line.split("|"))==3: #if the number of columns is equal to 3, retain the row, else write to the error file
				fout.write(line)
			else:
				ferr.write(line)
				
fout.close()		
ferr.close()		

