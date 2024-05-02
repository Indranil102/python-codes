w= "Welcome back to Pycharm"

#find the length of string
t=len(w)
print(t)

for a in range(t):
    print(w[a]) # here [a] is showing the index of string
'''
# reverse iteration
w=w[-1::-1]
for b in range(t):
    print(w[b])

'''
print(" reverse ")

for a in range (t-1,-1,-1):  # iteration for reverse a string 
    print(w[a])