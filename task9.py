
from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = sum(1 for char in self.data if char.isdigit())
        return count

res = NumberString('6767cd676no8p')
print(res.number_count())      
           
                
# import re

# def calculate_numbers_in_string(string):
#     numbers = re.findall(r'\d+', string)
    
#     concatenated_numbers = ''.join(numbers)
    
#     count = len(concatenated_numbers)
    
#     return count

# string = "ddk434hb34knbkc9887bh"
# print(calculate_numbers_in_string(string))


'''another way'''
# def calculate_numbers_in_string(string):
#     count = 0

#     for char in string:
#         if char.isdigit():
#             count += 1

#     return count

# string = "ddk43h3443434b34knbkc9887bh"
# print(calculate_numbers_in_string(string))
