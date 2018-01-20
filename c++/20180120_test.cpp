#include <iostream>
#define pi 3.1415926 //定义π
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;

#include <iomanip>
using std::setw;
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

	//数组
	int n[10];//一个包含10个整数的数组

	//初始化数组
	for (int i = 0; i < 10; i++)
	{
		n[i] = i + 100;

	}
	cout << "Element" << setw(13) << "Value" << endl;

	//输出
	for (int j = 0; j < 10; j++)
	{
		cout << setw(7) << j << setw(13) << n[j] << endl;

	}

	//字符串
	char greeting[6] = { 'H', 'e', 'l', 'l', 'o', '\0' };
	cout << endl;
	cout << "Greeting message: ";
	cout << greeting << endl;

	//指针
	int var[20];//实际变量
	int *ip;//指针变量
	cout << endl;
	cout << "Element" << setw(15) << "Value" << endl;

	for (int i = 0; i < 20; i++)
	{
		var[i] = i + 100;
		cout << setw(5) << i << setw(15) << var[i] << endl;
		ip = &var[i];
	}
	ip = &var[0];//操作完成，将指针指回数组首元素

	cout << endl<< endl;
	cout << "Value of *ip variable:"<<endl;
	for (int i = 0; i < 20; i++)
	{
		cout << setw(5) << i << setw(15) << *ip << endl;
		ip++;
	}

	//引用
	int z = 3;
	int& zz = z;
	cout << "The value of z:" << z << "\t" << endl;
	cout << "The value of zz(the yinyong of z):" << zz;
	cin.get();
	return 0;

}

