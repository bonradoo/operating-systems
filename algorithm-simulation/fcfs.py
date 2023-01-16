import csv, datetime

def calculation(processes: list) -> list[int]:
    processes.sort(key=lambda x: x[1])
    completionTime = 0
    result = []
    
    for process in processes:
        name, arrivalTime, burstTime = process
        completionTime = max(completionTime, arrivalTime)
        result.append((name, arrivalTime, burstTime, completionTime-arrivalTime, completionTime, completionTime + burstTime))
        completionTime += burstTime

    return result

def processesInput(processesTuples):
    processes = []
    for i in range(len(processesTuples)):
        temp = []
        temp.append('p'+str(i))
        temp.append(processesTuples[i][0])
        temp.append(processesTuples[i][1])
        processes.append(tuple(temp))

    results = calculation(processes)
    waitTimes = [i[4] for i in results]
    turnAroundTimes = [i[3] for i in results]
    saveResults(results, waitTimes, turnAroundTimes)

def saveResults(results, waitTimes, turnAroundTimes):
    headerList = ['ID', 'Arrival Time', 'Burst Time', 'Completion Time', 'Turn Around Time', 'Wait Time']
    calcList = ['Avg WT', 'Max WT', 'Avg TAT', 'Max TAT']
    avgList = [str(round(sum(waitTimes)/len(waitTimes), 5)).replace('.', ','), str(max(waitTimes)).replace('.',','), str(round(sum(turnAroundTimes)/len(turnAroundTimes), 5)).replace('.',','),str(max(turnAroundTimes)).replace('.',',')]
    filePath = './logs/process/FCFS_' + (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    with open(filePath, 'w',newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(calcList)
        writer.writerow(avgList)
        writer.writerow(headerList)
        for tup in results:
            writer.writerow(tup)
        
    with open('./logs/process/FCFS_summary.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(avgList)

    print('FCFS average turn around time: ', str(round(sum(turnAroundTimes)/len(turnAroundTimes), 5)).replace('.',','))
    print('FCFS average wait time: ', str(round(sum(waitTimes)/len(waitTimes), 5)).replace('.', ','))

def main():
    pass

if __name__ == '__main__':
    main()