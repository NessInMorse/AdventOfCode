def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        a = ["A", "B", "C"]
        b = ["X", "Y", "Z"]


        # X lose
        # Y draw
        # Z win

        bonus = [0, 3, 6]

        score = 0
        for inp in raw:
                i = inp.split(" ")
                second = 0
                if i[1] == "X":
                        second = ((a.index(i[0]) - 1) + 3) % 3
                elif i[1] == "Y":
                        second = a.index(i[0])
                elif i[1] == "Z":
                        second = ((a.index(i[0]) + 1) + 3) % 3
                print(second + 1, bonus[b.index(i[1])])
                score += bonus[b.index(i[1])] + second + 1
        print(score)



main()
