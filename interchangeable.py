#  Take input number from User

input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))

# We are not using 3rd variable

input_num_a = input_num_a + input_num_b
input_num_b = input_num_a - input_num_b
input_num_a = input_num_a - input_num_b

# After change first value is
print("After changing value, first value is =  " + str(input_num_a))

# After change second value is
print("After changing value, second value is =  " + str(input_num_b))