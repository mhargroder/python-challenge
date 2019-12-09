import csv
import os

inputFileName = '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'
outputFileName = 'ElectionResults.csv'
csvInPath = os.path.join('..', 'inputs', inputFileName)
csvOutPath = os.path.join('..', 'outputs', outputFileName)
candidates =[]
voteTalley = {}
totalVotes = 0
votePerc =0.0
maxVoteCount = 0
winner =''

#create a unique list of candidates and create dict with candidate and vote count for talley as k:v
with open(csvInPath) as f:
	csvreader = csv.reader(f, delimiter=',')
#skip the header
	next(csvreader)

	for v in csvreader:
		totalVotes +=1
		if v[2] in candidates:
			voteTalley[v[2]] +=1
		else:
			candidates.append(v[2])
			voteTalley.update({v[2]:1})

#determine candidate %s, winner, and print 
print('Election Results')
print('-----------------')
print(f'Total Votes: {totalVotes}')
print('-----------------')

for k,v in voteTalley.items():
	votePerc = round(((v/totalVotes)*100),2)
	print(f'{k}: {votePerc}% ({v})')

	if v > maxVoteCount:
		maxVoteCount = v
		winner = k
	else:
		pass
print('-----------------')
print(f'Winner: {winner}')

#export output
with open(csvOutPath, 'w', newline='') as t:
    csvwriter = csv.writer(t, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------'])
    csvwriter.writerow(['TotalVotes:', totalVotes])
    csvwriter.writerow(['Winner:', winner])
    csvwriter.writerow(['----------------'])
    for k,v in voteTalley.items():
    	votePerc = round(((v/totalVotes)*100),2)
    	csvwriter.writerow([k,str(votePerc)+'%','['+str(v)+']'])

#THE END
