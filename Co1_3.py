#positive number

numbers =[-10,-15,-16,8,4,9]
positive_number =[num for num in numbers if num >0]
print(positive_number)


#sqaure of n numbers

numbers =[1,2,3,4,5,6,]
square =[x*x for x in numbers]
print("Numbers:",numbers)
print("square:",square)

#list of vowels

word ="computer"
vowels =[ch for ch in word if ch in"aeiou"]
print("Vowels:",vowels)

#list ordinal values of each element of a word 

word ="hello"
ordinal_values=[ord(char)for char in word]
print("Ordinal values:",ordinal_values)