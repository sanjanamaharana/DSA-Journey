#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int num;
  cout << "Enter an integer: ";
  cin >> num;
  int revnum =0;
  while(num>0){
      int rem = num % 10;
       num = num/10;
                 
      if (revnum > INT_MAX / 10 || (revnum == INT_MAX / 10 && rem > 7))
                return 0;

     if (revnum < INT_MIN / 10 || 
               (revnum == INT_MIN / 10 && rem < -8))
                return 0;

       revnum = (revnum*10)+rem;
  }
  if(revnum==num){
      cout<<"this is palindrome number";
      
  }
  
  
  cout<<revnum;
  
}
// Enter an integer: 10400 
// 401

// O(log₁₀N),