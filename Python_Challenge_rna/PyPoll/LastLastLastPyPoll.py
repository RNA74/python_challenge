import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

csv_path = os.path.join('..','election_data.csv')
print(csv_path)
print(type(csv_path))
candidates = []
candidates_votes={}
totalvotes = 0
with open(csv_path,'r', encoding="utf-8") as csvfile:
    print(f'File {csv_path} opened.')
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    print(csvreader)

    for row in csvreader:
        totalvotes= totalvotes + 1
        candidates_name= row[2]


        if candidates_name not in candidates:
           candidates.append(candidates_name)
           candidates_votes[candidates_name]= 0
        candidates_votes[candidates_name]= candidates_votes[candidates_name]+1

print('Election Results')
print('-------------------------')
print( f'Total Votes: {totalvotes}')
print('-------------------------')
print(candidates_votes)
with open('../results.txt','w') as export_file:
  for x in candidates_votes:
     export_file.write(f'{x: <40}  {candidates_votes.get(x)}\n')
 


/usr/local/bin/python3 "/Users/rnababikar/bootcamp/hw/python_challenge/HW03-Python 2/Instructions/PyPoll/Resources/PyPoll/LastLastPyPoll.py"
(base) Rnas-iMac:Instructions rnababikar$ /usr/local/bin/python3 "/Users/rnababikar/bootcamp/hw/python_challenge/HW03-Python 2/Instructions/PyPoll/Resources/PyPoll/LastLastPyPoll.py"
../election_data.csv
<class 'str'>
File ../election_data.csv opened.
<_csv.reader object at 0x7ff60ba25900>
Election Results
-------------------------
Total Votes: 3521002
-------------------------
{'Candidate': 1, 'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
(base) Rnas-iMac:Instructions rnababikar$ 









       







