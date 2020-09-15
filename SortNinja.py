import time; import os
from colorama import init
from termcolor import colored
import re

unsorted = []; sorted = []

BANNER1 = colored('''
                  ██████  ▒█████   ██▀███  ▄▄▄█████▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                ▒██    ▒ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                ░ ▓██▄   ▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                  ▒   ██▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                ▒██████▒▒░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                ░ ░▒  ░ ░  ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                ░  ░  ░  ░ ░ ░ ▒    ░░   ░   ░         ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                      ░      ░ ░     ░                       ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                                SortNinja: The Double Edged Sorting Algorithm''', 'red')
BANNER3 = colored('''                               -----------------------------------------------''', 'blue')


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)


def ascending(indexFirst, indexLast):
    print("\nWorking...", end='')

    small = min(unsorted); big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, small), sorted.insert(indexLast, big)
        unsorted.remove(small), unsorted.remove(big)

        if (len(unsorted) >= 1):
            small = min(unsorted); big = max(unsorted)
            indexFirst += 1; indexLast += 1

    if (len(unsorted) >= 1):
        sorted.insert(indexFirst, unsorted[0])
    return sorted


def descending(indexFirst, indexLast):
    print("\nWorking...", end='')

    small = min(unsorted); big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, big), sorted.insert(indexLast, small)
        unsorted.remove(big), unsorted.remove(small)

        if (len(unsorted) >= 1):
            small = min(unsorted); big = max(unsorted)
            indexFirst += 1; indexLast += 1

    if (len(unsorted) >= 1):
        sorted.insert(indexFirst, unsorted[0])
    return sorted


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


def outputFile():
        try:
            outputMatch = re.search(r"(.+)[$\.].+", filePath)
            output = str(outputMatch[1])
            extensionMatch = re.search(r".+[$\.](.+)", filePath)
            extension = str(extensionMatch[1])
        except:
            output = filePath
            extension = ""

        output += " [Sorted]." + extension

        with open(output, "w") as file:
            for line in sorted:
                file.write(str(line) + "\n")
        print(f"\n\nGenerated \"{output}\" with sorted elements.")


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (True):
        print("\nMethods:-")
        print("1. Manual entry of integers\n2. Supply a number list file")
        method = input("\nSelect method number: ")
        if (method == "1"):
            while (True):
                try:
                    unsorted = list(map(int, input("\nEnter integers to sort (separated by spaces): ").split()))
                except ValueError:
                    clrscr()
                    print("\nInvalid character(s) entered. Enter only integers. Try again.\n")
                    continue
                break
            break

        elif (method == "2"):
            unsorted = []

            while (True):
                filePath = input("\nEnter file path here: ")

                if (os.path.exists(filePath) is True):
                    with open(filePath, "r") as file:
                        for number in file:
                            unsorted.append(int(number))
                        if (len(unsorted) != 0):
                            break
                        else:
                            clrscr()
                            print("\nSpecified file is empty. Try again.\n")
                            continue

                else:
                    clrscr()
                    print("\nEither file does not exist or invalid path entered. Try again.\n")
                    continue
        else:
            clrscr()
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue

    iterations = (len(unsorted) // 2)
    indexFirst = 0
    indexLast = indexFirst + 1

    while (True):
        print("\nOrder:-")
        print("1. Ascending\n2. Descending")
        ascdesc = input("\nSelect order number (Default = Ascending): ") or "1"

        start = time.time()

        if (ascdesc == "1"):
            clrscr()
            sorted = ascending(indexFirst, indexLast)
            break

        elif (ascdesc == "2"):
            clrscr()
            sorted = descending(indexFirst, indexLast)
            break

        else:
            clrscr()
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue

    completionTime = time.time() - start

    if (method == "1"):
        clrscr()
        print(f"\n\nSorted elements: {sorted}")
    elif(method == "2"):
        outputFile()

    try:
        rate = iterations // completionTime
        print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} accesses/sec)")
        print("Press Enter to exit.")
        input()
    except ZeroDivisionError:
        print("\n\nThe task completed successfully in zero seconds.")
        print("Press Enter to exit.")
        input()
