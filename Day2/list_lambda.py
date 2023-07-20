
# Comprohensive list 

# friends = ["Mohini", "Mohina", "Mamta", "Priya", "Priyanka"]
# friends_M = [friend for friend in friends if friend.startswith('M')]
# print(friends_M)

# Lambda in Python

# add = (lambda x , y : x + y)
# print(add(2,10))

def double(x):
    return x * 2

sequence = [1,2,3,4]
doubled = [(lambda x: x * 2 )(x) for x in sequence]                  # map(double, sequence)              # [double(x) for x in sequence]

print(doubled)
