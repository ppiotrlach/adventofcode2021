text_file = open("day2.txt", "r")

commands = text_file.read().split('\n')

horizontal_value = 0 #forward
depth_value = 0      #up, down

# up,down,forward

for i in commands:
    if("forward" in i):
        horizontal_value += int(i[-1])
    elif("up" in i):
         depth_value -= int(i[-1])
    elif("down" in i):
         depth_value += int(i[-1])

print(horizontal_value, " * ",depth_value, " = ", depth_value*horizontal_value)


