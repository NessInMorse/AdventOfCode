function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end

function main()
        raw = openFile()
        data = [parse(Int, raw[1])]
        for i ∈ eachindex(raw[2:end])
                i = i + 1
                if raw[i] != ""
                        data[end] += parse(Int, raw[i])
                else
                        append!(data, 0)
                end
        end
        s = sort!(data)
        println(s[end])
        println(s[end] + s[end-1] + s[end-2])
end

main()
