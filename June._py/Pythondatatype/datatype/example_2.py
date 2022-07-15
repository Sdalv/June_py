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

def highest_number():
	numbers = [21, 14, 72, 148, 54]
	max = numbers[0]
	for i in range(1,len(numbers)-1):
		if(numbers[i]>max):
			max=numbers[i]

	return max

print(highest_number())

# scores = [21, 14, 72, 148, 54]
# top_score = higest_number(scores)
# print(top_score)