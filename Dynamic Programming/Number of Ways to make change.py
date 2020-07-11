# Time=(Nd) | Space = o(N)
def NumberOfWaysToMakeChange(n,coins):
    ways=[0 for ammount in range(n+1)]
    ways[0]=1
    for coin in coins:

        for ammount in range(1,n+1):
            
            if coin <= ammount:
                ways[ammount]+=ways[ammount-coin]
    
    return ways[n]

                