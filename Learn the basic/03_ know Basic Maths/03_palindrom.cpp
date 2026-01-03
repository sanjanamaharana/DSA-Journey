#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int nu,num;
  cout << "Enter an integer: ";
  cin >> nu;
  num = nu;
  int revnum =0;
  while(num!=0){
      int rem = num % 10;
       num = num/10;


       revnum = (revnum*10)+rem;
  }
  if(revnum==nu){
      cout<<"this is palindrome number";
      
  }
  
  
  cout<<revnum;
  
}
//  palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

// Time Complexity: O(log10N + 1), as in the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1. In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations. In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into the vector.