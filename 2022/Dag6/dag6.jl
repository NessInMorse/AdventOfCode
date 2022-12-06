function  openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end


function part1()
        raw = openFile()
        s = 0
        for i in raw
                found = false
                for j in enumerate(i)
                        if length(Set(i[j[1]:j[1]+3])) == 4 && !found
                                s += j[1] + 3
                                found = true
                                break
                        end
                end
        end
        return s
end


function part2()
        raw = openFile()
        s = 0
        for i in raw
                found = false
                for j in enumerate(i)
                        if length(Set(i[j[1]:j[1]+13])) == 14 && !found
                                s += j[1] + 13
                                found = true
                                break
                        end
                end
        end
        return s
end    





println(part1())
println(part2())
