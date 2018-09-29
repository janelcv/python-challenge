#name the title

#import csv file
import csv
#define variable
voteslist = []
candidatelist = []
khanlist = []
correylist =[]
lilist = []
otooleylist = []
final_list ={}
khan, correy, li, otooley = 0, 0 , 0 , 0
totalkhan, totalcorrey, totalli, totalotooley = 0, 0 ,0 , 0
totalvote=0
winner = 0
datasum = 0
#read file
with open ("election_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
        #creating new dictionaries
        voteslist.append(line["Voter ID"])
        candidatelist.append(line["Candidate"])

    #counting number total number of votes
    totalvote = int(len(voteslist))
    #creating new dictionary with voters and candidates
    newdict=dict(zip(voteslist,candidatelist))
    #counting votes for each candidate
    khanlist = {k:v for (k,v) in newdict.items() if v=="Khan"}
    khan = int(len(khanlist))
    correylist = {k:v for (k,v) in newdict.items() if v=="Correy"}
    correy = int(len(correylist))
    lilist = {k:v for (k,v) in newdict.items() if v=="Li"}
    li = int(len(lilist))
    otooleylist = {k:v for (k,v) in newdict.items() if v=="O'Tooley"}
    otooley = int(len(otooleylist))
    totalkhan=(int(len(khanlist))/totalvote)*100
    totalcorrey=(int(len(correylist))/totalvote)*100
    totalli=(int(len(lilist))/totalvote)*100
    totalotooley=(int(len(otooleylist))/totalvote)*100
    
#printing results
final_list = {"Khan":khan, "Correy":correy, "Li":li, "O'Tooley":otooley }
winner = max(final_list, key=final_list.get)
datasum = f"""
    Election Results
    ----------------------
    Total Votes: {totalvote}
    ----------------------
    Khan: {totalkhan}% ({khan})
    Correy: {totalcorrey}% ({correy})
    Li: {totalli}% ({li})
    O'Tooley: {totalotooley}% ({otooley})
    ----------------------
    Winner: {winner}
    ----------------------
    """
print(datasum)

# putting data summary as a .txt file output
f = open('test_output.txt','w')
f.write(datasum)
f.close()