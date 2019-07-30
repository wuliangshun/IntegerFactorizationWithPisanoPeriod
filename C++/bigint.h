#ifndef BIGINT_H
#define BIGINT_H

#include<iostream>
#include <ctime>
#include <string.h>

#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)

using std::istream;
using std::ostream;

class bigint
{
private:
	static const int MAX_LEN = 1024; //最大不超过10^1024
	char arr[MAX_LEN];

public:
	void bzero(){ memset(arr, 0, MAX_LEN); }
	bigint(){ bzero(); }
	bigint(const char *);
	bigint(int);
	bigint(const bigint&);
	bigint& operator=(const bigint&);

public: /* 算术运算符重载 */
	bigint& operator++();   // 前置++ 
	bigint operator++(int); // 后置++ 
	bigint& operator--();   // 前置-- 
	bigint operator--(int); // 后置-- 

	bigint operator+()const{ return *this; }
	bigint operator-()const;
	bigint abs()const;

	bigint operator+(const bigint &obj)const;
	bigint operator-(const bigint &obj)const;
	bigint operator*(const bigint &obj)const;
	bigint operator/(const bigint &obj)const;
	bigint operator%(const bigint &obj)const;

	bigint& operator+=(const bigint &obj){ *this = *this + obj; return *this; }
	bigint& operator-=(const bigint &obj){ *this = *this - obj; return *this; }
	bigint& operator/=(const bigint &obj){ *this = *this * obj; return *this; }
	bigint& operator*=(const bigint &obj){ *this = *this / obj; return *this; }
	bigint& operator%=(const bigint &obj){ *this = *this % obj; return *this; }

	bigint sqrt() const;
	

public:/* 布尔运算符重载 */
	bool operator!=(const bigint &obj)const{ return !(*this == obj); }
	bool operator==(const bigint &obj)const;
	bool operator<=(const bigint &obj)const;
	bool operator>=(const bigint &obj)const;
	bool operator<(const bigint &obj)const{ return !(*this >= obj); }
	bool operator>(const bigint &obj)const{ return !(*this <= obj); }

	bool absbigger(const bigint &obj)const; // 绝对值大于 
	bool absequal(const bigint &obj)const;  // 绝对值等于 
	bool abssmaller(const bigint &obj)const;// 绝对值小于 

	operator int() const; // bigint -> int 的类型转换函数 

public:
	friend istream& operator>>(istream&, bigint &obj);
	friend ostream& operator<<(ostream&, const bigint &obj);

public:
	int length()const;  /* 返回数值位的长度 */
	void debugprint()const; /* 调试时使用，打印每一位的值 */

private:  /* 一些私有函数 */
	void format();
	bool iszero()const;
	bigint& unsigned_add(const bigint &obj);
	bigint& unsigned_dif(const bigint &obj);
};


#endif
