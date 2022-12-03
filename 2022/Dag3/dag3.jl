function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end

function part1()
        raw = openFile()
        summie = 0
        pre_codepoint_lower = codepoint('a') - 1
        pre_codepoint_upper = codepoint('A') - 1
        alphabet_length = 26
        for i in raw
                first = Set(i[begin:length(i) ÷ 2])
                second = Set(i[length(i) ÷ 2 + 1:end])
                overlap = pop!(intersect(first, second))

                score = codepoint(overlap)
                if score > pre_codepoint_lower
                        score = score - pre_codepoint_lower
                else
                        score = score - pre_codepoint_upper + alphabet_length
                end
                summie += score
        end
        return summie
end

function part2()
        raw = openFile()
        summie = 0
        teller = 0
        lis = []
        pre_codepoint_lower = codepoint('a') - 1
        pre_codepoint_upper = codepoint('A') - 1
        alphabet_length = 26

        for i in raw
                if ((teller + 1) % 3) == 0
                        push!(lis, i)
                        overlap = intersect(Set(lis[1]), Set(lis[2]), Set(lis[3]))
                        score = codepoint(pop!(overlap))
                        if score > pre_codepoint_lower
                                score = score - pre_codepoint_lower
                        else
                                score = (score - pre_codepoint_upper) + alphabet_length
                        end
                        summie += score
                        lis = []
                else
                        push!(lis, i)
                end

                teller += 1
        end
        return summie
end


println(part1())
println(part2())
