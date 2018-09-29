#name the title
#import csv file
import csv
#define variable
valuelist = []
datelist = []
differencelist = []
date=0
total=0
greatinc=0
greatdec =0
datasum=0

#find max in the list 
def return_greatest_increase(list):
    countmax = 0
    for number in list:
        if countmax < number:
           countmax = number
    return countmax

#find min in the list  
def return_greatest_decrease(list):
    countmin = 0
    for number in list:
        if countmin > number:
           countmin = number
    return countmin

#find average in the list
def return_average_change(list):
    countsum = 0
    avgchange = 0
    for number in list:
        countsum = countsum + number
    avgchange = (countsum/int(len(list)-1))
    return avgchange
  
#read file
with open ("budget_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
#starting loop
    for line in csvreader:
        valuelist.append(line["Profit/Losses"])
        datelist.append(line["Date"])
        date = int(len(datelist))
        total += int(line["Profit/Losses"])
differencelist.append(0)
#define new list to loop through
for x in range(1,int(len(datelist))):
    #creating new list which will consist of the diffences between rows 
    differencelist.append(int(valuelist[x])-int(valuelist[x-1]))
    #creating new dictionary with existing lists

newdict=dict(zip(differencelist,datelist))

#finding max and min, avgchance
avgchange = return_average_change(differencelist)
greatinc = return_greatest_increase(differencelist)
greatdec = return_greatest_decrease(differencelist)

# printing data summary
datasum = f"""

    Financial Analysis
    -------------------------
    Total Months:{date}
    Total: ${total}
    Average Change:${avgchange}
    Greatest Increase in Profits:{newdict[greatinc]}(${greatinc})
    Greatest Decrease in Profits:{newdict[greatdec]}(${greatdec})
   """
print(datasum)

# putting data summary as a .txt file output
f = open('test_output.txt','w')
f.write(datasum)
f.close()