open System
open System.Collections.Generic

let merge (left : List<int>, right : List<int>) =
  let len = match left.Count with
            | x when x > right.Count -> left.Count
            | x when x <= right.Count -> right.Count
  let mutable i = 0
  let mutable j = 0
  let result = new List<int>()

  while i < left.Count && j < right.Count do
    if left.[i] < right.[j] then 
      result.Add(left.[i])
      i <- i + 1
    else 
      result.Add(right.[j])
      j <- j + 1

  result.AddRange(left.GetRange(i, (left.Count - i)))
  result.AddRange(right.GetRange(j, (right.Count - j)))
  result

let rec mergesort (lst : List<int>) =
  match lst.Count with
  | 0 | 1 -> lst
  | _ ->
    let m = lst.Count / 2
    let b = lst.GetRange(0, m)
    let c = lst.GetRange(m, (lst.Count - m))

    let b = mergesort(b)
    let c = mergesort(c)

    merge(b, c)

let a = [| 0; 6; 5; 13; 3; 1; 8; 15; 7; 2; 4; 10; 14; 12; 9; 11 |]
let lst = new List<int>()

for i in a do
  lst.Add(i)

for i in (mergesort lst) do
  printfn "%d" i
