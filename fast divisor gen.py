# -*- coding: utf-8 -*-
"""
code stolen from http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
The overall efficiency of this algorithm will depend entirely on the efficiency of the factorGenerator.

In essence, this algorithm is doing the following:

factors = prime1 ^ 0 * prime2 ^ 0 * ... primeN ^ 0;
          prime1 ^ 0 * prime2 ^ 0 * ... primeN ^ 1;
            ...          ...        ...   ...     ;
          prime2 ^ i * prime2 ^ j * ... primeN ^ k;
Where i, j, and k are the multiplicity of the prime factor. Given n = 100:

# Prime factors are 5, and 2 with a multiplicity of 2 for each

5 ^ 0 * 2 ^ 0 = 1
5 ^ 0 * 2 ^ 1 = 2
5 ^ 0 * 2 ^ 2 = 4
5 ^ 1 * 2 ^ 0 = 5
...
5 ^ 2 * 2 ^ 2 = 100

Created on Fri Jan 16 00:17:07 2015
@author: Richard Decal, decal@uw.edu
"""

def divisorGen(n):
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return