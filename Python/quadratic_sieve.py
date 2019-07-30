# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:29:17 2019

@author: user
"""

#!/usr/bin/python3

# pypy python interpreter is strongly recomended



import math

import sys



# generation of new number: openssl genrsa <bits> | openssl rsa -modulus -noout

N = 3025577890235798683543591

#N = 3025577890235798683543591  # 82 bit

#N = 1822370728996458306753277  # 81 bit

#N = 854626116323831524991473  # 80 bit

#N = 399066586857431823726709  # 79 bit

#N = 235311326942746619548591  # 78 bit

#N = 113576732865342496692451  # 77 bit

#N = 71346986589122957051491  # 76 bit

#N = 32621041168941237031687  # 75 bit

#N = 14838142262537816848201  # 74 bit

#N = 7574625114799379190481  # 73 bit

#N = 3541904643519702945253  # 72 bit

#N = 1753044930908746416511  # 71 bit

#N = 861256316295598761961  # 70 bit

#N = 533595842543374012417  # 69 bit

#N = 200903802201060018373  # 68 bit

#N = 93496418013679648963  # 67 bit

#N = 54570430399383971173  # 66 bit

#N = 27419891463310753159  # 65 bit

#N = 14128513504013581789  # 64 bit

#N = 6357994389398958601  # 63 bit

#N = 3191071089482212003  # 62 bit

#N = 2064846507704311861  # 61 bit

#N = 959125210334783077  # 60 bit

#N = 434686773884327407  # 59 bit

#N = 210491451967849183  # 58 bit

#N = 92092615464081619  # 57 bit

#N = 64157244473449123  # 56 bit

#N = 26408936706025597  # 55 bit

#N = 12096819068999101  # 54 bit

#N = 7875168790028311  # 53 bit

#N = 3207054426926827  # 52 bit

#N = 851821581119671  # 50 bit

#N = 832730084101

#N = 84923



sieving_array_size = 1000000



# uncomment more if not founded

primes = [

    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,

    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,

    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,

    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,

    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,

    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,

    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,

    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,

    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,

    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,

    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,

    1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,

    1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163,

    1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249,

    1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,

    1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439,

    1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,

    1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601,

    1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693,

    1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783,

    1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877,

    1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,

    1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069,

    2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143,

    2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267,

    2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347,

    2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423,

    2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543,

    2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657,

    2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713,

    2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801,

    2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903,

    2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011,

    3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119,

    3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221,

    3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323,

    3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413,

    3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527,

    3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607,

    3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697,

    3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797,

    3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907,

    3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003,

    4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093,

    4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211,

    4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283,

    4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409,

    4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513,

    4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621,

    4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721,

    4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813,

    4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937,

    4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011,

    5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113,

    5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233,

    5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351,

    5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443,

    5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531,

    5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653,

    5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743,

    5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849,

    5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939,

    5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073,

    6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173,

    6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271,

    6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359,

    6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473,

    6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581,

    6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701,

    6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803,

    6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907,

    6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997,

    7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121,

    7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229,

    7237, 7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349,

    7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487,

    7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561,

    7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669,

    7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757,

    7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879,

    7883, 7901, 7907, 7919, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009,

    8011, 8017, 8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111,

    8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, 8221, 8231,

    8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, 8293, 8297, 8311, 8317,

    8329, 8353, 8363, 8369, 8377, 8387, 8389, 8419, 8423, 8429, 8431, 8443,

    8447, 8461, 8467, 8501, 8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573,

    8581, 8597, 8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677,

    8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, 8747, 8753,

    8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, 8837, 8839, 8849, 8861,

    8863, 8867, 8887, 8893, 8923, 8929, 8933, 8941, 8951, 8963, 8969, 8971,

    8999, 9001, 9007, 9011, 9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091,

    9103, 9109, 9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199,

    9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, 9293, 9311,

    9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, 9391, 9397, 9403, 9413,

    9419, 9421, 9431, 9433, 9437, 9439, 9461, 9463, 9467, 9473, 9479, 9491,

    9497, 9511, 9521, 9533, 9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623,

    9629, 9631, 9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733,

    9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, 9817, 9829,

    9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, 9901, 9907, 9923, 9929,

    9931, 9941, 9949, 9967, 9973

]





def get_factor_base(N, primes):

    # return only values for which N is a quadratic residue

    return [prime for prime in primes if N ** ((prime - 1) // 2) % prime == 1]





def tonelli_shanks_algo(n, p):

    """ algo for solving a congruence x * x =* n by module p """



    assert p % 2 == 1



    if n ** ((p - 1) // 2) % p != 1:

        return 0



    Q = p - 1

    S = 0

    while Q % 2 == 0:

        Q //= 2

        S += 1



    #print(" = Q=%d S=%d" % (Q,S))



    # find z such as Legendre symbol (z/p) == -1

    for z in range(2, 100):

        euler_crit = z ** ((p - 1) // 2) % p

        if euler_crit == p - 1:

            break

    else:

        #print(" - z not founded")

        return 0



    c = z ** Q % p

    #print(" = z=%d c=%d" % (z,c))



    R = n ** ((Q + 1) // 2) % p

    t = n ** Q % p

    M = S



    while t != 1:

        for i in range(1, M):

            if t ** (2 ** i) % p == 1:

                break

        else:

            #print(" - i not founded")
            pass

        #print( " = i=%d" % (i))

        b = c ** (2 ** (M - i - 1)) % p

        R = (R * b) % p

        t = (t * b * b) % p

        c = (b * b) % p

        M = i

    return R





def is_smooth(n, factor_base):

    if n == 0:

        return False



    for factor in factor_base:

        while n % factor == 0:

            n = n / factor

    return n == 1





def gen_smooth(factor_base, max_num):

    ret = set({})

    startpoint = int(math.sqrt(N)) - sieving_array_size // 2

    endpoint = startpoint + sieving_array_size



    #print(" = initializing an array for quadratic sieving")

    sieve = [x * x - N for x in range(startpoint, endpoint)]



    #print(sieve)



    for factor in factor_base:

        # tonelli shanks algo doesn't work with factor 2

        if factor == 2:

            # solving x*x=N % 2

            if N % 2 == 0:

                    R_all = [0]

            else:

                R_all = [1]

        else:

            # sqrt_N

            R = tonelli_shanks_algo(N, factor)
            

            assert R != 0

            R_all = [R, factor - R]



        #print(" = factor %d, R_all=%s" % (factor, R_all))



        # R + faktor * k > startpoint

        # faktor * k > startpoint - R

        # k > ( startpoint - R ) // factor



        # R + faktor * k < endpoint



        for R in R_all:

            k_from = (startpoint - R + (factor - 1)) // factor

            k_to = (k_from + (endpoint - (R + factor * k_from) +

                    (factor - 1)) // factor)



            for k in range(k_from, k_to):

                x = (R + factor * k) - startpoint

                #if sieve[x]==0:

                #  continue

                val = x + startpoint



                assert sieve[x] % factor == 0



                #print("s_before[x]=%d, factor=%d"%(sieve[x],factor))

                sieve[x] //= factor

                while(sieve[x] % factor == 0):

                    sieve[x] //= factor



                if sieve[x] == 1 and x != 0:

                    ret.add(val)

                    number = val * val - N

                    assert is_smooth(number, factor_base)

                    #print(" + founded %d" % (len(ret)))

                    sieve[x] = 0

                    if len(ret) > max_num:

                        return list(ret)

    return list(ret)





def generate_vector(n, factor_base):

    ret = []

    for factor in factor_base:

        times = 0

        while n % factor == 0:

            times += 1

            n /= factor

        if times % 2 == 0:

            ret.append(0)

        else:

            ret.append(1)

    return ret





def gcd(x, y):

    #print("gcd %d %d"%(x,y))

    if x < 0:

        x *= -1



    if y < 0:

        y *= -1



    if x < y:

        x, y = y, x



    while x % y != 0:

        x = x % y

        if x < y:

            x, y = y, x

    return y





def identity_matrix(height):

    return [[1 if i == j else 0 for j in range(height)] for i in range(height)]





def find_linear_combination(vector_list):

    height = len(vector_list)

    if height == 0:

        return None



    width = len(vector_list[0])

    if height < width:

        #print(height, width, len(primes))

        #print("failed, insufficient matrix rows. Try to uncomment more primes "          "in source")

        return None



    # for each string: what has been multiplied

    combinations = identity_matrix(height)



    for offset in range(width):

        if vector_list[offset][offset] == 0:

            # check if all

            for x in range(width):

                if vector_list[offset][x] != 0:

                    break

            else:

                # all nulls

                return combinations[offset]

            # find a string to swap

            for y in range(offset + 1, height):

                if vector_list[y][offset] != 0:

                    vector_list[y], vector_list[offset] = vector_list[offset], vector_list[y]

                    combinations[y], combinations[offset] = combinations[offset], combinations[y]

                    break

            else:

                continue  # we didn't find a string to swap



        for y in range(offset + 1, height):

            if vector_list[y][offset] == 0:

                continue

            for x in range(width):

                vector_list[y][x] *= -1

                vector_list[y][x] += vector_list[offset][x]

                vector_list[y][x] %= 2



            # mul vector and sum two vectors

            for x in range(height):

                combinations[y][x] *= -1

                combinations[y][x] += combinations[offset][x]

                combinations[y][x] %= 2



    return combinations[-1]





def get_y(x, factor_base):

    # actually, it computes integer square root of x, x must be smooth over

    # the factor base, square root must exists

    y = 1

    for factor in factor_base:

        while x % (factor ** 2) == 0:

            #print("factor found: %d" % factor)

            x = x // (factor ** 2)

            y *= factor

    return y





def gen_dependent_subset(U, factor_base):

    #print(" = finding non-trivial linear combination from vectors generated "

          #"from smooth array")

    vector_list = [generate_vector(u * u - N, factor_base) for u in U]



    linear_combination = find_linear_combination(vector_list)



    if not linear_combination:

        return None



    return [u for num, u in enumerate(U) if linear_combination[num] == 1]





def factorize(NN):
    global N
    N = NN
    
    factor_base = get_factor_base(N, primes)

    #print("factor base: %s" % factor_base)



    #print(" = generating smooth array")

    U = gen_smooth(factor_base, len(factor_base) + 20)

    # 20 is for good chance to find a non-trivial factors, probabliliy

    # of not finding ~ (1/3) ^ 20



    #print(U)

    #while len(U)>num:

    #  ret.remove(random.choice(ret))



    while True:

        U_dep = gen_dependent_subset(U, factor_base)

        if not U_dep:

            #print("  = bad luck")

            return 0, 0

        #print("dependent subset %s" % U_dep)



        x = 1

        for u in U_dep:

            x *= u



        pre_y = 1

        for u in U_dep:

            pre_y *= u * u - N



        y = get_y(pre_y, factor_base)



        if x == y:

            #print("bad dependency, removing %d from smooth array" % (U_dep[0]))

            U.remove(U_dep[0])

            continue



        f1, f2 = gcd(x + y, N), gcd(x - y, N)

        #print("finished dependency: x=%d, y=%d factors: %d and %d" % (

            #x, y, f1, f2))

        if f1 != N and f1 != 1 and f2 != N and f2 != 1:

            return f1, f2

        #print("bad dependency, removing %d from smooth array" % (U_dep[0]))

        U.remove(U_dep[0])



if __name__ == "__main__":

    p1 = 701
    p2 = 12532469
    N = p1*p2 


    f1, f2 = factorize(N)

    print("Answer: %d and %d" % (f1, f2))