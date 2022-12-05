def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        count = 0
        # hardcoded input because I don't know how else I would do it, split (on either spaces or tabs) does not seem to work correctly
        cargo = ["GJWRFTZ", "MWG", "GHNJ", "WNCRJ", "MVQGBSFW", "CWVDTRS", "VGZDCNBH", "CGMNJS", "LDJCWNPG"]
        # cargo = ["NZ", "DCM", "P"]
        start = False
        for i in raw:
                if start:
                        move = i.split(" ")
                        print(move[3], move[1], move[5])
                        print(f"move {cargo[int(move[3]) - 1][0:int(move[1])]} to {cargo[int(move[5]) - 1]}")
                        cargo[int(move[5]) - 1] = cargo[int(move[3]) - 1][0:int(move[1])] + cargo[int(move[5]) - 1]
                        cargo[int(move[3]) - 1] = cargo[int(move[3]) - 1][int(move[1])::]
                        print(cargo)


                if i == "":
                        start = True

        for i in cargo:
                print(i[0], end="")

                


main()
