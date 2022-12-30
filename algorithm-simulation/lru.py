def foo(pages):
    #Tworzymy słownik, który będzie przechowywać strony w pamięci operacyjnej
    memory = {}

    #Ustawiamy maksymalną liczbę stron, które mogą być przechowywane w pamięci
    max_pages = 3

    #Iterujemy przez zapotrzebowanie na strony
    for page in pages:
    #Jeśli strona jest już w pamięci, to usuwamy ją i dodajemy ponownie
        if page in memory:
            memory.pop(page)
        #Jeśli strona nie jest w pamięci, ale pamięć jest pełna, to usuwamy najrzadziej używaną stronę
        elif len(memory) == max_pages:
            memory.pop(min(memory, key=memory.get))
    #Dodajemy stronę do pamięci
    memory[page] = 0
    #Zwiększamy licznik użycia dla każdej strony w pamięci
    for key in memory:
        memory[key] += 1

    #Wynikowa pamięć operacyjna
    print(memory)

def main():
    pass

if __name__ == '__main__':
    main()

