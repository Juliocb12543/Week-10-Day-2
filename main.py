# from methods_help import method_help
# from functions import welcome, add_numbers, num_dividedFrom_add_numbers, greet, welcome1, square
#from returnStuff import power, usd_to_eur, reverse_word
#from dynamic_functions import check_3Digits, all_positives
# # method_help()
# #function()
from function_interactions import mix_sticks, try_your_luck, verify_number

# welcome("Julio")
# added = add_numbers(4, 5)
# print(added)
# final = num_dividedFrom_add_numbers(64, added)
# print(final)
# greet()
# welcome1("Julio")
# square1 = square(6)
# print(square1)
# print(power(3,2))
# print(usd_to_eur(300))
# reverse_word()
#sum = 567 + 345
#result = check_3Digits([55, 969, 609, 780, 340, 78, 876, 934, 56, 974])
#print(result)
#result2 = all_positives([10, 45, 9, -9, 6, 46])
#print(result2)
sticks = ["-", "--", "---", "----", "-----"]
my_mix = mix_sticks(sticks)
print(my_mix)

num = try_your_luck()
print(num)

print(verify_number(my_mix, num))