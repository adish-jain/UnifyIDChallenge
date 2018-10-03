#UnifyID Full Stack Engineering Internship Coding Challenge
#Author: Adish Jain
#Date: Wednesday, October 3rd, 2018

#Reference 1: http://paulbourke.net/dataformats/bitmaps/
#Reference 2: https://www.random.org/clients/http/

import requests
import numpy as np
import matplotlib.pyplot as plt

'''
get_random is a function which uses random.org's HTTP API to generate random values and store them in request.
Parameters:
    num - the number of integers requested
    _min - the smallest value allowed for each integer
    _max - the largest value allowed for each integer
Return:
    A flat array containing all the random values generated from our request.
'''
def get_random(num, _min, _max):
    # Our specifications for random number generation
    myDict = {
        'num': str(num),
        'min': str(_min),
        'max': str(_max),
        'col': '1',
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }
    request = requests.get('https://www.random.org/integers/', params=myDict)

    # For error-handling
    if request.status_code != 200:
        print('Could not request bits due to a ' + str(request.status_code) + ' error')
        exit()

    # Return randomly generated values in a flat array
    return np.asarray([int(x) for x in request.text.split()])

min_val, max_val = 0, 256 ** 3 - 1  # Max value is 256 * 256 * 256 (Reference 1)
x, y = 128, 128

# Plotting our RGB bitmap
bit_map = get_random(x * y / 2, min_val, max_val)
bit_map = np.append(bit_map, get_random(x * y / 2, min_val, max_val))
bit_map = bit_map.reshape(x, y)
fig = plt.imshow(bit_map)
plt.show()
