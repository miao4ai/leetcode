#include <iostream>

int addNumbers(int first_param, int second_param){
    return first_param+second_param;
}

int main(){
    int first_number {3};
    int second_number {7};

    std::cout<< "First number: "<< first_number<<std::endl;
    std::cout<< "Second number: " <<second_number<<std::endl;

    int sum= addNumbers(first_number,second_number);

    std::cout<< "The sum is: " <<sum<<std::endl;
    return 0;
}