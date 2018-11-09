# The Python Challenge
The Pyhton Challenge is part of the Berkeley Extension Data Analytics Bootcamp Program. Challenge was target to  speed up the analysis process using Pyhton. 
The Pyhton Challenge includes two part: 
- [PyBank](PyBank/main.py) - script for analyzing the financial records of company.
    * CSV file  [budget_data.csv](PyBank/budget_data.csv) was used to analyze the financial records of the company.
    ```#read file
    with open ("budget_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    ```
    * Results of the analysis were printed and written as a [test_output.txt](PyBank/test_output.txt)
    ```# printing data summary
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
    ```
    
- [PyPoll](PyPoll/main.py) - script that helps to modernize and analyze the vote-counting process for small, rural town.
    * CSV file  [election_data.csv](PyPoll/election_data.csv) was used to analyze the election data of the town.
    ```#read file
    with open ("election_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    ```
    * Results of the analysis were printed and written as a [test_output.txt](PyPoll/test_output.txt)
    ```#printing results
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
    ```

# Prerequisites
* For this project the command line was used to run following comands:
* To create a new python 3.6 environment.
    * `conda create --name PythonData python=3.6 anaconda`
* To activate the newly created environment on Mac OS. 
    * `source activate PythonData`
* To check that Jupyter notebook is running properly.
    * `jupyter notebook`
