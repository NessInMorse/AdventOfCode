def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()

        sum = 0
        for i in raw:
                elves = i.split(",")
                s1 = elves[0].split("-")
                s2 = elves[1].split("-")
                a = [i for i in range(int(s1[0]) - 1, int(s1[1]))]
                b = [i for i in range(int(s2[0]) - 1, int(s2[1]))]

                if min(b) in a and max(b) in a or min(a) in b and max(a) in b:
                        sum += 1
        print(sum)




main()
