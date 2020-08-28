class calc{
	int op1, op2;
	
	public:
		int add(int a, int b);	
		int sub(int a, int b);
		int mul(int a, int b);
		double div(int a, int b);
};

int calc::add(int a, int b){
	return a+b;
}
int calc::sub(int a, int b){
	return a-b;
}
int calc::mul(int a, int b){
	return a*b;
}
double calc::div(int a, int b){
	return (double)a/(double)b;
}

#include<iostream>
using namespace std;

int main(void){
	//class calc 선언된 클래스의 객체 cal을 생성
	calc cal;
	
	std::cout<<"cal.add(10,19)="<<cal.add(10,19)<<std::endl;
	cout<<"cal.sub(14,5)="<<cal.sub(14,5)<<endl;
	cout<<"cal.mul(5,7)="<<cal.mul(5,7)<<endl;
	cout<<"cal.div(20,3)="<<cal.div(20,3)<<endl;
	
	return 0;
}
