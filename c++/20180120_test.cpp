#include <iostream>
#define pi 3.1415926 //�����
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;

#include <iomanip>
using std::setw;
/*
�������е��ú���ʱ��Ҫô�����ܺ���д��������ǰ�棬Ҫô���չ��ܺ������ø�ʽ���ã��������׳�������
int sum(int x, int y =20)�У��������ʱֻ��sum��a��������һ����������ô�����sum����д������������ͻ���ִ���
*/
int sum(int x, int y = 20)
{
	//ʵ����������͹��ܵĺ���
	cout << "The two input is:" << x << "," << y << endl;
	int result;
	result = x + y;
	cout << "The sum is:" << result << endl;
	return (result);
}

double Hudu2Jiaodu(double x=0)
{
	//ʵ�ֻ��ȵ��Ƕȵı任
	double jiaodu;
	jiaodu = pi * x / 180;
	return (jiaodu);
}
int main()
{

	//����
	int n[10];//һ������10������������

	//��ʼ������
	for (int i = 0; i < 10; i++)
	{
		n[i] = i + 100;

	}
	cout << "Element" << setw(13) << "Value" << endl;

	//���
	for (int j = 0; j < 10; j++)
	{
		cout << setw(7) << j << setw(13) << n[j] << endl;

	}

	//�ַ���
	char greeting[6] = { 'H', 'e', 'l', 'l', 'o', '\0' };
	cout << endl;
	cout << "Greeting message: ";
	cout << greeting << endl;

	//ָ��
	int var[20];//ʵ�ʱ���
	int *ip;//ָ�����
	cout << endl;
	cout << "Element" << setw(15) << "Value" << endl;

	for (int i = 0; i < 20; i++)
	{
		var[i] = i + 100;
		cout << setw(5) << i << setw(15) << var[i] << endl;
		ip = &var[i];
	}
	ip = &var[0];//������ɣ���ָ��ָ��������Ԫ��

	cout << endl<< endl;
	cout << "Value of *ip variable:"<<endl;
	for (int i = 0; i < 20; i++)
	{
		cout << setw(5) << i << setw(15) << *ip << endl;
		ip++;
	}

	//����
	int z = 3;
	int& zz = z;
	cout << "The value of z:" << z << "\t" << endl;
	cout << "The value of zz(the yinyong of z):" << zz;
	cin.get();
	return 0;

}

