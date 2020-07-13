import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for random_number in my_randoms:
        
        
    # Does my_randoms contain number? Change the boolean.
        if random_number == number:
            the_numbers_match = True

    if the_numbers_match == True:
        print(f'my_randoms list contains {number}')
    else:
        print(f'my_randoms list does not contain {number}')
            

    # print(f'{number} is in the random list')
    