from collections import OrderedDict

#Tworzymy słownik, który będzie przechowywać strony w pamięci operacyjnej
#Ustawiamy maksymalną liczbę stron, które mogą być przechowywane w pamięci
#Iterujemy przez zapotrzebowanie na strony
#Jeśli strona jest już w pamięci, to usuwamy ją i dodajemy ponownie
#Jeśli strona nie jest w pamięci, ale pamięć jest pełna, to usuwamy najrzadziej używaną stronę
#Dodajemy stronę do pamięci
#Zwiększamy licznik użycia dla każdej strony w pamięc
#Wynikowa pamięć operacyjna

def foo(capacity: int, pages: list):
    # memory = {}
    # capacity = 3
    # for page in pages:
    #     if page in memory:
    #         memory.pop(page)
    #     elif len(memory) == capacity:
    #         memory.pop(min(memory, key=memory.get))

    # memory[page] = 0
    # for key in memory:
    #     memory[key] += 1
    #     print(memory.keys())


    memory = {}
    
    for page in pages:
        if page in memory:
            memory[page] += 1
        else:
            memory.update({page: 1})

                
    

    memory = dict(sorted(memory.items(), key=lambda x: x[1], reverse=True))

    result = {}

    while len(memory) > capacity:
        memory.popitem()

    print(memory)

def main():
    pass

if __name__ == '__main__':
    main()

