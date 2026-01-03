#include<iostream>
using namespace std;

int main() {
    // while loop to print numbers from 1 to 100
    int i = 1;
    while(i<=100){
        cout << i << " ";
        i++;
    }
    return 0;
}


// factotial find using while loop

#include<iostream>
using namespace std;

int main() {
  int x ,fact =1;
  cout << "Enter an integer: ";
  cin >> x; 
  int i = 1;
  while(i<=x){
        fact = fact * i;
        i++;
    }
  cout << "Factorial of " << x << " is: " << fact << endl;
  return 0;
}
