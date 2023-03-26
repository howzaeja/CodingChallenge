# roman --> decimal
#check each character and the one to the right to see if there's subtraction, otherwise use addition


def convert_rom_dec(num):
    #make a new num because I'm going to take out numbers so I don't add them twice and I want to preserve the original
    new_num = num
    numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    num_vals = [1, 5, 10, 50, 100, 500, 1000]
    curr_val = 0
    next_val = 0
    final_num = 0

    for i in range(len(num)):

        #because 5 and 50 cannot precede any numbers and be used for subtraction, it can have its own case
        if new_num[i] == "V":
            final_num += 5
            break
        if new_num[i] == "L":
            final_num += 50
            break
            
        for j in range(len(numerals)):
            #check to see if character to the right is greater than the current character
            #first convert current character and character to the right to their proper values
            #then make sure the character to the right can be preceded by the current character
            #then subtract the two numbers or add the current number to the final number

            #if the current letter is the same as the letter in the list of numerals, give that letter the proper numerical value
            if new_num[i] == numerals[j]:
                curr_val = num_vals[j]
                break
            #check if the letter to the right is one of the ones the current one can precede
            #if it is, we can do the subtraction
            #if you subtract, you need to skip over the next letter because it's already been taken into account
            #this only works if the string is longer than one
            if len(new_num) > 1:
                if new_num[i+1] == numerals[j+1]:
                    next_val = num_vals[j+1]
                    final_num += (next_val - curr_val)
                    new_num.remove(new_num[i+1])
                elif new_num[i+1] == numerals[j+2]:
                    next_val = num_vals[j+2]
                    final_num += (next_val - curr_val)
                    new_num.remove(new_num[i+1])
            
        #if you can't subtract them, then add the current letter
        final_num += curr_val
                

    print(f'{num} = {final_num}')

convert_rom_dec("X")

# decimal --> roman
#go through each digit using // and % from the ones place up, and convert each digit to roman numerals after


def separate_decimal(num):

#go through each digit
    n = num
    power = 1
    lst_nums = []
    while n != 0:
        k = n % (10 ** power)
        lst_nums.append(k)
        power += 1
        n = n - k
    return lst_nums

#use pattern to make it simpler
def convert_dec_rom(lst):
    numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    num_vals = [1, 5, 10, 50, 100, 500, 1000]
    final_string = ""
    base = 'I'
    tens_place = 0

    #if there are any zeros, we don't want them to be evaluated, or they'll throw the number off
    new_list = [x for x in lst if x != 0]
    new_list = new_list[::-1]
    
    #pattern:
    #check for roman numeral values
    #then check for subraction values
    #then the rest will be the addition values
    
    for i in new_list:
        #the base and tens place variables need to reset with each new item in the list so they represent accurate values
        base = 'I'
        tens_place = 0

        for j in range(len(num_vals)):
            
            #if list element = a roman numeral value: add that roman numeral
            if i == num_vals[j]:
                final_string += numerals[j]
                break
            
            #we only need to check for addition and subtraction values if list element < the current roman numeral value
            #otherwise we can just skip to the next roman numeral value
            elif i < num_vals[j]:
                #if list element = roman numeral value - 1*(the proper tens place): add the proper base and the roman numeral
                if i == num_vals[j] - 10**tens_place:
                    final_string += base + numerals[j]
                    break
                #otherwise: get highest roman numeral less than list element,
                #then add the lower roman numeral to base*(list element - lower roman numeral)
                else:
                    final_string += numerals[j-1] + (base)*((i - num_vals[j-1])//10**tens_place)
                    break
            
            #we need a special case for when list element > 1000 because the largest number they found was 3,999
            elif i > 1000:
                final_string += 'M' * (i // 1000)
                break

            #the base and tens_place need to change every time we go to the next group (ones to tens, tens to hundreds, etc.)
            #first change is after we check if i == 10, or when j = 2
            if j == 2:
                base = 'X'
                tens_place = 1
            #second change is after we check if i == 100, or when j = 4
            elif j == 4:
                base = 'C'
                tens_place = 2
    print(final_string)

convert_dec_rom(separate_decimal(3999))