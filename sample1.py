import re
import sys

from datetime import datetime

start_time=sys.argv[1]
end_time=sys.argv[2]
logfile_path=sys.argv[3]


start_time_obj = datetime. strptime(start_time, '%d/%b/%Y:%H:%M:%S %z')
end_time_obj = datetime. strptime(end_time, '%d/%b/%Y:%H:%M:%S %z')



counters = {"304" : 0, "200" : 0, "404": 0}


def myfunction(line):

    date_match = re.search(r'(\d+)/(\w+)/(\d+):(\d*):(\d*):(\d*) \+\d*', line)
    errorcode = re.search(r' (\d\d\d) ', line)
    if (type(date_match) == "NoneType" ):
        print (line)
    date_time_obj = datetime. strptime(date_match[0], '%d/%b/%Y:%H:%M:%S %z')
   
   


    if date_time_obj > start_time_obj :
        if date_time_obj < end_time_obj :
            if errorcode[1]=="304":
                counters["304"]=counters["304"]+1
            if errorcode[1]=="404":
                counters["404"]=counters["404"]+1
            if errorcode[1]=="200":
                counters["200"]=counters["200"]+1         
              
        
with open(logfile_path) as f:
   for line in f:
       # For Python3, use print(line)
       myfunction (line)
       

total=(counters["404"]+counters["200"]+counters["304"])
returnstring = "The site has returned a total of {} 200 responses, and {} 404 \n responses, out of a total {} requests between time {} and time {} \n That is a  {}% 404 errors, and {}% of 200 responses."
print(returnstring.format(counters["200"], counters["404"], total, start_time, end_time, (counters["404"]/total)*100, (counters["200"]/total)*100 ))