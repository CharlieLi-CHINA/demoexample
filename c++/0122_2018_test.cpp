#include <iostream>
#include <cstring>
using namespace std;
void printBook(struct Books book);

//���ݽṹ��ʹ��
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
int main()
{
	Books Book1, Book2;
	//Books Book2;

	//Book1
	strcpy(Book1.title, "Pyhton �̳�");
	strcpy(Book1.author, "EUHFGI");
	strcpy(Book1.subject, "���������");
	Book1.book_id = 652851;

	//Book2
	strcpy(Book2.title, "C++�����ŵ�����");
	strcpy(Book2.author, "AJDKF");
	strcpy(Book2.subject, "�������");
	Book2.book_id = 528674;

	printBook(Book1);
	printBook(Book2);

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
