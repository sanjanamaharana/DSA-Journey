class Solution {
public:
    bool isPalindrome(int x) {
        
  
  int num = x;
  long revnum =0;
  while(num>0){
      int rem = num % 10;
       num = num/10;
       if(revnum > INT_MAX/10 || revnum< INT_MIN /10)
       return false;
       revnum = (revnum*10)+rem;
  }
  if(revnum==x){
      return true;  
  }
 return false;   
    }
};
// Enter an integer: 10400 
// 401

// O(log₁₀N),

// import math

// x = int(input("Enter number : "))
// num = x
// rev = 0
// while(num != 0):
//     rem = num % 10
//     num //= 10
//     rev = (rev*10)+rem

// if(rev==x):
//     print("success")
// else:
//     print("no")