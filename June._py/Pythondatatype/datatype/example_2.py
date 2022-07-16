# import turtle
# my_turtle = turtle.Turtle()
# my_turtle.speed(0)

# def square(length, angle):
# 	for i in range(20):
# 		my_turtle.forward(length)
# 		my_turtle.left(angle)

# square(101, 100)
# turtle.done()

# def add(a,b):
# 	results = a + b
# 	return results

# sum = add(2,3)
# print(sum)

# def highest_number():
# 	numbers = [21, 14, 72, 148, 54]
# 	max_number = numbers[0]
# 	for i in range(1,len(numbers)-1):
# 		if(numbers[i]>max_number):
# 			max_number=numbers[i]

# 	return max_number

# print(highest_number())

# scores = [21, 14, 72, 148, 54]
# top_score = higest_number(scores)
# print(top_score)

my_list = [21, 14, 72, 148, 54]
result = None

def max_number(arg_list):
	result = None
	for i in my_list:
		if result is None or i > result:
			result = i
	return result
print(max_number(my_list))

# for i in my_list:
# 	if i > my_list[0]:
# 		result = i
# 		print(type(result))

	# print(i)

