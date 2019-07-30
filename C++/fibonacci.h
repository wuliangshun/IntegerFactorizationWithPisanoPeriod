#ifndef _FAST_FIBONACCI_H
#define _FAST_FIBONACCI_H
#include "bigint.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <vector>
#include <assert.h>
#include <algorithm>
#include <numeric>
#include <stdlib.h>

using namespace std;

#define uint unsigned int 

class Fibonacci
{
public:
	Fibonacci();
	Fibonacci(const char*paths[2]);//输入1亿内素数表
	~Fibonacci();
	bigint FastDoublingFibonacci(int) const;//快速Fibonacci
	bigint FastModulo(int, const bigint&) const;//快速Fibonacci求模
	bigint GetPisanoPeriod(const bigint& d) const;//找皮萨诺周期
	bigint GetConstPeriod(const bigint& d) const;//找约束周期
	bigint Lerander(const bigint& d) const;//勒让德符号
	bigint Random(bigint downLimit, bigint upLimit) const;//随机数
	bigint BinarySearch(std::vector<bigint> &invec,  bigint &value) const;//二分查找
	std::vector<bigint> SortVec(std::vector<bigint> &v) const;//排序返回下标
	bigint Factorization(bigint& T, bigint& d) const;//分解大整数

	vector<bigint> _primes;

private:
	
};





#endif