import argparse, csv, datetime

def inputHandler():
    parser = argparse.ArgumentParser(description='File input handler')
    parser.add_argument('-f', '--file', default='default.txt', help='Provide filepath (default: %(default)s)')
    args = parser.parse_args()
    return args

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
    saveResults(results)
    waitTimes = [i[4] for i in results]
    turnAroundTimes = [i[3] for i in results]

    print('FCFS:')
    print('     Average wait time: ', round(sum(waitTimes)/len(waitTimes), 5))
    print('     Max wait time: ', max(waitTimes))
    print('     Average turn around time: ', round(sum(turnAroundTimes)/len(turnAroundTimes), 5))
    print('     Max turn around time: ', max(turnAroundTimes))

def saveResults(results):
    headerList = ['ID', 'Arrival Time', 'Burst Time', 'Turn Around Time', 'Wait Time', 'Completion Time']
    filePath = './logs/' + (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    with open(filePath, 'w',newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(headerList)
        for tup in results:
            writer.writerow(tup)

def main():
    pass

if __name__ == '__main__':
    main()

