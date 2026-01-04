# include <iostream>
using namespace std;
int main() {
    for(int i=0; i<=5; i++) {
        for(int j=0; j<=i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}

// for i in range(6):
//     for j in range(0,i):
//         print("*", end="")
//     print("")


// * 
// * * 
// * * * 
// * * * * 
// * * * * * 
// * * * * * * 