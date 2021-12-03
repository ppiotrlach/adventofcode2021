
text_file = open("day3.txt", "r")

bits_numbers = text_file.read().split('\n')
bits_in_number = len(bits_numbers[0]) 

individual_bits_counters = [0] * bits_in_number 
amount_of_numbers = len(bits_numbers)


gamma_rate = 0
epsilon_rate = 0

for bits_number in bits_numbers:
    for bit_index in range (0, len(bits_number)):
        if(bits_number[bit_index] == '1'): 
            individual_bits_counters[bit_index] += 1

for bit_index in range (bits_in_number):
    if(individual_bits_counters[bit_index] > amount_of_numbers/2): gamma_rate+= pow(2, bits_in_number - 1 - bit_index)
    else: 
        epsilon_rate+= pow(2, bits_in_number - 1 - bit_index)

print(individual_bits_counters)
print("Gamma rate = ", gamma_rate,"\nEpsilon rate = ", epsilon_rate, "\n Gamma * Epsilon = ", gamma_rate * epsilon_rate)
