#include <iostream>
#include <cstring>
using namespace std;
void printBook(struct Books book);

//数据结构的使用
/*
主函数中调用函数时，要么将功能函数写在主函数前面，要么按照功能函数调用格式调用，否则容易出错，比如
int sum(int x, int y =20)中，如果调用时只是sum（a）即输入一个参数，那么如果将sum函数写在主函数后面就会出现错误
*/

//声明一个结构体类型
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
	strcpy(Book1.title, "Pyhton 教程");
	strcpy(Book1.author, "EUHFGI");
	strcpy(Book1.subject, "计算机技术");
	Book1.book_id = 652851;

	//Book2
	strcpy(Book2.title, "C++从入门到放弃");
	strcpy(Book2.author, "AJDKF");
	strcpy(Book2.subject, "软件技术");
	Book2.book_id = 528674;

	printBook(Book1);
	printBook(Book2);

	cin.get();
	return 0;

}

void printBook( Books book)
{
	cout << "书名:" << book.title << endl;
	cout << "作者:" << book.author << endl;
	cout << "分类:" << book.subject<< endl;
	cout << "ID:" << book.book_id << endl;
	cout << "\t"<<endl;
}
