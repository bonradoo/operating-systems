import csv, datetime

def calcTurnAroundTime(processes):
    turnAroundTimes = [i[4] - i[1] for i in processes]
    for i in range(len(processes)):
        processes[i].append(turnAroundTimes[i])
    return turnAroundTimes

def calcWaitingTime(processes):
    waitTimes = [i[5] - i[2] for i in processes]
    for i in range(len(processes)):
        processes[i].append(waitTimes[i])
    return waitTimes

def scheduling(processes):
    currentTime = 0

    for _ in range(len(processes)):
        readyQueue = []
        waitQueue = []

        for j in range(len(processes)):
            if (processes[j][1] <= currentTime) and (processes[j][3] == 0):
                readyQueue.append([processes[j][0], processes[j][1], processes[j][2]])
            elif processes[j][3] == 0:
                waitQueue.append([processes[j][0], processes[j][1], processes[j][2]])

        if len(readyQueue) != 0:
            readyQueue.sort(key=lambda x: x[2])

            currentTime = currentTime + readyQueue[0][2]
            eTime = currentTime

            k = next(index for (index, process) in enumerate(processes) if process[0] == readyQueue[0][0])

            processes[k][3] = 1
            processes[k].append(eTime)

        elif len(readyQueue) == 0:
            if currentTime < waitQueue[0][1]:
                currentTime = waitQueue[0][1]

            currentTime = currentTime + waitQueue[0][2]
            eTime = currentTime

            k = next(index for (index, process) in enumerate(processes) if process[0] == readyQueue[0][0])

            processes[k][3] = 1
            processes[k].append(eTime)

    turnAroundTimes = calcTurnAroundTime(processes)
    waitTimes = calcWaitingTime(processes)
    saveResults(processes, turnAroundTimes, waitTimes)

def processesInput(processesTuples):
    processes = []
    for i in range(len(processesTuples)):
        processes.append([i, processesTuples[i][0], processesTuples[i][1], 0])
    processes.sort(key=lambda x: x[1])

    scheduling(processes)

def saveResults(processes, turnAroundTimes, waitTimes):
    headerList = ['ID', 'Arrival Time', 'Burst Time', 'Completion Time', 'Turn Around Time', 'Wait Time']
    calcList = ['Avg WT', 'Max WT', 'Avg TAT', 'Max TAT']
    avgList = [str(round(sum(waitTimes)/len(waitTimes), 5)).replace('.', ','), str(max(waitTimes)).replace('.',','), str(round(sum(turnAroundTimes)/len(turnAroundTimes), 5)).replace('.',','),str(max(turnAroundTimes)).replace('.',',')]
    filePath = './logs/process/SJF_' + (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    with open(filePath, 'w',newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(calcList)
        writer.writerow(avgList)
        writer.writerow(headerList)
        for res in processes:
            #      id            at            bt            complt        tat           wt
            line = [str('p' + str(res[0])), str(res[1]), str(res[2]), str(res[4]), str(res[5]), str(res[6])]
            writer.writerow(line)
        
    with open('./logs/process/SJF_summary.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(avgList)

    print('SJF average turn around time: ', str(round(sum(turnAroundTimes)/len(turnAroundTimes), 5)).replace('.',','))
    print('SJF average wait time: ', str(round(sum(waitTimes)/len(waitTimes), 5)).replace('.', ','))

def main():
    pass

if __name__ == '__main__':
    main()