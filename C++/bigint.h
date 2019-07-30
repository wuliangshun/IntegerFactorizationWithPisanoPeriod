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
	static const int MAX_LEN = 1024; //��󲻳���10^1024
	char arr[MAX_LEN];

public:
	void bzero(){ memset(arr, 0, MAX_LEN); }
	bigint(){ bzero(); }
	bigint(const char *);
	bigint(int);
	bigint(const bigint&);
	bigint& operator=(const bigint&);

public: /* ������������� */
	bigint& operator++();   // ǰ��++ 
	bigint operator++(int); // ����++ 
	bigint& operator--();   // ǰ��-- 
	bigint operator--(int); // ����-- 

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
	

public:/* ������������� */
	bool operator!=(const bigint &obj)const{ return !(*this == obj); }
	bool operator==(const bigint &obj)const;
	bool operator<=(const bigint &obj)const;
	bool operator>=(const bigint &obj)const;
	bool operator<(const bigint &obj)const{ return !(*this >= obj); }
	bool operator>(const bigint &obj)const{ return !(*this <= obj); }

	bool absbigger(const bigint &obj)const; // ����ֵ���� 
	bool absequal(const bigint &obj)const;  // ����ֵ���� 
	bool abssmaller(const bigint &obj)const;// ����ֵС�� 

	operator int() const; // bigint -> int ������ת������ 

public:
	friend istream& operator>>(istream&, bigint &obj);
	friend ostream& operator<<(ostream&, const bigint &obj);

public:
	int length()const;  /* ������ֵλ�ĳ��� */
	void debugprint()const; /* ����ʱʹ�ã���ӡÿһλ��ֵ */

private:  /* һЩ˽�к��� */
	void format();
	bool iszero()const;
	bigint& unsigned_add(const bigint &obj);
	bigint& unsigned_dif(const bigint &obj);
};


#endif
