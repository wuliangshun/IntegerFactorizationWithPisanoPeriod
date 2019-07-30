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
	Fibonacci(const char*paths[2]);//����1����������
	~Fibonacci();
	bigint FastDoublingFibonacci(int) const;//����Fibonacci
	bigint FastModulo(int, const bigint&) const;//����Fibonacci��ģ
	bigint GetPisanoPeriod(const bigint& d) const;//��Ƥ��ŵ����
	bigint GetConstPeriod(const bigint& d) const;//��Լ������
	bigint Lerander(const bigint& d) const;//���õ·���
	bigint Random(bigint downLimit, bigint upLimit) const;//�����
	bigint BinarySearch(std::vector<bigint> &invec,  bigint &value) const;//���ֲ���
	std::vector<bigint> SortVec(std::vector<bigint> &v) const;//���򷵻��±�
	bigint Factorization(bigint& T, bigint& d) const;//�ֽ������

	vector<bigint> _primes;

private:
	
};





#endif