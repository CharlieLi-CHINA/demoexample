#include <iostream>
using namespace std;
extern int a1, b1;
extern int c1;
extern float f1;
void func(void);
int hht;
extern void write_extern();
static int countt = 10;
enum time1
{
	first, second,
	third, forth, fifth
};
int main()
{
	enum time1 a = fifth;
	int aa, a1, b1, c1;
	float f1;
	a1 = 10;
	b1 = 20;
	c1 = a1 + b1;
	cout << c1 << endl;

	f1 = 70.0 / 3.0;
	cout << f1 << endl;
	cout << "Size of char : " << sizeof(char) << endl;
	cout << "Size of int : " << sizeof(int) << endl;
	cout << "Size of short int : " << sizeof(short int) << endl;
	cout << "Size of long int : " << sizeof(long int) << endl;
	cout << "Size of float : " << sizeof(float) << endl;
	cout << "Size of double : " << sizeof(double) << endl;
	cout << "Size of wchar_t : " << sizeof(wchar_t) << endl;
	aa = 2;
	if (aa == 2)
	{
		cout << "liqilv is a man" << endl;
		cout << a << endl;
	}
	while ( countt --)
	{
		func();
	}
	hht = 5;
	write_extern();
	return 0;
}
void func(void)
{
	static int i = 5; // 局部静态变量
	i++;
	std::cout << "变量 i 为 " << i;
	std::cout << " , 变量 count 为 " << countt << endl;
}