#include <iostream>
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

int main()
{
	//���
	int a=100, b=200;
	int result;
	result = sum(a, b);
	result = sum(a);
	cin.get();//�ÿ���̨��ʾ�����ͣ��
	return 0;

}

