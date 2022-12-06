
def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        s = 0
        for i in raw:
                found = False
                for j in range(0, len(i) - 1):
                        if len(set(i[j:j+4])) == 4 and not found:
                                s += j  + 4
                                found = True
                                break
                                
        print(s)

main()
