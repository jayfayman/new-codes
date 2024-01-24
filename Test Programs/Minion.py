def minion_game(inp_string):
    stuart_score = 0
    kevin_score = 0
    #i=1
    for i in range(len(inp_string)+1):
        for j in range(i):
            sub_str = inp_string[j:i]
            print(sub_str)
            if sub_str[0] in ('A', 'E', 'I', 'O', 'U'):
                kevin_score+=1
            else:
                stuart_score+=1
    if (kevin_score>stuart_score):
        print(f"Kevin {kevin_score}")
    elif (kevin_score<stuart_score):
        print (f"Stuart {stuart_score}")
    else:
        print("Draw")

input_string = input ("Enter the string that you want to play with: ")
minion_game(input_string.upper())