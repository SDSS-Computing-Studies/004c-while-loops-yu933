#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
i = 1
j = 1
print("1", end =" ", flush=True)
print("1", end =" ", flush=True)
k = i + j
while k <= 100:
   print(k, end =" ", flush=True)
   i = j
   j = k
   k = i + j
print(k, end ="", flush=True)