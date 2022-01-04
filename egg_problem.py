# Lab-2-Variables-Expressions




# 1.1 In this program, prompt the user to enter a whole number.

# 1.2 Print how many full cartons of a dozen eggs would be filled if we pretend that the number represented a number of eggs. For example: 

# input     ->      output
# 2            ->      0 egg cartons full
# 11           ->      0 egg cartons full
# 12           ->      1 egg cartons full
# 50           ->     4 egg cartons full

# 1.3 Print how many eggs would be left over when filling full cartons of a dozen eggs if we pretend that the number number represented a number of eggs. For example:

# input     ->      output
# 2            ->      2 eggs left over 
# 11           ->    11 eggs left over 
# 12           ->    0 eggs left over 
# 50           ->    2 eggs left over 

# You will edit starter file to write the program. You can save and run the tests to check the correctness of the program. 




whole_number = input("Enter a whole number: ") #variable for whole number input
print(whole_number // 12) # prints how many cartons will be filled
print(whole_number % 12) # prints how many eggs are left over
