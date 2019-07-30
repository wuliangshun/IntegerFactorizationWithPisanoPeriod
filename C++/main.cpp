

#include "bigint.h"
#include "fibonacci.h"
#include "util.h"



int main()
{
	

	cout << "---------------------------------------------Test big int Operation--------------------------------" << endl;
	bigint li = bigint("45") + bigint("15");
	cout << "45 + 15 = " << li << endl;
	cout << "-16 / 7 = " << bigint("-16") / bigint("7") << endl;
	cout << "34 % 5 = :" << bigint("34") % bigint("5") << endl;
	cout << "sqrt(34) = " << bigint(34).sqrt() << endl;
	cout << endl;
	
	cout << "---------------------------------------------Test print function--------------------------------" << endl;
	const char* str = "aaa";
	int ret = strcmp(str, "aaa");
	cout << "strcmp result:" << ret << endl;
	cout << endl;

	cout << "---------------------------------------------Test fast Fibonacci modulo-------------------------------" << endl; 
	int n = 12;
	bigint m = bigint("11");
	Fibonacci *fib = new Fibonacci();	
	bigint f = fib->FastDoublingFibonacci(n);
	cout <<  "The" << n << "th Fibonacci Number:" <<  f << endl;	
	
	bigint ff = fib->FastModulo(n, m);	
	cout << "The " << n << "th Fibonacci Number modulo " << m << " is " << ff << ",correct answer:" << f%m << endl;
	cout << endl;

	if (NULL != fib) { delete fib; fib = NULL; }

	cout << "---------------------------------------------Test sort fuction--------------------------------" << endl;
	std::vector<bigint> vv;
	vv.push_back(bigint("4"));
	vv.push_back(bigint("2"));
	vv.push_back(bigint("3"));
	vv.push_back(bigint("1"));
	std::vector<bigint> idx = fib->SortVec(vv);
	cout << "sort result" << endl;
	for (size_t i = 0; i < idx.size(); i++)
	{		
		cout << vv[i] << "," << idx[i] << endl;
	}
	cout << endl;
		
	cout << "---------------------------------------------Test prime table--------------------------------" << endl; 
	const struct tm *start = Util::NowTime();
	const char* paths[2]{"D:\\wls\\Fib\\Fib\\Debug\\01.csv", "D:\\wls\\Fib\\Fib\\Debug\\02.csv"};
	fib = new Fibonacci(paths);
	cout << "The prime number count:" << fib->_primes.size() << endl;
	if (NULL != fib) { delete fib; fib = NULL; }
	const struct tm *end = Util::NowTime();	
	cout << "Time used:" << Util::TimeSpan(start,end) << " secs" << endl;
	cout << endl;


	cout << "---------------------------------------------Test factorization--------------------------------" << endl;
	bigint p1 = bigint(701);
	bigint p2 = bigint(4051);
	bigint N = p1*p2;
	fib->GetPisanoPeriod(N);
	getchar();
	return 0;
}

