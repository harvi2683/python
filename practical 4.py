runner_up=[]
n=int(input())

for i in range(0,n):
    item=int(input())
    runner_up.append(item)

print(runner_up)
runner_up.sort()
runner_up.reverse()
print(runner_up)
print(runner_up[2])