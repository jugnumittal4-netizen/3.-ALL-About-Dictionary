td = {"codingal":2,"are":2,"fun":2,"and":2,"learning":2,"is":2,"good":1}
print("the orignal dictionary is:", str(td))
k = 2
res = 0
for key in td:
    if td[key] == k:
        res += 1
print("the frequency of",k,"is",res)
      