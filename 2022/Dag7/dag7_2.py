from re import findall

def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw

def part2():
        raw = openFile()


        directory_string = ""
        all_directories = {}
        for i in raw:
                if i.startswith("$ cd") and i != "$ cd .." and i.split(" ")[-1]:
                        map_name = i.split(" ")[-1]
                        if map_name != "/":
                                directory_string += f"{map_name}/"
                        else:
                                directory_string += f"{map_name}"
                        all_directories[directory_string] = 0
                elif i == "$ cd ..":
                        directory_string = '/'.join(directory_string.split("/")[:-2]) + "/"
                else:
                        if len(findall("[0-9]", i)) > 0:
                                all_directories[directory_string] += int(i.split(" ")[0])

        count_back = max([len(findall("/", i)) for i in all_directories])

        for i in range(count_back, -1, -1):
                for j in all_directories:
                        if len(findall("/", j)) == i:
                                for x in all_directories:
                                        if x.startswith(j) and len(findall("/", x)) == i + 1 and x != j:
                                                all_directories[j] += all_directories[x]
        total_space = 70_000_000
        used_space = all_directories['/']
        unused_space_required = 30_000_000
        options = []
        for i in all_directories:
                if (total_space - (used_space - all_directories[i])) > unused_space_required:
                        options.append(all_directories[i])
        print(min(options))

part2()
