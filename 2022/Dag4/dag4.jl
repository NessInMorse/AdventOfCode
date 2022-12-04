function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end


function part1()
        raw = openFile()

        count = 0
        for i in raw
                elves = split(i, ',')
                s1 = split(elves[1], '-')
                s2 = split(elves[2], '-')
                a = parse(Int32, s1[1]):parse(Int32, s1[2])
                b = parse(Int32, s2[1]):parse(Int32, s2[2])
                if issubset(a, b) || issubset(b, a)
                        count += 1
                end
        end
        return count
end

function part2()
        raw = openFile()

        count = 0
        for i in raw
                elves = split(i, ',')
                s1 = split(elves[1], '-')
                s2 = split(elves[2], '-')
                a = parse(Int32, s1[1]):parse(Int32, s1[2])
                b = parse(Int32, s2[1]):parse(Int32, s2[2])

                if any(map(x -> x ∈ b, a))
                        count += 1
                end
        end
        return count
end




println(part1())
println(part2())
