import csv
import os

inputFileName = '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'
outputFileName = 'FinancialAnalysis.csv'
csvInPath = os.path.join('..', 'inputs', inputFileName)
csvOutPath = os.path.join('..', 'outputs', outputFileName)

monthCount = 0
total = 0.0
sumChange = 0
maxIncrease = 0.0
maxIncrMnth =''
maxDecrease = 0.0
maxDecrMnth =''
hold =0.0 # used to hold the prior period value
change =0.0


with open(csvInPath) as f:
	csvreader = csv.reader(f, delimiter=',')
    #skip the header
	next(csvreader)

	for x in csvreader:
		monthCount +=1
		total=  float(x[1]) + total
		if monthCount > 1:
			change = float(x[1]) - hold #compare to previous period for current period change
			sumChange = sumChange + change
		if change > maxIncrease:
			maxIncrease = change
			maxIncrMnth = x[0]
		elif change < maxDecrease:
			maxDecrease = change
			maxDecrMnth = x[0]
		hold = float(x[1])


#print the output
print('Financial Analysis')
print('------------------')
print(f'Total Months: {monthCount}')
print(f'Total: ${int(total)}')
print(f'Average  Change: ${round((sumChange/monthCount),2)}')
print(f'Greatest Increase in Profits: {maxIncrMnth} (${int(maxIncrease)})')
print(f'Greatest Decrease in Profits: {maxDecrMnth} (${int(maxDecrease)})')



# Output to file 
with open(csvOutPath, 'w', newline='') as t:
    csvwriter = csv.writer(t, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow([f'Total Months:', monthCount]) #i want values after delim 
    csvwriter.writerow([f'Total:$', int(total)])
    csvwriter.writerow([f'Average  Change: $', round((sumChange/monthCount),2)])
    csvwriter.writerow([f'Greatest Increase in Profits:', maxIncrMnth ,int(maxIncrease)])
    csvwriter.writerow([f'Greatest Decrease in Profits:', maxDecrMnth ,int(maxDecrease)])
    

    





