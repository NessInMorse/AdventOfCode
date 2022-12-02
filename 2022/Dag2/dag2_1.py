def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        a = ["A", "B", "C"]
        b = ["X", "Y", "Z"]

        bonus = [3, 0, 6]

        score = 0
        for inp in raw:
                i = inp.split(" ")
                print(bonus[(a.index(i[0]) - b.index(i[1]) + 3) % 3] + b.index(i[1]))
                score += bonus[(a.index(i[0]) - b.index(i[1]) + 3) % 3] + (b.index(i[1]) + 1)
        print(score)



main()
