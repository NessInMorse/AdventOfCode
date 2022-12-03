def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        summie = 0
        for i in raw:
                first = set(i[:len(i)//2])
                second = set(i[len(i)//2:])
                # print(first, second)
                score = ord(first.intersection(second).pop())
                if score > 96:
                        score = ord(first.intersection(second).pop()) - 96
                else:
                        score = (ord(first.intersection(second).pop()) - 64) + 26
                summie += score
        print(summie)


main()
