from math import sqrt
import math, sys, locale, operator
import extra_functions as extra

alphabets = {}
list_alphabets = 'abcdefghijklmnopqrstuvwxyz'
j = 1
lettertonumber = []
for letter in list_alphabets:
	alphabets[letter] = j
	j += 1

primes = []
def is_prime(num):
	global primes
	if num % 2 == 0 or num == 1:
		return False
	if num in primes:
		return True
	is_prime = True
	i = 3
	while is_prime and i <= sqrt(num):
		if num % i == 0:
			is_prime = False
		i = i + 2
	if is_prime:
		primes.append(num)
	return is_prime


# Problem 31
# How many different ways can £2 be made using any number of coins?
def problem31():
	bound = 200
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	curr_count = {}
	for k in range(0, bound+1):
		curr_count[k] = 0
	curr_count[0] = 1
	for i in coins:
		for j in range(i, bound+1):
			curr_count[j] += curr_count[j - i]
	return curr_count[bound]


# Problem 32
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def problem32():
	curr_products = []
	list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	numbers = set(list_of_numbers)
	for i in range(1, 200):
		for j in range(1, 2000):
			curr = ''
			curr_product = i * j
			curr += str(i) + str(j) + str(curr_product)
			curr_set = set(curr)
			if numbers.issubset(curr_set) and (len(curr) == 9) and (curr_product not in curr_products):
				#print(curr, i, j, curr_product)
				curr_products.append(curr_product)
	return sum(curr_products)


# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may 
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and 
# containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
def problem33():
	curr_product = 1
	numerators = []
	denominators = []
	for i in range(10, 99):
		for j in range(10, 99):
			if i % 10 == j // 10 and i != j:
				numerator = float(i // 10)
				denominator = float(j % 10)
				if (denominator != 0) and numerator/denominator == float(i)/float(j):
					# print(numerator, denominator, i, j)
					numerators.append(i)
					denominators.append(j)
					curr_product = curr_product * float(i)/float(j)
	return curr_product


# Problem 34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
def problem34():
	factorials = {}
	digit_factorials = []
	max_sum = 0
	for i in range(0, 10):
		factorials[i] = extra.factorial(i)
		max_sum += factorials[i]
	print(max_sum)
	for j in range(3, max_sum):
		curr_sum = 0
		curr_num = j
		curr_digit = 0
		while curr_num > 0:
			#print(curr_num)
			curr_digit = curr_num % 10
			curr_sum += factorials[curr_digit]
			curr_num = curr_num // 10
		if curr_sum == j:
			digit_factorials.append(j)
	return sum(digit_factorials)


# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# How many circular primes are there below one million?
def problem35():
	bound = 1000000
	circular_primes = [2, 3, 5, 7]
	for i in range(11, bound+1):
		if is_prime(i):
			curr_length = len(str(i))
			curr_num = i
			is_circular = True
			while curr_length > 0 and is_circular:
				curr_digit = curr_num % 10
				curr_num = int(str(curr_digit) + str(curr_num // 10))
				if not is_prime(curr_num):
					is_circular = False
				curr_length -= 1
			if is_circular:
				circular_primes.append(i)
	return len(circular_primes)


# Problem 36
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
def is_palindrome(input_string):
	string_length = len(input_string)
	if string_length == 1:
		return True
	if string_length % 2 == 0:
		for_length = string_length / 2
	else:
		for_length = string_length // 2 + 1
	return_value = True
	for i in range(for_length + 1):
		if input_string[i] != input_string[string_length-1-i]:
			return_value = False
			break;
	return return_value
def problem36():
	bound = 1000000
	double_base = []
	for i in range(1, bound+1):
		if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
			double_base.append(i)
	return sum(double_base)


# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and 
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
def problem37():
	trunc_primes = []
	i = 11
	while len(trunc_primes) != 11:
		if is_prime(i):
			curr_len = len(str(i))
			curr_left = i
			curr_right = i
			left_prime = True
			right_prime = True
			while curr_len > 1 and left_prime:
				test_num = str(curr_left)[1:]
				if test_num[0] == '0':
					break
				#print("left", i, test_num)
				curr_left = int(test_num)
				if not extra.is_prime(curr_left):
					left_prime = False
				curr_len -= 1
			curr_len = len(str(i))
			while left_prime and curr_len > 1 and right_prime:
				test_num = str(curr_right)[:-1]
				#print("right", test_num, i)
				if test_num[0] == '0':
					break
				curr_right = int(test_num)
				curr_len -= 1
				if not extra.is_prime(curr_right):
					right_prime = False
			if left_prime and right_prime:
				trunc_primes.append(i)
				#print(i)
		i += 2
	return sum(trunc_primes)


# Problem 38
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
# concatenated product of an integer with (1,2, ... , n) where n > 1?
def problem38():
	curr_max = 0
	list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	numbers = set(list_of_numbers)
	for i in range(1, 10000):
		curr = ''
		curr_n = 1
		while len(curr) < 9:
			curr += str(i * curr_n)
			curr_n += 1
		if len(curr) == 9:
			curr_set = set(curr)
			if numbers.issubset(curr_set):
				print(i, curr_n, curr)
				if curr_max < int(curr):
					curr_max = int(curr)
	return curr_max


# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
def problem39():
	curr_max = 0
	right_triangles = []
	bound = 1000
	for a in range(1,bound+1):
		for b in range(1,bound/2):
			for c in range(1,bound/3):
				if pow(c,2) + pow(b,2) == pow(a,2):
					right_triangles += [[a,b,c]]
	int_right_triangles = {}
	for triangle in right_triangles:
		curr_sum = sum(triangle)
		if curr_sum not in int_right_triangles.keys():
			int_right_triangles[sum(triangle)] = 1
		else:
			int_right_triangles[sum(triangle)] += 1
	return max(int_right_triangles.iteritems(), key=operator.itemgetter(1))[0]


# Problem 40
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
def problem40():
	parts = [1, 10, 100, 1000, 10000, 100000, 1000000]
	curr = ''
	for i in range(1, 1000000):
		curr += str(i)
	curr_product = 1
	for i in parts:
		curr_product *= int(curr[i-1])
	return curr_product


# Problem 41
# What is the largest n-digit pandigital prime that exists?
def problem41():
	curr_max = 7654321
	list_of_numbers = ['1', '2', '3', '4', '5', '6', '7']
	numbers = set(list_of_numbers)
	while not is_prime(curr_max):
		curr_max -= 2
		while not numbers.issubset(set(str(curr_max))):
			curr_max -= 2
	return curr_max


# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = 0.5*n(n+1)
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these 
# values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
def problem42():
	triange_numbers = []
	count = 0
	for i in range(1, 27):
		triange_numbers.append((i)*(i+1)/2)
	list_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alphabet_dictionary = {}
	i = 1
	for alphabet in list_alphabets:
		alphabet_dictionary[alphabet] = i
		i += 1
	words = open("problem42.txt", "r").read().split('","')
	words[0] = words[0][1:]
	words[-1] = words[-1][:-1]
	for word in words:
		curr_sum = 0
		for letter in word:
			curr_sum += alphabet_dictionary[letter]
		if curr_sum in triange_numbers:
			count += 1
	return count


# Problem 43
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
def problem43():
	pandigital_nums = []
	i = 9876543210
	list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	the_multiples = [2, 3, 5, 7, 11, 13, 17]
	numbers = set(list_of_numbers)
	multiples = {}
	differences = {"d7_10" : [], "d6_9" : [], "d5_8" : [], "d4_7" : [], "d3_6" : [], "d2_5" : []}
	one_up = {"d6_9": ("d7_10", 3, 11, 4, 5), "d5_8": ("d6_9", 4, 7, 5, 6), "d4_7": ("d5_8", 5, 5, 6, 7) , 
		"d3_6": ("d4_7", 6, 3, 7, 8) , "d2_5": ("d3_6", 7, 2, 8, 9)}
	differences_order = ["d7_10", "d6_9", "d5_8", "d4_7", "d3_6", "d2_5"]
	for i in the_multiples:
		multiples[i] = []
	for i in range(1, 1000):
		for j in the_multiples:
			if i % j == 0:
				multiples[j].append(i)
	for difference in differences_order:
		if difference == "d7_10":
			for curr in multiples[17]:
				if len(str(curr)) == 2:
					curr_str = '0' + str(curr)
				else:
					curr_str = str(curr)
				for curr1 in multiples[13]:
					if len(str(curr1)) == 2:
						curr_str1 = '0' + str(curr1)
					else:
						curr_str1 = str(curr1)
					if curr_str1[1:] == curr_str[:-1]:
						test_num = int(curr_str1 + curr_str[-1])
						if len(str(test_num)) == 3:
							if len(set(str(test_num))) == 3:
								differences["d7_10"].append(test_num)
						elif len(set(str(test_num))) == 4:
							differences["d7_10"].append(test_num)
		else:
			info = one_up[difference]
			# print(info)
			for curr in differences[info[0]]:
				if len(str(curr)) == info[1]:
					curr_str = '0' + str(curr)
				else:
					curr_str = str(curr)
				for curr1 in multiples[info[2]]:
					if len(str(curr1)) == 2:
						curr_str1 = '0' + str(curr1)
					else:
						curr_str1 = str(curr1)
					if curr_str[:2] == curr_str1[1:]:
						test_num = int(curr_str1[0] + curr_str)
						if len(str(test_num)) == info[3]:
							if len(set(str(test_num))) == info[3]:
								differences[difference].append(test_num)
						elif len(set(str(test_num))) == info[4]:
							differences[difference].append(test_num)
	second_to_last = []
	# print(differences)
	for curr in differences["d2_5"]:
		if len(set(str(curr))) == 9:
			second_to_last.append(curr)
	curr_sum = 0
	for curr in second_to_last:
		different_int_set = numbers.difference(set(str(curr)))
		for diff_int in different_int_set:
			if diff_int != 0:
				#print(int(diff_int + str(curr)))
				curr_sum += int(diff_int + str(curr))
	# ans = 16695334890
	return curr_sum


def problem44():
	return None

