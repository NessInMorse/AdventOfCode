def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()

        sum = 0

        subset = set()
        for i in raw:
                subset = set()
                elves = i.split(",")
                s1 = elves[0].split("-")
                s2 = elves[1].split("-")
                a = set([i for i in range(int(s1[0]) - 1, int(s1[1]))])
                b = set([i for i in range(int(s2[0]) - 1, int(s2[1]))])

                for j in a:
                        if j in b:
                                subset.add(j)


                if len(subset):
                        sum += 1

        print(sum)




main()
