# include <iostream>
using namespace std;
int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;
    if (age > 18) {
        cout << "You are an adult." << endl;
    } 
    else if (age == 18) {
        cout << "congratulation! ,You are just an adult." << endl;
    }
    else {
        cout << "You are a minor." << endl;
    }
    return 0;
}