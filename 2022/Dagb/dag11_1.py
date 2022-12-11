from re import findall

def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw

def main():
        raw = openFile()

        monkeycount = 0
        items_list = []
        # test_operation = [["*", 19], ["+", 6], ["*", "itself"], ["+", 3]]
        # test_operation = [["*",2], ["*", 13], ["+", 5], ["+", 6], ["+", 1], ["+", 4], ["+", 2], ["*", "itself"]]
        test_operation = []
        testvalues = []
        throws_to = []
        check_counter = []
        for i in raw:
                if i.startswith("Monkey"):
                        monkeycount += 1
                        items_list.append([])
                        throws_to.append([])
                        check_counter.append(0)
                        test_operation.append([])
                elif i.lstrip().startswith("Starting items: "):
                        for j in i.split(" ")[4:]:
                                items_list[-1].append(int(''.join(findall("[0-9]", j))))
                elif i.lstrip().startswith("Operation: "):
                        options = i.split(" ")
                        test_operation[-1].append(options[6])
                        if options[7] == "old":
                                test_operation[-1].append("itself")
                        else:
                                test_operation[-1].append(int(options[7]))

                elif i.lstrip().startswith("Test:"):
                        testvalues.append(int(i.split(" ")[-1]))
                elif i.lstrip().startswith("If"):
                        throws_to[-1].append(int(i.split(" ")[-1]))

        # print(items_list)
        # print(testvalues)
        # print(throws_to)
        # print(check_counter)

        
        for i in range(20):
                for j in range(len(items_list)):
                        for _ in range(len(items_list[j])):
                                check_counter[j] += 1
                                if test_operation[j][0] == "*" and test_operation[j][1] == "itself": # x stays 0 anyway, since the items get deleted after iteration
                                        # print(items_list[j][0] * items_list[j][0] // 3)
                                        items_list[j][0] = items_list[j][0] * items_list[j][0]
                                        
                                elif test_operation[j][0] == "*" and type(test_operation[j][1]) == int:
                                        # print(items_list[j][0] * test_operation[j][1] // 3)
                                        items_list[j][0] = items_list[j][0] * test_operation[j][1]
                                        
                                elif test_operation[j][0] == "+" and type(test_operation[j][1]) == int:
                                        # print(items_list[j][0] + test_operation[j][1] // 3)
                                        items_list[j][0] = items_list[j][0] + test_operation[j][1]
                                        
                                elif test_operation[j][0] == "+" and test_operation[j][1] == "itself":
                                        # print(items_list[j][0] + items_list[j][0] // 3)
                                        items_list[j][0] = items_list[j][0] + items_list[j][0]
                                        

                                items_list[j][0] = items_list[j][0] // 3

                                # print("before: ", items_list)
                                if not (items_list[j][0] % testvalues[j]):
                                        items_list[throws_to[j][0]].append(items_list[j][0])
                                        del items_list[j][0]
                                else:
                                        items_list[throws_to[j][1]].append(items_list[j][0])
                                        del items_list[j][0]
                                # print("after: ", items_list)
                                # print("-" * 30)
        worths = sorted(check_counter)[::-1]
        print(worths[0] * worths[1])





main()


"""
Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
"""

"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""




