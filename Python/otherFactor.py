# -*- coding: utf-8 -*-
"""
几种主流的整数分解方法
"""
from math import sqrt,floor,gcd
import random
from time import time
import Demo
import pandas as pd
import GeneratePrime as gp

"""
---------------------以下是一些常见大整数分解方法的实现------------------------
"""

"""
  费马算法：适合p1 p2几乎相等的情况https://blog.csdn.net/u011815404/article/details/81335633
"""
def femat_factorization(d):
    starttime = time()
    a = int(sqrt(d))
    if a*a<d:
        a += 1
    
    while True:
        temp = a*a - d
        b = int(sqrt(temp))
        if b*b == temp:
            break
        a += 1
    p1 = a+b
    p2 = a-b
    print('femat,p1=%d, p2=%d, time used %f secs'%(p1,p2,time()-starttime))
    return time()-starttime
    
"""
   pollard p-1因子分解方法
"""  
def fast_power(x,e,m):
    a = x
    b = 1
    while e>0:
        if e%2==1:
            b = (b*a)%m
        a = (a*a)%m
        e = floor(e/2)
        if e<=0:
            break
    return b        
         

def pollard_p_1_factorization(N):
    starttime = time()
    a = 2
    iterations = 0
    for j in range(2,N):
        a = fast_power(a,j,N)
        d = gcd(a-1,N)
        iterations += 1
        if d>1 and d<N:
            #print("iterations:%d"%(iterations))
            print('pollard p-1方法,p1=%d, p2=%d, time used %f secs'%(d,N/d,time()-starttime))
            return time()-starttime
   
    
    
     
  
"""
   连分数分解方法
"""  
#判断是否为平方数
def is_square(n):
    t = int(sqrt(n))
    return t*t == n

def continued_fraction_factorization(d):
    starttime = time()
    n=d
    seq_P, seq_Q=0, 1
    a0 = floor(sqrt(n))
    seq_a= [a0]
    seq_p = [0,a0]
    i = 1
    while True:
        #P_{k},Q_{k}序列
        seq_P = seq_a[0]*seq_Q-seq_P
        seq_Q = divmod(n-seq_P**2,seq_Q)[0]
        t = (seq_P+sqrt(n))/seq_Q
        seq_a[0] = floor(t)
        #p_{k}序列
        if i == 1:
            seq_p.append(a0*seq_a[0]+1)
        else:
            seq_p[0] = seq_p[1]
            seq_p[1] = seq_p[2]
            seq_p[2] = seq_a[0]*seq_p[1]+seq_p[0]
        #分解因式
        if i%2 == 0 and is_square(seq_Q):
            s = int(sqrt(seq_Q))
            factor = [gcd(seq_p[1]-s,n),gcd(seq_p[1]+s,n)]
            if factor[0] != 1 and factor[1] != 1:
                #print('第%d项：%d,%d'%(i,factor[0],factor[1]))
                #print('程序运行完毕！')
                break
        if i%1000 == 0:
            #print('已运行到第%d项'%i)
            pass
        i += 1
    print('连分数方法,p1=%d, p2=%d, time used %f secs'%(factor[0],factor[1],time()-starttime))
    return time()-starttime

"""
  二次筛法
"""
def quadratic_sieve(N):
    import quadratic_sieve as qs
    starttime = time()
    results = qs.factorize(N)
    print('二次筛法,p1=%d, p2=%d, time used %f secs'%(results[0],results[1],time()-starttime))
    return time()-starttime

"""
  椭圆曲线方法
"""
def ecliptic_curve_factorization(N):
    from elliptic_curve.lenstra import Lenstra
    starttime = time()
    sol = Lenstra(N).factor()
    print('椭圆曲线方法 p1=%d, p2=%d, time used %f secs'%(sol,N/sol,time()-starttime))
    return time()-starttime

if __name__=='__main__':
#    p1 = 701
#    p2 = 12532469
#    N = p1*p2  
    
#    demo = Demo.Demo()
#    demo.get_primes()
    '''
    位数相差较大时，
    '''
    p1_list=[]
    p2_list=[]
    x_list=[]
    time_fermat_list = []
    time_CFF_list = []
    time_Pollard_list = []
    time_QS_list = []
    time_ECM_list = []
    count = 0
    for i in range(12,20):
        try:            
            p1 = gp.generate_prime_number_decimal(i)
            p2 = gp.generate_prime_number_decimal(20-i)
            N =  71641520761751435455133616475667090434063332228247871795429
            minus = abs(len(str(p2))- len(str(p1)))
            plus = len(str(p2)) + len(str(p1))            
            print(minus,plus,p1,p2)
            time_fermat = 1#femat_factorization(N)
            time_CFF = continued_fraction_factorization(N)
            time_Pollard = pollard_p_1_factorization(N)
            time_QS = quadratic_sieve(N)
            time_ECM = ecliptic_curve_factorization(N)
            p1_list.append(p1)
            p2_list.append(p2)
            time_fermat_list.append(time_fermat)
            time_CFF_list.append(time_CFF)
            time_Pollard_list.append(time_Pollard)
            time_QS_list.append(time_QS)
            time_ECM_list.append(time_ECM)
            x_list.append(minus)
            if count%2 == 0:
                df = pd.DataFrame({'p1':p1_list,'p2':p2_list,
                                   'x':x_list,
                                   'fermat':time_fermat_list,
                                   'CFRAC':time_CFF_list,
                                   'Pollard':time_Pollard_list,
                                   'quadratic sieve':time_QS_list,
                                   'ecliptic curve':time_ECM_list,                               
                                   })
                df.to_csv('../Data/factor_time_compare.csv',index=False)
                print('%d has done'%(count))
            count+=1
        except Exception as e:
            print (e)
        
    
    
    
    
    
    

