#include "bigint.h"
using namespace std;

using std::cerr;
using std::endl;

#pragma warning(disable: 4996)

//////////////////////////////////////////////////////////////
void bigint::format()
{
	int len = strlen(arr);
	arr[len] = 0;
	for (int i = len - 1; i>0; i--){
		arr[MAX_LEN - len + i] = arr[i] - 48; // 数字字符转转为数值 
		arr[i] = 0;
	}
	if (arr[0] == '-') arr[0] = 1;
	else if (arr[0] == '+') arr[0] = 0;
	else{
		arr[MAX_LEN - len] = arr[0] - 48;
		arr[0] = 0;
	}
}

bigint::bigint(int a)
{
	bzero();
	//itoa(a, arr, 10);
	snprintf(arr,sizeof(arr),"%d",a);
	format();
}

bigint::bigint(const char *str)
{
	bzero();
	const char *c = str;
	char *p = arr;
	if (*c == '+' || *c == '-')
		*p++ = *c++;
	while (*c)
	{
		if (*c >= '0' && *c <= '9')
			*p++ = *c++;
		else break;
	}
	*p = '\0';
	format();
}

bigint::bigint(const bigint &obj)
{
	for (int i = 0; i<MAX_LEN; i++)
		arr[i] = obj.arr[i];
}

bigint& bigint::operator=(const bigint &obj)
{
	if (this == &obj) return *this;
	for (int i = 0; i<MAX_LEN; i++)
		arr[i] = obj.arr[i];
	return *this;
}

//////////////////////////////////////////////////////////////////////
bigint& bigint::operator++()
{
	int jw, len = length();
	if (arr[0] == 0){
		for (int i = MAX_LEN - 1; i>MAX_LEN - len - 2; i--)
		{
			++arr[i];
			if (arr[i]>9)
				arr[i] = arr[i] % 10;
			else break;
		}
	}
	else{
		for (int i = MAX_LEN - 1; i>MAX_LEN - len - 2; i--)
		{
			--arr[i];
			if (arr[i]>9)
				arr[i] = arr[i] % 10;
			else break;
		}
	}
	return *this;
}

bigint bigint::operator++(int)
{
	bigint ret(*this);
	++*this;
	return ret;
}
bigint& bigint::operator--()
{
	int jw, len = length();
	if (arr[0] == 0){
		for (int i = MAX_LEN - 1; i>MAX_LEN - len - 2; i--)
		{
			--arr[i];
			if (arr[i]>9)
				arr[i] = arr[i] % 10;
			else break;
		}
	}
	else{
		for (int i = MAX_LEN - 1; i>MAX_LEN - len - 2; i--)
		{
			++arr[i];
			if (arr[i]>9)
				arr[i] = arr[i] % 10;
			else break;
		}
	}
	return *this;
}

bigint bigint::operator--(int)
{
	bigint ret(*this);
	--*this;
	return ret;
}

bigint bigint::operator-() const
{
	bigint ret = *this;
	ret.arr[0] = 1 - ret.arr[0];
	return ret;
}

bigint bigint::abs() const
{
	bigint ret = *this;
	ret.arr[0] = 0;
	return ret;
}
///////////////////////////////////////////////////////////////////
bool bigint::absbigger(const bigint &obj) const
{
	for (int i = 1; i<MAX_LEN; i++){
		if (arr[i] > obj.arr[i])
			return true;
		else if (arr[i] < obj.arr[i])
			return false;
	}
	return false;
}
bool bigint::abssmaller(const bigint &obj) const
{
	for (int i = 1; i<MAX_LEN; i++){
		if (arr[i] < obj.arr[i])
			return true;
		else if (arr[i] > obj.arr[i])
			return false;
	}
	return false;
}
bool bigint::absequal(const bigint &obj) const
{
	for (int i = 1; i<MAX_LEN; i++)
	if (arr[i] != obj.arr[i])
		return false;
	return true;
}

////////////////////////////////////////////////////////////////////
bool bigint::operator==(const bigint &obj)const
{
	bool ret = (arr[0] == obj.arr[0] && absequal(obj));
	if (ret) return ret;
	if (iszero() && obj.iszero()) return true;
	else return false;
}

bool bigint::operator<=(const bigint &obj)const
{
	bigint tmp = *this - obj;
	if (tmp.iszero()) return true;
	else return (tmp.arr[0] == 1);

}
bool bigint::operator>=(const bigint &obj)const
{
	bigint tmp = *this - obj;
	if (tmp.iszero()) return true;
	else return (tmp.arr[0] == 0);
}

////////////////////////////////////////////////////////////////////////
istream& operator>>(istream &is, bigint &obj)
{
	obj.bzero();
	is >> obj.arr;
	obj.format();
	return is;
}

ostream& operator<<(ostream &os, const bigint &obj)
{
	if (obj.arr[0] == 1) os << '-';    //输出符号位 
	bool flag = false;
	for (int i = 1; i<obj.MAX_LEN; i++){
		if (obj.arr[i] >= 1 && obj.arr[i] <= 9){
			os << (int)obj.arr[i];
			flag = true;
		}
		else if (flag)
			os << (int)obj.arr[i];
	}
	if (flag == false)
		os << '0';
	return os;
}

//////////////////////////////////////////////////////////////////////////
bigint::operator int() const
{
	bigint max(INT_MAX);
	bigint min(INT_MIN);
	if (*this >= max) return INT_MAX;
	if (*this <= min) return INT_MIN;
	int len = length();
	int ret = 0;
	int w = 1;
	for (int i = MAX_LEN - 1; i>MAX_LEN - len - 1; i--){
		ret += w*(int)arr[i];
		w *= 10;
	}
	if (arr[0] == 0) return ret;
	else return -ret;
}

bool bigint::iszero()const
{
	for (int i = 1; i<MAX_LEN; i++)
	if (arr[i] != 0) return false;
	return true;
}

int bigint::length()const
{
	int i;
	for (i = 1; i<MAX_LEN; i++)
	if (arr[i] >= 1 && arr[i] <= 9)
		break;
	return MAX_LEN - i;
}

void bigint::debugprint()const
{
	cout << "{ ";
	for (int i = 0; i<MAX_LEN; i++) cout << (int)arr[i];
	cout << " }" << endl;
}

//////////////////////////////////////////////////////////////////////////
/**
* 将obj的数值位加到*this的数值位
* 时间复杂度 O(n)
* 空间复杂度 O(1)
**/
bigint& bigint::unsigned_add(const bigint &obj)
{
	int len1 = length();
	int len2 = obj.length();
	int ml = len1>len2 ? len1 : len2;

	int sum, jw = 0;
	for (int i = MAX_LEN - 1; i>MAX_LEN - ml - 2; i--){
		sum = jw + arr[i] + obj.arr[i];
		arr[i] = (sum % 10);
		jw = sum / 10;
	}
	return *this;
}

/**
* 计算两个bigint数值位之间的差值 -> *this的数值位
* 时间复杂度 O(n)
* 空间复杂度 O(1)
**/
bigint& bigint::unsigned_dif(const bigint &obj)
{
	int len1 = length();
	int len2 = obj.length();
	int ml = len1>len2 ? len1 : len2;
	int flag = absbigger(obj);
	int sub, jw = 0;
	for (int i = MAX_LEN - 1; i>MAX_LEN - ml - 2; i--)
	{
		if (flag) sub = arr[i] - jw - obj.arr[i];
		else sub = obj.arr[i] - jw - arr[i];
		if (sub >= 0){
			arr[i] = sub;
			jw = 0;
		}
		else{
			arr[i] = sub + 10;
			jw = 1;
		}
	}
	return *this;
}

bigint bigint::operator+(const bigint &obj) const
{
	bigint ret = *this;
	if (arr[0] == obj.arr[0]){   //符号位相同 
		ret.unsigned_add(obj);
	}
	else {
		if (abssmaller(obj))
			ret.arr[0] = obj.arr[0];
		ret.unsigned_dif(obj);
	}
	return ret;
}

bigint bigint::operator-(const bigint &obj) const
{
	bigint ret = *this;
	if (arr[0] == (1 - obj.arr[0])){   //符号位相同 
		ret.unsigned_add(obj);
	}
	else {
		if (abssmaller(obj))
			ret.arr[0] = (1 - obj.arr[0]);
		ret.unsigned_dif(obj);
	}
	return ret;
}

bigint bigint::operator*(const bigint &obj) const
{
	bigint ret;
	// 处理符号位 
	if (arr[0] != obj.arr[0])
		ret.arr[0] = 1;
	// 处理数值位 
	int len1 = length();
	int len2 = obj.length();
	int tmp, cur;
	for (int i = MAX_LEN - 1; i >= MAX_LEN - len1; i--)
	{
		for (int j = MAX_LEN - 1; j >= MAX_LEN - len2; j--)
		{
			cur = i + j - MAX_LEN + 1;
			if (cur<1){
				cerr << "error: 乘积超出范围!" << endl;
				exit(1);
			}
			tmp = arr[i] * obj.arr[j] + ret.arr[cur];
			ret.arr[cur] = tmp % 10;
			ret.arr[cur - 1] += tmp / 10;
		}
	}
	return ret;
}

bigint bigint::operator/(const bigint &obj) const
{
	bigint ret;
	// 处理数值位 
	bigint a = *this;  a.arr[0] = 0;
	bigint b = obj;    b.arr[0] = 0;
	bigint t = ret*b;
	while (t <= a){
		++ret;
		t = ret*b;
	}
	--ret;
	// 处理符号位 
	if (arr[0] != obj.arr[0])
		ret.arr[0] = 1;
	return ret;
}

bigint bigint::operator%(const bigint &obj) const
{
	bigint ret;
	bigint a = *this; 
	while (1)
	{
		if (a < bigint(0))
			a += obj;
		else
			break;
	}	
	a.arr[0] = 0;
	bigint b = obj; b.arr[0] = 0;
	bigint c = a / b;
	return a - b*c;
}

bigint bigint::sqrt() const
{
	bigint x = *this;
	bigint sum_n = 0;
	bigint n = (x / bigint(2));
	bigint top = x;
	bigint bottom = 0;

	if (x <= bigint(1))
	{
		return x;
	}
	for (;;)
	{
		sum_n = n*n;
		if (sum_n < x)
		{
			bottom = n;
			n += ((top - bottom) / bigint(2));
			if (n == bottom)
				return n;
		}
		else if ( sum_n > x)			
		{
			top = n;
			n -= ((top - bottom) / bigint(2));
			if (n == top)
				return n - bigint(1);				
			}
		else
		{
			return n;
		}		
	}

}

