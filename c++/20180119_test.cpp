#include <iostream>
#define pi 3.1415926 //定义π
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
/*
主函数中调用函数时，要么将功能函数写在主函数前面，要么按照功能函数调用格式调用，否则容易出错，比如
int sum(int x, int y =20)中，如果调用时只是sum（a）即输入一个参数，那么如果将sum函数写在主函数后面就会出现错误
*/
int sum(int x, int y = 20)
{
	//实现两个数求和功能的函数
	cout << "The two input is:" << x << "," << y << endl;
	int result;
	result = x + y;
	cout << "The sum is:" << result << endl;
	return (result);
}

double Hudu2Jiaodu(double x=0)
{
	//实现弧度到角度的变换
	double jiaodu;
	jiaodu = pi * x / 180;
	return (jiaodu);
}
int main()
{
	//数字运算
	//三角函数，默认是使用弧度制，换算公式：U/π = A/180，其中U、A分别是弧度和角度
	double a1=45,a2 = 0;
	int a3 = -21;
	long a4 = 1009;
	double a5 = 210.984;
	a2 = Hudu2Jiaodu(a1);
	double b;
	int c1=0,d1=0;
	int i, j;
	//cin >> c1 >> d1;
	//cin.get();
	b = sin(a2);
	cout << "a,sin(a):" << a1 <<","<< b << endl;
	b = cos(a2);
	cout << "a,cos(a):" << a1 << "," << b << endl;
	b = tan(a2);
	cout << "a,tan(a):" << a1 << "," << b << endl;
	//绝对值
	cout << "a,abs(a):" << a3 << "," << abs(a3) << endl;
	//平方根
	cout << "a,sqrt(a):" << a4 << "," << sqrt(a4) << endl;
	//a 的2次方
	cout << "a,pow(a,2):" << a5 << "," << pow(a5,2) << endl;

	//随机数
	//设置种子
	srand( ( unsigned ) time ( NULL ) );
	/*生成实际的随机数，10个*/
	for (i = 0; i < 10; i++)
	{
		j = rand();
		cout << "The random number is :" << "\t"<< j << endl;
	}
	cin.get();
	return 0;

}

