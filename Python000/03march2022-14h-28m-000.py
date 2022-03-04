num_str = input("Input an integer (0 terminates):")
num_int=int(num_str)
even_count=0
odd_count=0
even_sum=0
odd_sum=0 
total = even_count + odd_count

while num_int !=0:
    num_str = input("Input an integer (0 terminates):")
    num_int=int(num_str)
    if num_int < 0:
        num_str = input("Input an integer greater than 0.")
    for num_int in num_str:
        num_int = int(num_str)

        if num_int % 2 == 0 and not num_int == 3 and not num_int == 0: 
            even_count += 1
            even_sum = even_sum + num_int
        elif not num_int == 0: 
            odd_count +=1
            odd_sum = odd_sum + num_int
    total = even_count + odd_count

print("")
print("Sum of odds:", odd_sum)
print("Sum of evens:", even_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Total positive int count:", total)