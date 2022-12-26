import argparse

class Process:
    def __init__(self, arrivalTime: int, computationTime: int):
        self.arrivalTime = arrivalTime
        self.computationTime = computationTime

def inputHandler():
    parser = argparse.ArgumentParser(description='File input handler')
    parser.add_argument('-f', '--file', default='default.txt', help='Provide filepath (default: %(default)s)')
    args = parser.parse_args()
    return args

def calculation(processes: list):
    processes.sort(key=lambda p: p.arrivalTime)
    



def main():
    pass

if __name__ == '__main__':
    main()

