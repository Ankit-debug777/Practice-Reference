#For this task, you will write two validators.
#Shift Validator: When each element is translated (added or subtracted) by a constant.
#Multiple Validator: When each element is multiplied (by a positive or negative number) by a constant.
#is_shifted([1, 2, 3], [2, 3, 4]) ➞ True
# Each element is shifted +1
is_shifted([1, 2, 3], [-9, -8, -7]) ➞ True
# Each element is shifted -10
is_multiplied([1, 2, 3], [10, 20, 30]) ➞ True
# Each element is multiplied by 10
is_multiplied([1, 2, 3], [-0.5, -1, -1.5]) ➞ True
# Each element is multiplied by -1/2
is_multiplied([1, 2, 3], [0, 0, 0]) ➞ True
# Each element is multiplied by 0
def is_shifted(lst1, lst2):
	diff = set()
	for x,y in zip(lst1,lst2):
		a = y-x
		diff.add(a)
	return len(diff)==1
def is_multiplied(lst1, lst2):
	mul = set()
	for x,y in zip(lst1,lst2):
		z = float(y)/x
		mul.add(z)
	return len(mul)==1
