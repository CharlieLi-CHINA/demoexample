#include <iostream>
#include <cstring>
using namespace std;
void printBook(struct Books book);//��������

//��&���ݽṹ��ʹ��
/*
�������е��ú���ʱ��Ҫô�����ܺ���д��������ǰ�棬Ҫô���չ��ܺ������ø�ʽ���ã��������׳�������
int sum(int x, int y =20)�У��������ʱֻ��sum��a��������һ����������ô�����sum����д������������ͻ���ִ���
*/

//����һ���ṹ������
struct Books
{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
};

//��
class Box
{
public:
	double length;
	double breadth;
	double height;
};

int main()
{
	Books Book1, Book2; //�������ݽṹ��
	Box Box1, Box2; //����Box1/Box2,����ΪBox
	double volume = 0.0; //�洢���
	//Book1 ���ݽṹд������
	strcpy(Book1.title, "Pyhton �̳�");
	strcpy(Book1.author, "EUHFGI");
	strcpy(Book1.subject, "���������");
	Book1.book_id = 652851;

	//Book2 ���ݽṹд������
	strcpy(Book2.title, "C++�����ŵ�����");
	strcpy(Book2.author, "AJDKF");
	strcpy(Book2.subject, "�������");
	Book2.book_id = 528674;

	printBook(Book1); //ִ�к���������Ϊ����õ����ݽṹ
	printBook(Book2);
	cout << "\t" << endl;

	//���ʹ��

	Box1.height = 6.9;
	Box1.length = 23.2;
	Box1.breadth = 9.3;

	Box2.height = 34.2;
	Box2.length = 31.4;
	Box2.breadth = 32.2;

	volume = Box1.height * Box1.length * Box1.breadth;
	cout << "Box1 v = " << volume << endl;
	volume = Box2.height * Box2.length * Box2.breadth;
	cout << "Box2 v = " << volume << endl;
	//���ʹ�����
	cin.get();
	return 0;

}

void printBook( Books book)
{
	cout << "����:" << book.title << endl;
	cout << "����:" << book.author << endl;
	cout << "����:" << book.subject<< endl;
	cout << "ID:" << book.book_id << endl;
	cout << "\t"<<endl;
}
