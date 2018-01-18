#include <iostream>
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

int main()
{
	//求和
	int a=100, b=200;
	int result;
	result = sum(a, b);
	result = sum(a);
	cin.get();//让控制台显示结果并停留
	return 0;

}

