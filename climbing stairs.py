def climbStairs(x):
    one,two=1,1
    for i in range(x-1):
        temp=one
        one=one+two
        two=temp
    return one
z=int(input())
y=climbStairs(z)
print(y)

