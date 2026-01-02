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

// E
// DE
// CDE
// BCDE
// ABCDE