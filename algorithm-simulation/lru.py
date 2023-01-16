import datetime, csv

def calcPageFaults(pages, capacity):
    s = []
    pageFaults = 0

    for i in pages:
        if i not in s:
            if(len(s) == capacity):
                s.remove(s[0])
                s.append(i)
            else:
                s.append(i)
            pageFaults +=1
        else:
            s.remove(i)
            s.append(i)
    return pageFaults

def processInput(pages, capacity):
    pageFaults = calcPageFaults(pages, capacity)
    n = len(pages)
    print("LRU Page Faults: \t" + str(pageFaults))
    print("LRU Hit: \t\t" + str(n - pageFaults))

    saveToFile(pages, capacity, (n - pageFaults), pageFaults)

def saveToFile(pages, capacity, pageHits, pageFaults):
    filePath = './logs/pagesc/pages_c7/LRU_'+ (str(datetime.datetime.now())).replace(' ', '_').replace(':', '').replace('.', '') + '.csv'
    nameList = ['Pages', 'Capacity', 'Page Hits', 'Page Fault']
    statsList = [len(pages), capacity, pageHits, pageFaults]
    with open(filePath, 'w', encoding='utf-8', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(nameList)
        writer.writerow(statsList)
        for page in pages:
            writer.writerow(str(page))
    
    with open('./logs/pagesc/pages_c7/LRU_summary.csv', 'a', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(statsList)
        

def main():
    processInput([1,2,3,6,5,4], 3)

if __name__ == '__main__':
    main()
