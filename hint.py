import random
from rand_num import first, second, generate_number
hnt = list(range(0, 7))
random.shuffle(hnt)
def get_hint():

    number = generate_number()

#determines if the first number of the combination is odd or even
    if first & 1 == 0:
        first_eo = "even"
    else:
        first_eo = "odd"


#determines if the second number of the combination is odd or even
    if second & 1 == 0:
        second_eo = "even"
    else:
        second_eo = "odd"


# Varies how close the numbers are on "number is between x and y"
    num_variation_low = number - random.randint(1 , 10)
    num_variation_high = number + random.randint(1 , 10)
    

#sets the numbers for the "first/second number os x, y, or z"
    first_span = ((first - 1), first, (first +1))
    if first == 0:
        first_span = (1, 2, 3)
    if first == 9:
        first_span = (7, 8 ,9)
    if first > 0 and first < 9:
        rndf = random.randint(-1, 1)
        for i in first_span:
            i += rndf
    
    second_span = ((second - 1), second, (second +1))
    if second == 0:
        second_span = (0, 1, 2)
    if second == 9:
        second_span = (7, 8 ,9)
    if second > 0 and second < 9:
        rnds = random.randint(-1, 1)
        for i in second_span:
            i += rnds


    hint_list = [ 
        f"You get the feeling that one of the numbers is {first}.", 

        f"You get the feeling that one of the numbers is {second}.",
        
        f"You get the feeling that the number is greater than {num_variation_low} and less than {num_variation_high}",

        f"You get the feeling that the first number is {first_eo}.",

        f"You get the feeling that the second number is {second_eo}.",

        f"You get the feeling that the first number is a {first_span[0]}, {first_span[1]}, or {first_span[2]}.",

        f"You get the feeling that the second number is a {second_span[0]}, {second_span[1]}, or {second_span[2]}"

    ]

    hnt_num = hnt.pop()
    print(hint_list[hnt_num])
    
    print(f"debugging:{first} and {second} ")
    print("")