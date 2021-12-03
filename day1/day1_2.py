text_file = open("day1.txt", "r")

string_numbers = text_file.read().split('\n')
numbers = list(map(int,string_numbers))

greater_than_prev_counter = 0
list_length = len(numbers)
for i in range (2, list_length - 1):
    sum1 = numbers[i] + numbers[i - 1] + numbers[i - 2]
    sum2 = numbers[i + 1] + numbers[i] + numbers[i - 1]
    if(sum2 > sum1): greater_than_prev_counter+=1

print(greater_than_prev_counter)