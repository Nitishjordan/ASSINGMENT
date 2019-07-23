def read_numbers ( f ):
    print("Reading file", f, "...", end=" ")
    numbers = []
    with open(f, 'r') as f:
        for line in f:
            numbers += [int(line.strip())]
    print("done.")
    return numbers

def overlapping_elements ( list1, list2 ):
    print("Finding overlapping elements in these two lists ...", end=" ")
    result = []
    for i in list1:
        if i in list2:
            result += [i]
    print("done.")
    return result

if __name__=="__main__":
    prime_numbers = read_numbers("primenumbers.txt")
    happy_numbers = read_numbers("happynumbers.txt")
    overlapping = overlapping_elements(prime_numbers, happy_numbers)
    print(overlapping)
    print("'One line' solution:")
    print([n for n in prime_numbers if n in happy_numbers])