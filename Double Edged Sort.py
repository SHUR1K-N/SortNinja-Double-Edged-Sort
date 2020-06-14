unsorted = []; sorted = []; isEven = True
decisionMade = False; correctInput = False
correctPath = False


##### Odd functions #####

def ascendingOdd():
    if isEven is False:

        iterations = (len(unsorted) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(unsorted)
        big = max(unsorted)

        for i in range(iterations):

            sorted.insert(indexfirst, small)
            sorted.insert(indexlast, big)
            unsorted.remove(small)
            unsorted.remove(big)

            small = min(unsorted)
            big = max(unsorted)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, unsorted[0])
    return(sorted)


def descendingOdd():
    if isEven is False:

        iterations = (len(unsorted) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(unsorted)
        big = max(unsorted)

        for i in range(iterations):

            sorted.insert(indexfirst, big)
            sorted.insert(indexlast, small)
            unsorted.remove(big)
            unsorted.remove(small)

            small = min(unsorted)
            big = max(unsorted)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, unsorted[0])
    return(sorted)


##### Even functions #####

def ascendingEven():
    if isEven is True:

        iterations = (len(unsorted) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(unsorted)
        big = max(unsorted)

        for i in range(1, iterations):

            sorted.insert(indexfirst, small)
            sorted.insert(indexlast, big)
            unsorted.remove(small)
            unsorted.remove(big)

            small = min(unsorted)
            big = max(unsorted)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, small)
        sorted.insert(indexlast, big)
    return(sorted)


def descendingEven():
    if isEven is True:

        iterations = (len(unsorted) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(unsorted)
        big = max(unsorted)

        for i in range(1, iterations):

            sorted.insert(indexfirst, big)
            sorted.insert(indexlast, small)
            unsorted.remove(big)
            unsorted.remove(small)

            small = min(unsorted)
            big = max(unsorted)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, big)
        sorted.insert(indexlast, small)
    return(sorted)


def prompt(unsorted):
    while (decisionMade is False):
        print("\nMethods:-")
        print("1. Manual entry of integers\n2. Supply a number list file")
        decision = input("\nSelect method number: ")
        if (decision == "1"):
            while (correctInput is False):
                try:
                    unsorted = list(map(int, input("\nInput integers to sort (separated by spaces): ").split()))
                    break
                except ValueError:
                    print("\nInvalid character(s) entered. Input only integers. Try again.\n")
                    continue
            break

        elif (decision == "2"):
            while (correctPath is False):
                try:
                    filePath = input("\nEnter the file path here: ")
                    with open(filePath) as file:
                        for num in file:
                            integerize = int(num)
                            unsorted.append(integerize)
                    break

                except FileNotFoundError:
                    print("\nEither file does not exist or invalid path entered. Try again.\n")
                    continue
            break

        else:
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue
    return (unsorted)


##### Main #####

unsorted = prompt(unsorted)

if ((len(unsorted)) % 2 == 0):
    isEven = True
else:
    isEven = False

ascdesc = str(input("\nAscending or Descending? (Default = Ascending): ") or "ascending")
ascdesc = ascdesc.lower()

print("\nWorking...", end='')

if (ascdesc == "ascending"):
    small = min(unsorted)
    big = max(unsorted)
    if isEven is True:
        ascendingEven()
    elif isEven is False:
        ascendingOdd()

elif (ascdesc == "descending"):
    small = max(unsorted)
    big = min(unsorted)
    if isEven is True:
        descendingEven()
    elif isEven is False:
        descendingOdd()

print("\n\nSorted list: ", sorted)
print("\n\nPress any key to exit.")
input()
