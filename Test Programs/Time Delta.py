import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):    
    timestamp1 = t1[4:]
    timestamp2 = t2[4:]
    time1 = datetime.strptime(timestamp1,"%d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(timestamp2,"%d %b %Y %H:%M:%S %z")
    time_difference = abs(time2 - time1)
    time_in_secs = time_difference.total_seconds()
    print (time_in_secs) 
    
    # timestamp1 = t1.split(" ")
    # timestamp2 = t2.split(" ")
        
    # # print (time1,time2)
    # date1 = timestamp1 [1:4]
    # date2 = timestamp2 [1:4]   
    # #print (date1,date2)
    # date1_str = ' '.join(date1)
    # date2_str = ' '.join(date2)
    # #print (date1_str,date2_str)
    # if date1_str == date2_str:
    #    time1 = timestamp1 [4]
    #    time2 = timestamp2 [4]
    #    #print (time1,time2)
    #    if time1 == time2:
    #        timezone1 = timestamp1 [-1]
    #        timezone2 = timestamp2 [-1]
    #        print(timezone1-timezone2)
            

if __name__ == '__main__':
    # fptr = open(os.environ['C:\Muneeb\Data Prism\Projects\Practice Projects\Muneeb\Python'], 'w')

    test_cases = int(input("Enter the number of test cases: "))

    for t_itr in range(test_cases):
        t1 = input(f"Enter timestamp 1 of test case {t_itr+1}: ")

        t2 = input(f"Enter timestamp 2 of test case {t_itr+1}: ")

    #     delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
    time_delta (t1,t2)