#include <iostream>

int main(){
    
    std::string full_name;
    int age3;

    std::cout<< "Please type your full name and age " <<std::endl;

    std::getline(std::cin,full_name);

    std::cin >> age3;

    std::cout<<"hello "<< full_name << "you are " << age3 << " years old!" << std::endl;

    return 0;

}