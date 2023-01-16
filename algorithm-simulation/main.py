import fcfs, sjf, generator, argparse, time, lru, fifo

def inputHandler():
    parser = argparse.ArgumentParser(description='File input handler')
    parser.add_argument('-a', '--amount', default=100, help='Provide number of processes (default: %(default)s)')
    parser.add_argument('-c', '--cycles', default=1, help='Provide number of cycles (default: %(default)s)')
    parser.add_argument('-p', '--pages', default=9, help='Provide distribution of pages (starting 0) (default: %(default)s)')
    parser.add_argument('-s', '--size', default=100, help='Provide amount of pages (default: %(default)s)')
    parser.add_argument('-y', '--capacity', default=9, help='Provide capacity of memory (default: %(default)s)')
    args = parser.parse_args()
    return args

def main():
    startTime = time.time()
    arguments = inputHandler()
    print('\nProcess scheduling algotithms (FCFS and SJF): ')
    print('Processes: \t', arguments.amount)
    print('Cycles: \t', arguments.cycles)

    print('\nPage scheduling algorithms (FIFO and LRU): ')
    print('Pages: \t\t', arguments.pages)
    print('Cycles: \t', arguments.cycles, '\n')
    
    for _ in range(int(arguments.cycles)):
        try:
            processList = generator.processGenList(int(arguments.amount))
            pageList = generator.pageGenList(int(arguments.pages), int(arguments.size))
        except:
            print('Error')

        sjf.processesInput(processList)
        fcfs.processesInput(processList)

        lru.processInput(pageList, int(arguments.capacity))
        fifo.processInput(pageList, int(arguments.capacity))

    endTime = time.time()

    print('\nReal computation time: ', round(float(endTime-startTime), 5))

if __name__ == '__main__':
    main()