#include <iostream>
using namespace std;

int main() {
    int n = 5;
    for (int i = 0; i < n; i++) {
        //space
        for(int j=0;j<n-i-1;j++){
            cout<< " ";
        }
        //star
        for(int j=0; j<2*i+1;j++){
            cout<< "*";
        }
        
        cout<< endl;
    }
    for (int i = 0; i < n; i++) {
        // spaces
        for (int j = 0; j < i; j++) {
            cout << " ";
        }

        // stars
        for (int j = 0; j < 2 * (n - i) - 1; j++) {
            cout << "*";
        }

        cout << endl;
    }
    return 0;
}




//     *
//    ***
//   *****
//  *******
// *********
// *********
//  *******
//   *****
//    ***
//     *


// for i in range(0,5):
//     for j in range(0,5-i-1):
//         print(" ", end="")
//     for k in range(0,2*i+1):
//         print("*", end="")
//     print("")
// for i in range(0,6):
//     for j in range(0,i):
//         print(" ", end="")
//     for k in range(0,2 * (5 - i) - 1):
//         print("*", end="")
//     print("")
