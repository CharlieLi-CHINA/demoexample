#include <iostream>
using namespace std;
//�������ϰ
int main()
{
	int a = 21;
	int b = 10;
	int c;
	cout << "a��b��ֵ��" << a <<","<< b << endl;
	c = a + b;
	cout << "Line 1 - c=a+b ��ֵ��" << c << endl;
	c = a - b;
	cout << "Line 2 - c=a-b��ֵ��" << c << endl;
	c = a / b;
	cout << "Line 3 - c=a/b��ֵ��" << c << endl;
	c = a % b;
	cout << "Line 4 - c=a%b��ֵ��" << c << endl;
	c = a * b;
	cout << "Line 5 - c=a*b��ֵ��" << c << endl;

	int d = 10;//���������Լ�
	cout << "c��ֵ��" << d  << endl;
	c = d++;
	cout << "Line 6 - c������ֵ��" << c << endl;

	d = 10;//���¸�ֵ
	c = d--;
	cout << "Line 6 - c�Լ���ֵ��" << c << endl;

	cin.get();
	return 0;
}