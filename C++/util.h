#ifndef _UTIL_H_
#define _UTIL_H_

#include <vector>
#include <iostream>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>

#pragma warning(disable:4996)

#define PRINT_USER_HEAP_SIZE
#define MAKE_HHMMSS(h, m, s) ((h)*10000 + (m)*100 + (s))
#define _int64 long long


using namespace std;

class Util
{
public:
	static std::vector<char*> SplitBuff(char* buff, const char* d);	
	static const struct tm* NowTime();	
	static _int64 TimeSpan(const struct tm* start, const struct tm* end);
	static void Log(const char* strFormat, ...);
};

#endif
