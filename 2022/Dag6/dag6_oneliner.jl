println((open("input.txt", "r") |> x -> readlines(x) .|> x -> [length(Set(x[j:minimum((j + 3, length(x)))])) == 4  for j ∈ 1:length(x)] |> x -> [x[i] == 1 ? (i + 3) : 99999999  for i ∈ 1:length(x)] |> minimum)[1])
println((open("input.txt", "r") |> x -> readlines(x) .|> x -> [length(Set(x[j:minimum((j + 13, length(x)))])) == 14  for j ∈ 1:length(x)] |> x -> [x[i] == 1 ? (i + 13) : 99999999  for i ∈ 1:length(x)] |> minimum)[1])
