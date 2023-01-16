from queue import Queue
import csv, datetime

def calcPageFaults(pages, n, capacity):
    s = set()
    queue = Queue()
    pageFaults = 0

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                pageFaults += 1
                queue.put(pages[i])
        else:
            if pages[i] not in s:
                val = queue.queue[0]
                queue.get()
                s.remove(val)
                s.add(pages[i])
                queue.put(pages[i])
                pageFaults += 1
    return pageFaults

def processInput(pages, capacity):
    n = len(pages)
    pageFaults = calcPageFaults(pages, n, capacity)
    print("FIFO Page Faults: \t" + str(pageFaults))
    print("FIFO Hit: \t\t" + str(n - pageFaults))
    saveToFile(pages, capacity, (n-pageFaults), pageFaults)

def saveToFile(pages, capacity, pageHits, pageFaults):
    filePath = './logs/pages/pages_c7/FIFO_'+ (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    nameList = ['Pages', 'Capacity', 'Page Hits', 'Page Fault']
    statsList = [len(pages), capacity, pageHits, pageFaults]
    with open(filePath, 'w', encoding='utf-8', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(nameList)
        writer.writerow(statsList)
        for page in pages:
            writer.writerow(str(page))
    
    with open('./logs/pages/pages_c7/FIFO_summary.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(statsList)


def main():
    processInput([1,2,3,6,5,4], 3)

if __name__ == '__main__':
    main()
