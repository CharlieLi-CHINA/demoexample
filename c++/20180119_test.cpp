#include <iostream>
#define pi 3.1415926 //�����
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
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
	//��������
	//���Ǻ�����Ĭ����ʹ�û����ƣ����㹫ʽ��U/�� = A/180������U��A�ֱ��ǻ��ȺͽǶ�
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
	//����ֵ
	cout << "a,abs(a):" << a3 << "," << abs(a3) << endl;
	//ƽ����
	cout << "a,sqrt(a):" << a4 << "," << sqrt(a4) << endl;
	//a ��2�η�
	cout << "a,pow(a,2):" << a5 << "," << pow(a5,2) << endl;

	//�����
	//��������
	srand( ( unsigned ) time ( NULL ) );
	/*����ʵ�ʵ��������10��*/
	for (i = 0; i < 10; i++)
	{
		j = rand();
		cout << "The random number is :" << "\t"<< j << endl;
	}
	cin.get();
	return 0;

}

