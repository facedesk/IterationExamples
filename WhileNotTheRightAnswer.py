'''
Ask a student how they are doing today.
Until they respond with an answer we decide in class,
Keep asking
'''


mood = raw_input("How are you doing today?")
if(mood == ""):
	print("thats the right answer!")
else:
	print("thats the wrong answer!")