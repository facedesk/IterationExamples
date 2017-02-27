'''
Ask a student how they are doing today.
Until they respond with an answer we decide in class,
keep asking
'''

mood = raw_input("How are you doing today?")
while(mood != "Overheated" and mood != "overheated" and mood != "OVERHEATED"):
    print("that's the wrong answer")
    mood = raw_input("How are you doing today?")
print("that's the right answer")

