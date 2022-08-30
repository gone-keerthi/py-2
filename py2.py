word = input('Enter three letter word : ')

result = []
for i in range(len(word)):
    for j in range(len(word)):
        if j==i:
            continue
        for k in range(len(word)):
            if  j==k or i==k:
                continue
            result.append(word[i]+word[j]+word[k])

print('All letter permutations of the PQR are : ')            
print(result)