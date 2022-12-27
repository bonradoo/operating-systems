import random

#n = number of processes in a list
def generateList(n=100):
    result = []
    for _ in range(n):
        temp = []
        temp.append(random.randint(0,10))
        temp.append(random.randint(0,10))
        temp = tuple(temp)
        result.append(temp)
    return result

def main():
    pass

if __name__ == '__main__':
    main()