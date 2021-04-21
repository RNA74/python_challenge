import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

csv_path = os.path.join('..','PyPoll','Resources','election_data.csv')
print(csv_path)
print(type(csv_path))
candidates = []
candidates_votes={}
totalvotes = 0
winning_count = 0
with open(csv_path,'r', encoding="utf-8") as csvfile:
    print(f'File {csv_path} opened.')
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    
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

     votes = candidates_votes.get(x)
     vote_percantage = round((votes/totalvotes) * 100, 2)

     if (votes > winning_count):
        winning_count = votes
        winning_candidates = x
     output= f'{x}: {vote_percantage}% ({votes})\n'
     print(output)

     export_file.write(output)
 
  winning_summary = (f'Winner: {winning_candidates}')  
  print(winning_summary)     
  export_file.write(winning_summary)







       







