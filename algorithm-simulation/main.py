import fcfs, sjf, generator, argparse, time, lru

def inputHandler():
    parser = argparse.ArgumentParser(description='File input handler')
    parser.add_argument('-a', '--amount', default=100, help='Provide number of processes (default: %(default)s)')
    parser.add_argument('-c', '--cycles', default=1, help='Provide number of cycles (default: %(default)s)')
    parser.add_argument('-p', '--pages', default=20, help='Provide number of pages (default: %(defualt)s)')
    args = parser.parse_args()
    return args

def main():
    startTime = time.time()
    arguments = inputHandler()
    
    for _ in range(int(arguments.cycles)):
        try:
            processList = generator.processGenList(int(arguments.amount))
            pageList = generator.pageGenList(int(arguments.pages))
        except:
            print('Error')

        # print('\nProcess scheduling algotithms: ')
        # print('Processes: ', arguments.amount)
        # print('Cycles: ', arguments.cycles)
        # sjf.processesInput(processList)
        # fcfs.processesInput(processList)

        print('\n\nPage scheduling algorithms: ')
        print('Pages: ', arguments.pages)
        print('Cycles: ', arguments.cycles)
        lru.foo(3, pageList)
    endTime = time.time()


    print('Real computation time: ', round(float(endTime-startTime), 5))

if __name__ == '__main__':
    main()