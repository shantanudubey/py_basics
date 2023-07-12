# Date and Time 

import random
import datetime
import time


# Set the seed of the random number generator to use the current time or OS dependent random source(if available) by not setting anything
random.seed()
print("random       :", random.random())
print("random       :", random.random())
print("randint      :", random.randint(10, 100))
print("date         :", datetime.date.today())
print("time         :", datetime.datetime.now(), datetime.datetime.utcnow())
print("Time         :", time.time(), time.timezone)
print('-' * 80)

""" Pseudo Random Number Generator : using seed() to get same result in every execution
    Ref : https://pynative.com/python-random-seed/
"""
seed_value = 6 * time.time()
random.seed(seed_value)
print("random       :", random.random())
print("randint      :", random.randint(10, 50))
print('-' * 80)