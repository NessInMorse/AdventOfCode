def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        summie = 0
        teller = 0
        lis = []
        for i in raw:
                if ((teller + 1) % 3) == 0:
                        lis.append(i)
                        if lis:
                                overlap = set(lis[0]).intersection(set(lis[1])).intersection(set(lis[2])).pop()
                                print(overlap)
                                items = ord(set(lis[0]).intersection(set(lis[1])).intersection(set(lis[2])).pop())
                                if items > 96:
                                        score = items - 96
                                else:
                                        score = (items - 64) + 26
                                summie += score
                        lis = []
                else:
                        lis.append(i)

                teller += 1
        print(summie)


main()
