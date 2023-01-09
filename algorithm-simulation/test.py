import generator
def temp():
    asdf = generator.processGenList(5)
    processes = []
    for i in range(len(asdf)):
        temp = []
        temp.append('p'+str(i))
        temp.append(asdf[i][0])
        temp.append(asdf[i][1])
        processes.append(tuple(temp))
    return processes

def main():
    processes = temp()
    processes.sort(key=lambda x: x[1])
    queue = []
    waiting = []
    result = []
    currentTime = 0

    [print(process) for process in processes]
    print('Curr ', currentTime)
    
    for process in processes:
        if process[1] <= currentTime:
            waiting.append(process)
        currentTime += 1

    for currentTime in range(11):
        for process in processes:
            if process[1] <= currentTime:
                waiting.append(process)
                processes.remove(process)



    print(waiting)







main()