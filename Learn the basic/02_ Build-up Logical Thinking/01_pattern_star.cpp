# include <iostream>
using namespace std;
int main() {
    for(int i=0; i<=5; i++) {
        for(int j=0; j<=5; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
// for i in range(5):
//     for j in range(5):
//         print("*", end="")
//     print(" ")


// * * * * * * 
// * * * * * * 
// * * * * * * 
// * * * * * * 
// * * * * * * 
// * * * * * * 

# include <iostream>
using namespace std;
int main() {
    int n = 5;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(i==0 || j ==0 || i == n-1 || j== n-1 ){
                cout<< "*" ;
            }
            else{
                cout<< " ";
            }
        }
        cout << endl;
    }
    return 0;
}
// for i in range(5):
//     for j in range(5):
//         if(i==0 or j ==0 or i == 5-1 or j== 5-1 ):
//             print("*", end="")
//         else:
//             print(" ", end="")
//     print(" ")

// *****
// *   *
// *   *
// *   *
// *****