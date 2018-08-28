""" Directions: This script is totally broken.  Your job is to fix it!

1)  The text you're currently reading is a (multiline) comment.  Single-line
    comments begun with the hash character `#`.
    While you're working on fixing one part of this file, you can surround
    the rest of this file with these triple quotes.  That will allow you to
    focus on one thing at once.

2) The comments beginning with TODO contain the instructions you need.

"""
import random
import math

#### Part A:
# TODO: This part should sum up all the even integers less than 200
# that are divisible by 3 but not 27.
output = 0
for i in range(200):
    # do something!

assert output == 3042 # Don't tweak this!


#### Part B:
# TODO: based on your understanding of flow control, add the proper
# indentation to make this code run.  Then tweak FACTOR to make the
# assertion pass.

FACTOR = 1.0 # TODO: After above, change only this to make the assert pass

def monte_carlo_pi(count = 100000):
def sample():
x = 2*random.random()-1
y = 2*random.random()-1
return x**2 + y**2 < 1
num_in = 0
for i in range(count):
if sample():
num_in += 1
return FACTOR*num_in/count

assert abs(monte_carlo_pi() - math.pi) < .05

##### Part C: The output from this section should be:
# Testing break versus continue:
# break outputs: 0 1 2 3
# continue outputs: 0_1_2_3_5_6_7_8
##### TODO: Your tasks:
##### 1) Add correct whitespace to make the code run without error.
##### 2) Change the stopping_number, skipped_number, and endpoint accordingly
##### 3) Change the `sep` and `end` keyword arguments of the print function
#####    to make it print correctly
##### 4) Making sure the final `_` is not present can be completed by adding
#####    an `if-else` statement, or that can be done in-line (look up "python
#####    ternary conditional operator")
stopping_number = 2 # fix me!
skipped_number = 6 # fix me!
endpoint = 15 # fix me!

print("Testing break versus continue:")
print("break", "outputs:", sep="TOTALLY", end='BROKEN')
for i in range(endpoint):
if i == stopping_number:
break
print(i)

# Note that we add a newline character here to make it skip a line.
# We could have alternatively added this line beforehand:
# print()
print("\ncontinue outputs: ")
for i in range(endpoint):
if i == skipped_number:
continue
print(i)
