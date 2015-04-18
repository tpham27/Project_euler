import math


def is_prime(num):
	is_prime = True
	if num % 2 == 0 or num == 1:
		return False
	i = 3
	while is_prime and i <= math.sqrt(num):
		if num % i == 0:
			is_prime = False
		i = i + 2
	return is_prime

def sum_proper_divisors(num):
	count = 0
	if num == 1:
		return 1
	if pow(int(sqrt(num)),2) == num:
		for i in range(1, int(sqrt(num))):
			if num % i == 0:
				count += i
				count += num / i
		count += int(sqrt(num))
	else:
		for i in range(1, int(sqrt(num))+1):
			if num % i == 0:
				count += i
				count += num / i
	count = count - num
	return count

def sum_divisors(num):
	count = 0
	if num == 1:
		return 1
	for i in range(1, int(math.ceil(sqrt(num)))):
		if num % i == 0:
			count += i
			count += num / i
	return count

def factorial(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return n * factorial(n-1)

def n_choose_k(n, k):
	return (factorial(n)) / (factorial(k) * factorial(n - k))

def num_divisors(num):
	count = 0
	if num == 1:
		return 1
	for i in range(1, int(math.ceil(sqrt(num)))):
		if num % i == 0:
			count += 2
	return count

def sum_digits(num):
	curr_sum = 0
	while num > 0:
		digit = int(num % 10)
		num = int(num // 10)
		curr_sum += digit
	return curr_sum