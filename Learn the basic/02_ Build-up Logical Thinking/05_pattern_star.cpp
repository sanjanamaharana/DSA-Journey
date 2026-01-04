# include <iostream>
using namespace std;
int main() {
    for(int i=5; i>=1; i--) {
        for(int j=i; j>0; j--) {
            cout << "*" ;
        }
        cout << endl;
    }
    return 0;
}

// for i in range(5, 0,-1):
//     for j in range(i,0,-1):
//         print("*", end="")
//     print("")


// *****
// ****
// ***
// **
// *

// for i in range(0,6):
//     for j in range(0,n-1):
//         print("*", end="")
//     print("")