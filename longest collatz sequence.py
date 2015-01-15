# -*- coding: utf-8 -*-
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Created on Thu Jan 15 00:47:40 2015
@author: Richard Decal, decal@uw.edu
"""

#==============================================================================
# iter up to 1M
# for number, start doing collatz, keeping a counter. if running collatz number in
# chain_lengths, look up it's length and add it to the counter, then add number, chain_len to dict
#==============================================================================

iter_ceiling = 13

chain_lengths = {1:1}

def collatz_step(number):
    if number == 1:
        print "poop!"
    if number%2 == 0:
        return number/2
    else:
        return 3*number + 1

def collatzer():
    for number in range(2,iter_ceiling+1):
        counter = 1
        running_collatz_number = number
        print "STARTING NUMBER " + str(running_collatz_number) + " with count " + str(counter)
        while running_collatz_number > 1:
            if running_collatz_number in chain_lengths.keys(): #we've done this before
                print "found " + str(running_collatz_number) + "! adding it's chain length, " + str(chain_lengths.get(running_collatz_number))             
                counter += chain_lengths.get(running_collatz_number)
                print "final count for " + str(number) + " is " + str(counter)
                chain_lengths[number] = counter
                running_collatz_number = 0 #end this loop
            else:
                running_collatz_number = collatz_step(running_collatz_number)
                counter += 1
                print "counter " +str(counter) + " number "+ str(running_collatz_number)
                if running_collatz_number == 1:
                    chain_lengths[number] = counter
                    print "final count for " + str(number) + " is " + str(counter)
        
collatzer()