#include <iostream>
using namespace std;
//运算符练习
int main()
{
	int a = 21;
	int b = 10;
	int c;
	cout << "a和b的值是" << a <<","<< b << endl;
	c = a + b;
	cout << "Line 1 - c=a+b 的值是" << c << endl;
	c = a - b;
	cout << "Line 2 - c=a-b的值是" << c << endl;
	c = a / b;
	cout << "Line 3 - c=a/b的值是" << c << endl;
	c = a % b;
	cout << "Line 4 - c=a%b的值是" << c << endl;
	c = a * b;
	cout << "Line 5 - c=a*b的值是" << c << endl;

	int d = 10;//测试自增自减
	cout << "c的值是" << d  << endl;
	c = d++;
	cout << "Line 6 - c自增的值是" << c << endl;

	d = 10;//重新赋值
	c = d--;
	cout << "Line 6 - c自减的值是" << c << endl;

	cin.get();
	return 0;
}