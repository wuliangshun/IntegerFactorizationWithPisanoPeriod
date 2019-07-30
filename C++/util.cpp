#include "util.h"
#include <stdarg.h>

#pragma warning(disable:4996)


void Util::Log(const char* strFormat, ...)
{
#ifdef PRINT_USER_HEAP_SIZE
	const int MAX_OUTPUT_LEN = 65534;
#else
	const int MAX_OUTPUT_LEN = 20480;
#endif

	const int nBufSize = MAX_OUTPUT_LEN + 1;
	va_list vArgs;
	va_start(vArgs, strFormat);

#ifdef PRINT_USER_HEAP_SIZE
	char* strBuf = new char[nBufSize];
#else
	char strBuf[nBufSize];
#endif	
	memset(strBuf, sizeof(strBuf), 0);
	vsnprintf(strBuf, nBufSize-1, strFormat, vArgs);

	cout << strBuf;

#ifdef PRINT_USER_HEAP_SIZE
	delete[] strBuf;
#else	
#endif
	va_end(vArgs);
}

std::vector<char*> Util::SplitBuff(char* buff, const  char* d)
{
	std::vector<char*> vec;
	char *p;
	p = strtok(buff, d);
	while (p != NULL)
	{
		vec.push_back(p);
		p = strtok(NULL, d);
	}
	return vec;
};

const struct tm* Util::NowTime()
{
	struct tm *p;
	time_t t;
	time(&t);
	p = localtime(&t);
	return p;
}

_int64 Util::TimeSpan(const struct tm* start, const struct tm* end)
{
	time_t s = mktime((tm*)start);
	time_t e = mktime((tm*)end);
	
	MAKE_HHMMSS(start->tm_hour, start->tm_min, start->tm_sec);


	char s_str[1024] = { 0 };
	sprintf(s_str, "%d", s);	
	_int64 s_int = atoi(s_str);
	cout << "start:" << s_int << endl;
	
	char e_str[1024] = { 0 };
	sprintf(e_str, "%d", e);
	_int64 e_int = atoi(e_str);
	cout << "end:" << e_int << endl;

	return e_int - s_int;
};
