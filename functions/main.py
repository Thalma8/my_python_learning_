# def message():
#     print("Enter a value: ")
# def outputt(number):
#     print("You entered ", number)
#
# message()
# a = int(input())
#
# message()
# b = int(input())
#
# message()
# c = int(input())
#
#
# outputt(a)
# outputt(b)
# outputt(c)
#
#
# def strange_function(n):
#     if (n % 2 == 0):
#         print("it is even")
#         return True
#
#
# print("enter a value to check if it is even")
# n = int(input())
#
# strange_function(n)

def is_year_leap(year):
 if year % 4 != 0:
  return False
 elif year % 100 != 0:
  return True
 elif year % 400 != 0:
  return False
 else:
  return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
