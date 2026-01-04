#include <iostream>
using namespace std;

int main() {
    int n=5;
    for (int i = 0; i <= n; i++) {
        //star
        for(int j=0;j<=n-i;j++){
            cout<< "*";
        }
        //space
        for(int j=1; j<2*i+1;j++){
            cout<<  " ";
        }
        //star
        for(int j=0;j<=n-i;j++){
            cout<< "*";
        }
        
        cout<< endl;
    }
    for (int i = 0; i <= n; i++) {
        // star
        for (int j = 0; j <= i; j++) {
            cout << "*";
        }

        // space
        for (int j = 1; j <=2 * (n - i) ; j++) {
            cout << " ";
        }
        for (int j = 0; j <= i; j++) {
            cout << "*";
        }

        cout << endl;
    }
    return 0;
}
// for i in range(0,6):
//     for j in range(0,6-i):
//         print("*", end="")
//     for j in range(0,(2*i)+1):
//         print(" ", end="")
//     for j in range(0,6-i):
//         print("*", end="")
//     print("")
// for i in range(0,6):
//     for j in range(0,i+1):
//         print("*", end="")
//     for j in range(0,2*(6-i)-1):
//         print(" ", end="")
//     for j in range(0,i+1):
//         print("*", end="")
//     print("")


// ************
// *****  *****
// ****    ****
// ***      ***
// **        **
// *          *
// *          *
// **        **
// ***      ***
// ****    ****
// *****  *****
// ************



#include <iostream>
using namespace std;

int main() {
    int n=5;
     for (int i = 0; i < n; i++) {
        // spaces
        for (int j = 0; j <= i; j++) {
            cout << "*";
        }

        // stars
        for (int j = 1; j <=2 * (n - i) ; j++) {
            cout << " ";
        }
        for (int j = 0; j <= i; j++) {
            cout << "*";
        }

        cout << endl;
    }
    for (int i = 0; i <= n; i++) {
        //space
        for(int j=0;j<=n-i;j++){
            cout<< "*";
        }
        //star
        for(int j=1; j<2*i+1;j++){
            cout<<  " ";
        }
        //space
        for(int j=0;j<=n-i;j++){
            cout<< "*";
        }
        
        cout<< endl;
    }
   
    return 0;
}

// for i in range(0,6):
//     for j in range(0,i+1):
//         print("*", end="")
//     for j in range(0,2*(6-i)-1):
//         print(" ", end="")
//     for j in range(0,i+1):
//         print("*", end="")
//     print("")
// for i in range(0,6):
//     for j in range(0,6-i):
//         print("*", end="")
//     for j in range(0,(2*i)+1):
//         print(" ", end="")
//     for j in range(0,6-i):
//         print("*", end="")
//     print("")


// *          *
// **        **
// ***      ***
// ****    ****
// *****  *****
// ************
// *****  *****
// ****    ****
// ***      ***
// **        **
// *          *

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n = 4;
    int size = 2 * n - 1;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            int top = i;
            int left = j;
            int right = size - 1 - i;
            int down = size - 1 - j;

            int value = n - min(min(top, left), min(right, down));
            cout << value;
        }
        cout << endl;
    }
    return 0;
}

n = 4
size = 2 * n - 1
for i in range(0,size):
    for j in range(0,size):
        top = i
        left = j
        right = size - 1 - i
        down = size - 1 - j
        value = n - min(top, left, right, down)
        print(value, end="")
       
    print("")



4444444
4333334
4322234
4321234
4322234
4333334
4444444

0 0 0 0 0 0 0   
0 1 1 1 1 1 0
0 1 2 2 2 1 0
0 1 2 3 2 1 0
0 1 2 2 2 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0