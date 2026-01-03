#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int num;
  cout << "Enter an integer: ";
  cin >> num;
  int digitCount = log10(num)+1;

  cout << "Number of digits in " << num << " is: "<< digitCount << endl;
  return 0;
  
}



// You are given an integer n. You need to return the number of digits in the number.



// The number will have no leading zeroes, except when the number is 0 itself.


// Example 1

// Input: n = 4

// Output: 1

// Explanation: There is only 1 digit in 4.

// Example 2

// Input: n = 14

// Output: 2

// Explanation: There are 2 digits in 14.

// Now your turn!

// Input: n = 234

// Output:3

// 0(log₁₀N)