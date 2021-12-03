text_file = open("day2.txt", "r")

commands = text_file.read().split('\n')

horizontal_value = 0 #forward
aim_value = 0        #up, down
depth_value = 0      #up,down,forward

for i in commands:
    if("forward" in i):
        horizontal_value += int(i[-1])
        if(aim_value != 0): 
            depth_value += int(i[-1])*aim_value
    elif("up" in i):
         aim_value -= int(i[-1])
    elif("down" in i):
         aim_value += int(i[-1])

print(horizontal_value, " * ",depth_value, " = ", depth_value*horizontal_value)


