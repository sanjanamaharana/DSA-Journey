# include <iostream>
using namespace std;
int main() {
    int count =64, n= 5;
    for(int i=0; i<n; i++) {
        //space
        for(int j=0;j<n-i-1;j++){
            cout<< " ";
        }
        char ch ='A';
        for(int j=0; j<2*i+1;j++){
            int breakpoint = (2*i+1) /2;
            cout<< ch;
            if(j< breakpoint){
                ch++;
                
            }else {
                ch--;
            }
        }
        //space
        for(int j=0;j<n-i-1;j++){
            cout<< " ";
        }
        cout << endl;
    }
    return 0;
}


//     A    
//    ABA   
//   ABCBA  
//  ABCDCBA 
// ABCDEDCBA


# include <iostream>
using namespace std;
int main() {
   for(int i =0;i<=5;i++){
       char ch= 'E';
       for(int j=0;j<i;j++){
           cout<<ch;
           ch--;
       }
       cout<<endl;
   }
    return 0;
}
// count = 69
// for i in range(0,6):
//     for j in range(0,i+1):
//         print(chr(count-j)," ", end="")
//         # count += 1
//     print("")

// E
// ED
// EDC
// EDCB
// EDCBA


# include <iostream>
using namespace std;
int main() {
   for(int i =0;i<5;i++){
       char ch= 'E'-i;
       for(int j=0;j<=i;j++){
           cout<<ch;
           ch++;
       }
       cout<<endl;
   }
    return 0;
}
// count = 64
// for i in range(5,0,-1):
//     for j in range(i,0,-1):
//         print(chr(count+j)," ", end="")
//     print("")


// E
// DE
// CDE
// BCDE
// ABCDE