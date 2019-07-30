#include "fibonacci.h"
#include "util.h"


Fibonacci::Fibonacci()
{};
Fibonacci::~Fibonacci()
{};

///
///读取1亿内素数表
Fibonacci::Fibonacci(const char*paths[2])
{	
	for(int i=0;i<2;i++)
	{
		const char* path = paths[i];
		ifstream f(path, ios::in);
		string s;
		while (getline(f, s))
		{
			vector<char*> vec = Util::SplitBuff((char*)s.c_str(), ",");
			vector<char*>::iterator it;
			for (it = vec.begin(); it < vec.end(); it++)
			{
				this->_primes.push_back(bigint(*it));
			}
		}
	}	
}

///
///获取第i个Fibonacci数
bigint Fibonacci::FastDoublingFibonacci(int n) const
{
	bigint a = bigint(0);
	bigint b = bigint(1);
	for (int i = 31; i >= 0; i--)
	{
		bigint d = a * (b * bigint(2) - a);
		bigint e = a*a + b*b;
		a = d;
		b = e;		
		if (((((uint)n >> i)) & 1)!=0)
		{
			bigint c = a + b;
			a = b;
			b = c;
		}
	}
	return a;
}

///
///获取第i个Fibonacci数模d
bigint Fibonacci::FastModulo(int n, const bigint& p) const
{
	bigint a = bigint(0);
	bigint b = bigint(1);
	
	for (int i = 31; i >= 0; i--)
	{
		bigint ap = a%p;
		bigint bp = b%p;						
		bigint d = (ap * ((bp * (bigint(2) % p)) % p - ap) % p) % p;
		bigint e = (ap * ap %p %p + bp * bp % p %p) % p;
		a = d;
		b = e;
		//cout << "i=" << i << ",value:" << ((((uint)n >> i)) & 1)<< endl;
		if (((((uint)n >> i)) & 1) != 0)
		{
			bigint c = a + b;
			a = b;
			b = c;
		}
	}
	return a;
}

///
///找约束周期
bigint Fibonacci::GetConstPeriod(const bigint& d) const
{
	bigint i = bigint(1);
	while (true)
	{
		bigint res = this->FastModulo(i, d);
		if (res == bigint(0))
			return i;
		i += bigint(1);
	}
}



///
///勒让德符号
bigint Fibonacci::Lerander(const bigint& d) const
{
	bigint r = d % bigint(5);
	bigint L = bigint(0);
	if (r != bigint(0))
	{
		bigint x = r.sqrt();
		if (x*x == r)
			L = bigint(1);
		else
			L = bigint(-1);		
	}
	return L;
}

///
///二分查找
bigint Fibonacci::BinarySearch(std::vector<bigint> &invec, bigint &value) const
{
	bigint pos = *(invec.end());
	bigint low = 0, high = pos - bigint(1);
	assert(!invec.empty() && pos >= bigint(0));
	while (low <= high){
		bigint mid = (low + high) / bigint(2);
		if (invec[mid] == value){
			return mid;
		}
		else if (invec[mid] < value){
			low = mid + bigint(1);
		}
		else{
			high = mid - bigint(1);
		}
	}
	return bigint(-1);
}

///
///排序并返回下标
std::vector<bigint> Fibonacci::SortVec(std::vector<bigint> &v) const
{
	vector<bigint> idx(v.size());	
	iota(idx.begin(), idx.end(), 0);
	sort(idx.begin(), idx.end(),
		[&v](bigint i1, bigint i2) {return v[i1] < v[i2]; });	
	sort(v.begin(), v.end());
	
	return idx;
}

///
///随机数
bigint Fibonacci::Random(bigint downLimit, bigint upLimit) const
{
	srand(time(NULL));	
	char str[1024] = { 0 };
	int size = rand()%(upLimit - downLimit).length();
	for (int i = 0; i<size;i++)
	{
		int num = rand() % (10);
		sprintf(str, "%s%d", str, num);
	}
	return downLimit + bigint(str);
}

///
///求皮萨诺周期
bigint Fibonacci::GetPisanoPeriod(const bigint& d) const
{
	//确定排序区间长度
	bigint pre = 100000;//d.sqrt().sqrt().sqrt().sqrt().sqrt().sqrt();
	bigint search_len = pre > bigint(10000) ? pre : bigint(10000);
	cout << "search len:" << search_len << endl;
		
	const struct tm *start = Util::NowTime();
	//估计相差的位数
	bigint xdiff = bigint(2);
	//找出较大的素数的位数
	bigint p_len = int((d.length() + xdiff) / bigint(2)) + bigint(1);
	//计算起点和终点
	char str[1024] = { 0 };
	for (int i = 0; i < p_len;i++)	sprintf(str,"%s%d",str, 9);
	bigint searchbegin = d - bigint(str);
	if (searchbegin <= bigint(0))
		searchbegin = bigint(0);
	bigint searchend = d + bigint(str);
	cout << "search begin:" << searchbegin << "search end:" << searchend << endl;
	//排序
	std::vector<bigint> sortVec;
	for (bigint i = 0; i < search_len; i++)
	{		
		sortVec.push_back(this->FastModulo(i, d));
	}
	std::vector<bigint> idxVec = this->SortVec(sortVec);
	const struct tm *end = Util::NowTime();
	cout << "sort time used:" << Util::TimeSpan(start, end) << " s" << endl;
	//查找	
	std::vector<bigint> checkedVec;
	while (true)
	{
		bigint r = this->Random(searchbegin, searchend);
		vector<bigint>::iterator loc = find(checkedVec.begin(), checkedVec.end(), r);
		if (loc != checkedVec.end())
			continue;
		else
			checkedVec.push_back(r);
		bigint res = this->FastModulo(r, d);
		bigint inx = BinarySearch(sortVec, res);
		if (inx != bigint(-1))
		{
			bigint res_n = idxVec[inx];
			bigint T = r - res_n;
			if (this->FastModulo(T, d)==bigint(0))
			{
				end = Util::NowTime();
				cout << "find T=" << T << ",total time used:" << Util::TimeSpan(start, end) << " s" << endl;
			}
		}
	}
}

///
///分解整数
bigint Fibonacci::Factorization(bigint& T, bigint& d) const
{
	bigint M = d - T + bigint(1);
	bigint p = (M + (M*M - bigint(4) * d).sqrt()) / bigint(2);
	bigint q = d / p;
	bigint _p = (M - (M*M - bigint(4) * d).sqrt()) / bigint(2);
	bigint _q = d / _p;
	if (p > bigint(0) && p*q == d)
	{
		cout << "factor type=1,p1=" << p << ",p2=" << q << endl;
		return p;
	}
	else if (_p > bigint(0) && _p*_q == d)
	{
		cout << "factor type=1,p1=" << _p << ",p2=" << _q << endl;
		return _p;
	}
	
	bigint M1 = d - T - bigint(1);
	bigint p1 = (M1 + (M1*M1 + bigint(4) * d).sqrt()) / bigint(2);
	bigint q1 = d / p1;
	bigint _p1 = (M1 - (M1*M1 + bigint(4) * d).sqrt()) / bigint(2);
	bigint _q1 = d / _p1;
	if (p1 > bigint(0) && p1*q1 == d)
	{
		cout << "factor typ1e=2,p11=" << p1 << ",p12=" << q1 << endl;
		return p1;
	}
	else if (_p1 > bigint(0) && _p1*_q1 == d)
	{
		cout << "factor typ1e=2,p11=" << _p1 << ",p12=" << _q1 << endl;
		return _p1;
	}

	bigint M2 = -(d - T - bigint(1));
	bigint p2 = (M2 + (M2*M2 + bigint(4) * d).sqrt()) / bigint(2);
	bigint q2 = d / p2;
	bigint _p2 = (M2 - (M2*M2 + bigint(4) * d).sqrt()) / bigint(2);
	bigint _q2 = d / _p2;
	if (p2 > bigint(0) && p2*q2 == d)
	{
		cout << "factor typ2e=1,p21=" << p2 << ",p22=" << q2 << endl;
		return p2;
	}
	else if (_p2 > bigint(0) && _p2*_q2 == d)
	{
		cout << "factor typ2e=1,p21=" << _p2 << ",p22=" << _q2 << endl;
		return _p2;
	}

	bigint M3 = -(d - T + bigint(1));
	bigint p3 = (M3 + (M3*M3 - bigint(4) * d).sqrt()) / bigint(2);
	bigint q3 = d / p3;
	bigint _p3 = (M3 - (M3*M3 - bigint(4) * d).sqrt()) / bigint(2);
	bigint _q3 = d / _p3;
	if (p3 > bigint(0) && p3*q3 == d)
	{
		cout << "factor typ3e=1,p31=" << p3 << ",p32=" << q3 << endl;
		return p3;
	}
	else if (_p3 > bigint(0) && _p3*_q3 == d)
	{
		cout << "factor typ3e=1,p31=" << _p3 << ",p32=" << _q3 << endl;
		return _p3;
	}

	cout << "factorization fail" << endl;
	return bigint(-1);
		
}


