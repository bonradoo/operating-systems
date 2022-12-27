import fcfs, sjf, processGen, argparse, time

def inputHandler():
    parser = argparse.ArgumentParser(description='File input handler')
    parser.add_argument('-a', '--amount', default=100, help='Provide number of processes (default: %(default)s)')
    parser.add_argument('-c', '--cycles', default=1, help='Provide number of cycles (default: %(default)s)')
    args = parser.parse_args()
    return args

def main():
    startTime = time.time()
    arguments = inputHandler()
    
    for _ in range(int(arguments.cycles)):
        try:
            processList = processGen.generateList(int(arguments.amount))
        except:
            print('Error')

        
        print('Processes: ', arguments.amount)
        print('Cycles: ', arguments.cycles)

        fcfs.processesInput(processList)
    endTime = time.time()


    print('Real computation time: ', round(float(endTime-startTime), 5))

if __name__ == '__main__':
    main()