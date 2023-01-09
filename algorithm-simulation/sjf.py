import csv, datetime

def calculation(processes: list) -> list[int]:
    processes.sort(key=lambda x: x[1])
    completionTime = 0
    queue = []
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
    print('SJF:')
    print('     Average wait time: ', round(sum(waitTimes)/len(waitTimes), 5))
    print('     Max wait time: ', max(waitTimes))
    print('     Average turn around time: ', round(sum(turnAroundTimes)/len(turnAroundTimes), 5))
    print('     Max turn around time: ', max(turnAroundTimes))

def saveResults(results, waitTimes, turnAroundTimes):
    headerList = ['ID', 'Arrival Time', 'Burst Time', 'Turn Around Time', 'Wait Time', 'Completion Time']
    calcList = ['Avg WT', 'Max WT', 'Avg TAT', 'Max TAT']
    avgList = [str(round(sum(waitTimes)/len(waitTimes), 5)).replace('.', ','), str(max(waitTimes)).replace('.',','), str(round(sum(turnAroundTimes)/len(turnAroundTimes), 5)).replace('.',','),str(max(turnAroundTimes)).replace('.',',')]
    filePath = './logs/process/SJF_' + (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    with open(filePath, 'w',newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(calcList)
        writer.writerow(avgList)
        writer.writerow(headerList)
        for tup in results:
            writer.writerow(tup)

def main():
    pass

if __name__ == '__main__':
    main()

