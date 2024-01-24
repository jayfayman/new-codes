# run = int(input("Enter the number of runners you want to enter: "))
# runners = []
# for i in range (0,run):
#     runner = int(input(f"Enter the score of {i+1} runner: "))
#     runners.append(runner)

# #print (runners)
# winner = max(runners)
# new_list = [x for x in runners if x < winner]
# new_list.sort()
# runnerup = max(new_list)
# print (runnerup)
# #print(runners[runnerup])

############################
n = int(input())
arr = map(int, input().split())
runners = list(map(int, arr))
winner = max(runners)
new_list = [x for x in runners if x < winner]
new_list.sort()
runnerup = max(new_list)
print (runnerup)
