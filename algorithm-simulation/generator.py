import random

#n = number of processes in a list
def processGenList(n=100):
    result = []
    for _ in range(n):
        temp = []
        temp.append(random.randint(0,10))
        temp.append(random.randint(0,10))
        temp = tuple(temp)
        result.append(temp)
    return result

def pageGenList(n=20):
    result = [random.randint(1,7) for _ in range(n)]
    return(result)

def main():
    pass

if __name__ == '__main__':
    main()