text_file = open("day3_test.txt", "r")

bits_numbers = text_file.read().split('\n')
bits_in_number = len(bits_numbers[0]) 

individual_bits_counters = [0] * bits_in_number 
amount_of_numbers = len(bits_numbers)

oxygen_list = []
O2_list = []

for bits_number in bits_numbers: #part two
    if(bits_number[0] == '1'):
        oxygen_list.append(bits_number)
    elif(bits_number[0] == '0'):
        O2_list.append(bits_number)


for bit_index in range (1, bits_in_number): #from second older bit
    oxygen_ones_counter = 0
    oxygen_zeros_counter = 0
    for bits_number in oxygen_list:
        if(bits_number[bit_index] == '1'): oxygen_ones_counter += 1
        elif(bits_number[bit_index] == '0'): oxygen_zeros_counter += 1
    temp_list = []
    if(len(oxygen_list) == 1): break
    elif(oxygen_ones_counter > oxygen_zeros_counter):
        for bits_number in oxygen_list:
            if(bits_number[bit_index] == '1'): temp_list.append(bits_number)
    elif(oxygen_ones_counter < oxygen_zeros_counter):
        for bits_number in oxygen_list:
            if(bits_number[bit_index] == '0'): temp_list.append(bits_number)
    elif(oxygen_ones_counter == oxygen_zeros_counter):
            if(bits_number[bit_index] == '1'): 
                temp_list.append(bits_number)
                oxygen_list = temp_list
                break
    oxygen_list = temp_list

for bit_index in range (1, bits_in_number): #from second older bit
    o2_ones_counter = 0
    o2_zeros_counter = 0
    for bits_number in O2_list:
        if(bits_number[bit_index] == '1'): o2_ones_counter += 1
        elif(bits_number[bit_index] == '0'): o2_zeros_counter += 1
    temp_list = []
    if(len(O2_list) == 1): break
    elif(o2_ones_counter < o2_zeros_counter):
        for bits_number in O2_list:
            if(bits_number[bit_index] == '1'): temp_list.append(bits_number)
    elif(o2_ones_counter > o2_zeros_counter):
        for bits_number in O2_list:
            if(bits_number[bit_index] == '0'): temp_list.append(bits_number)
    elif(o2_ones_counter == o2_zeros_counter):
            if(bits_number[bit_index] == '0'): 
                temp_list.append(bits_number)
                O2_list = temp_list
                break
    O2_list = temp_list


print("oxygen = ", oxygen_list, "\no2 = ", O2_list)