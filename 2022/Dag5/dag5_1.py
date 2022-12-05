from re import findall

def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def part1():
        raw = openFile()
        count = 0
        # hardcoded input because I don't know how else I would do it, split (on either spaces or tabs) does not seem to work correctly
        # cargo = ["GJWRFTZ", "MWG", "GHNJ", "WNCRJ", "MVQGBSFW", "CWVDTRS", "VGZDCNBH", "CGMNJS", "LDJCWNPG"]
        for i in raw:
                number_count = len(findall("[0-9]", i))
                char_and_number_count = len(findall("[A-Za-z0-9]", i))
                if number_count == char_and_number_count and number_count > 0:
                        cargo = ["" for i in range(int(i.split(" ")[-2]))]
        # cargo = ["NZ", "DCM", "P"]
        start = False
        for i in raw:
                if start:
                        # print(cargo)
                        move = i.split(" ")
                        # print(move[3], move[1], move[5])
                        # print(f"move {cargo[int(move[3]) - 1][0:int(move[1])]} to {cargo[int(move[5]) - 1]}")
                        cargo[int(move[5]) - 1] = cargo[int(move[3]) - 1][0:int(move[1])][::-1] + cargo[int(move[5]) - 1]
                        cargo[int(move[3]) - 1] = cargo[int(move[3]) - 1][int(move[1])::]
                        # print(cargo)
                else:
                        if i != "" and len(findall("[0-9]", i)) == 0:
                                i = i.replace("[", "  ")
                                i = i.replace("]", " ")
                                i = i.rstrip()
                                line = i.split(" ")
                                volgorde = line[::-1]
                                for i in range(0, len(volgorde), 4):
                                        cargo[8 - (i//4)] += volgorde[i]
                                        # print(volgorde[i], end="")
                                # print("\n")
                                # print(i.split(" "))
                                # print(len(i.split(" ")))
                if i == "":
                        start = True

        for i in cargo:
                print(i[0], end="")

part1()
# main()
