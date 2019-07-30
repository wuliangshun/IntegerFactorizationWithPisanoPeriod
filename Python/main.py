# -*- coding: utf-8 -*-
"""
RSA
"""
import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from memory_profiler import profile
import GeneratePrime as gp

class Fibonacci:
    
    def __init__(self):
        pass
    
    def _fib(self,n):
    	if n == 0:
    		return (0, 1)
    	else:
    		a, b = self._fib(n // 2)
    		c = a * (b * 2 - a)
    		d = a * a + b * b
    		if n % 2 == 0:
    			return (c, d)
    		else:
    			return (d, c + d)
    
    def _fib_res(self,n,p):
    	if n == 0:
    		return (0, 1)
    	else:
    		a, b = self._fib_res(n // 2,p)
    		c = (a%p * (2*b-a)%p)%p
    		d = (a*a%p + b*b%p)%p
    		if n % 2 == 0:
    			return (c, d)
    		else:
    			return (d, c+d)
    
    #获取第i个Fibonacci数
    def get_n(self,n):
        if n < 0:
            ValueError("Negative arguments not implemented")
        return self._fib(n)[0]
    
    #获取第i个Fibonacci数模d
    def get_n_mod_d(self,n,d):
        if n < 0:
            ValueError("Negative arguments not implemented")
        return self._fib_res(n,d)[0]
    
    #找约束周期
    def find_dm(self,d):
        i=1
        while True:
            res = self.get_n_mod_d(i,d)
            if res==0:
                return i
            i += 1
    
    #勒让德符号
    def lerander(self,p):
        r = p%5
        L = 0
        if r != 0:        
            x = int(np.sqrt(r)) 
            if x*x == r:
                L = 1
            else:
                L = -1
        return L
    
    #二分查找
    def binary_search(self,L,n):
        left=0
        right=len(L)-1
        while left<=right:
            mid=(left+right)//2
            if n==L[mid]:
                return mid
            elif n<L[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
    
    #求周期：找到剩余值为0，1为止
    def get_period(self,d):
        ini = 1
        mod0 = self.get_n_mod_d(ini,d)
        mod1 = self.get_n_mod_d(ini+1,d)
         
        i = ini+2
        while True:
            temp = mod0
            mod0 = mod1
            mod1 = (temp+mod1)%d                 
                   
            if mod0 == 0 and mod1 == 1:
                break;
            i += 1
        return i-1
    
    #求周期：同上，但初始值从d-sqrt(d)开始
    def get_period_sqrtini(self, d):
    
        if d > 1000:
            ini = d-int(np.sqrt(d))
        else:
            ini = 1
        mod0 = self.get_n_mod_d(ini,d)
        mod1 = self.get_n_mod_d(ini+1,d)
         
        i = ini+2
        while True:
            temp = mod0
            mod0 = mod1
            mod1 = (temp+mod1)%d                 
                   
            if mod0 == 0 and mod1 == 1:        
                break;
            i += 1
    
    #对list进行排序
    def sort_list(self,L):
        from operator import itemgetter
        indices, L_sorted = zip(*sorted(enumerate(L), key=itemgetter(1)))
        return list(L_sorted),list(indices)
    
    @profile(precision=4,stream=open('memory_profiler.log','w+'))  
    #求周期：大整数周期求法
    def get_period_bigint(self, d, min_accept, xdiff):            
        #搜索区间长度
        search_len = int(d**(1.0/6)/100)   
        
        if search_len<min_accept:
            search_len = min_accept
        print('search_len:%d'%(search_len))
        
        starttime = time.time()
        #估计相差的位数
        diff = xdiff 
        #找出较大的素数的位数
        p_len = int((len(str(d)) + diff)/2) + 1
        #计算起点和终点
        begin = d - int('9'*p_len) 
        if begin<=0:
            begin=0
        end = d + int('9'*p_len)
        
        print('search begin:%d,end:%d'%(begin,end))
                
        rs = [self.get_n_mod_d(x,d) for x in range(search_len)]
        rs_sort,rs_indices = self.sort_list(rs) 
                
        print('sort complete! time used:%f secs'%(time.time()-starttime))
                
        T = 0
        has_checked_list = []
        while True:       
            randi = random.randint(begin,end)            
            if randi in has_checked_list:
                continue
            else:
                has_checked_list.append(randi)
            
            res = self.get_n_mod_d(randi,d)
            inx = self.binary_search(rs_sort,res)
                                    
            if inx != -1:                
                res_n = rs_indices[inx]
                T = randi - res_n
                
                return
                     
                if self.get_n_mod_d(T,d) == 0:
                    t = time.time()-starttime
                    print('For N=%d,find T=%d,time used %f secs.'%(d,T,t))
                    return t,T
                else:
                    print('For N=%d,find res:%d,T:%d,but failed'%(d,res,T))
       
        
    
    
        
    def factorization(self, _T, d):
        #类型1
        M = d-_T+1
        p1 = (M + np.sqrt(M**2-4*d))/2
        p2 = d/p1
        _p1 = (M - np.sqrt(M**2-4*d))/2
        _p2 = d/_p1
        if p1>0 and p1==int(p1) and p2==int(p2):   
            print('factor type=1,p1={},p2={}'.format(p1,p2))
            return p1,p2
        elif _p1>0 and _p1==int(_p1) and _p2==int(_p2):   
            print('factor type=-1,p1={},p2={}'.format(_p1,_p2))
            return _p1,_p2
           
        #类型2
        M = d-_T-1
        p1 = (M + np.sqrt(M**2+4*d))/2
        p2 = d/p1
        _p1 = (M - np.sqrt(M**2+4*d))/2
        _p2 = d/_p1
        if p1>0 and p1==int(p1) and p2==int(p2):   
            print('factor type=2,p1={},p2={}'.format(p1,p2))
            return p1,p2
        elif _p1>0 and _p1==int(_p1) and _p2==int(_p2):   
            print('factor type=-2,p1={},p2={}'.format(_p1,_p2))
            return _p1,_p2
        
        #类型3
        M = d-_T-1
        p1 = (-M + np.sqrt(M**2+4*d))/2
        p2 = d/p1
        _p1 = (-M - np.sqrt(M**2+4*d))/2
        _p2 = d/_p1
        if p1>0 and p1==int(p1) and p2==int(p2):   
            print('factor type=3,p1={},p2={}'.format(p1,p2))
            return p1,p2
        elif _p1>0 and _p1==int(_p1) and _p2==int(_p2):   
            print('factor type=-3,p1={},p2={}'.format(_p1,_p2))
            return _p1,_p2
        
        #类型4
        M = d-_T+1
        p1 = (-M + np.sqrt(M**2-4*d))/2
        p2 = d/p1
        _p1 = (-M - np.sqrt(M**2-4*d))/2
        _p2 = d/_p1
        if p1>0 and p1==int(p1) and p2==int(p2):   
            print('factor type=4,p1={},p2={}'.format(p1,p2))
            return p1,p2
        elif _p1>0 and _p1==int(_p1) and _p2==int(_p2):   
            print('factor type=-4,p1={},p2={}'.format(_p1,_p2))
            return _p1,_p2
        
        print('factorization fail')
      
        
    #根据余数找Fibonacci数
    def find_inx(self,res):
        pass 
    
  
    def get_residuals(self,d): 
        dm = self.find_dm(d)
        T = 2*dm
        print('d=%d,T=%d'%(d,T))
        self.residuals = [self.get_n_mod_d(i,d) for i in range(2*T)]
        return self.residuals
    
    def draw_residuals(self):
        x_list = [i for i in range(len(self.residuals))]
        plt.scatter(x_list,self.residuals)
    
    def export_to_csv(self,residuals):
        df = pd.DataFrame({'res':residuals})
        df.to_csv('../Data/residuals.csv')
        print('export succeed!')
 
Ns = [11861,557951,581851,1343807,
      3031993,4192681,5502053,6654671,
      12399797,14159471,16364501,20211713,
      22828523,44335457,50632823,57635863,
      384237701921,901500973759,6673435981363,
      11882099612003,15916520600381,17536455849431,
      18960823962761,21554451067267,33241863073423,
      55076499371497,57744632372831,67165261388497,
      68072569242511,69684586201261,87756536366813,
      107458854058613,140967368218669,144086313393859,
      148077481187381,159872954386241,167863367550997,
      173112365219141,199390622342239,235255553137067,
      240522164849797,255119369061203,260436416434589,
      284911570131079,284984450489831,285341598723821,
      317418445093391,317554392679033,323219479761449,
      343840350739729,375275396864183,411429562199009,
      459621830953379,525220163614031]  
'''
RSA-59 RSA-79 RSA-99 RSA-119 RSA-100
'''
RSA = [71641520761751435455133616475667090434063332228247871795429,
       7293469445285646172092483905177589838606665884410340391954917800303813280275279,
       256724393281137036243618548169692747168133997830674574560564321074494892576105743931776484232708881,
       55519750778717908277109380212290093527311630068956900635648324635249028602517209502369255464843035183207399415841257091,
       1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139]         
p1_list = [786766447,16375977287,81465486209,90824225567,862404698273,10452041068841,12697022389549,87996844075109,102010159808071,654472677526847,714033326215093,13051559264369500,13152735237439093,85817923293837151,131912444345458000]
p2_list = [673815403,130260073,10937527,15171889,988483,109471,113489,11863,16141,919,631,83,67,13,11,]
    
if __name__=='__main__':
    fib = Fibonacci()
    times = []
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#小整数情形
    for i in range(18,len(Ns)):
        t,T = fib.get_period_bigint(701*4051,10000,2)
        times.append(t)
        print('---------------------------------')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#大整数
#    fib.get_period_bigint(RSA[1],1000,0)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#相差位数实验
#    for i in range(len(p1_list)):
#        p1 = p1_list[i]
#        p2 = p2_list[i]
#        if p1%2==0:
#            continue
#        N = p1*p2
#        fib.get_period_bigint(N,1000000,abs(len(str(p1)) - len(str(p2))))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#排序长度实验
#    min_list = [100,1000,10000,100000,1000000]
#    N = 525220163614031
#    for m in min_list:        
#        t,T = fib.get_period_bigint(N,min_list[1])

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#内存消耗实验
#for i in range(20,30):
#    N = gp.generate_prime_number_decimal(i)
#    fib.get_period_bigint(N,100000,0)
#    p1 = 701
#    p2 = 12532469
#    d = p1*p2  
#    fib.find_dm(221)
#    residuals = fib.get_residuals(221)
#    fib.draw_residuals()
#    fib.export_to_csv(residuals)
    #fib.draw_gamma_sigmoid(29)
    #fib.compare_time_sigmoid(29)
    #femat method
#    fib.femat_factorization(d)
#    #pollard_rho method
#    fib.pollard_rho_factorization(d)
#    #fib method
#    T = fib.get_period_zhengchu(d)
    #T = fib.verify_min_periodity(T,d)
    #fib.factorization(T,d)
    
    pass