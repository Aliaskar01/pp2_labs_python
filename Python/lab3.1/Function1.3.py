def solve(numheads, numlegs):
    rabbit = (numlegs - 2 * numheads) / 2 
    chicken  = numheads - rabbit
    return chicken, rabbit

numheads = 35
numlegs = 94

print(solve(numheads, numlegs))