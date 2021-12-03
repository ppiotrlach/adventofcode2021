text_file = open("day1.txt", "r")

string_numbers = text_file.read().split('\n')
numbers = list(map(int,string_numbers))

greater_than_prev_counter = 0
for i in range (len(numbers)):
    if (i>0 and numbers[i]>numbers[i-1]):
        greater_than_prev_counter+=1

print(greater_than_prev_counter)


