# include <iostream>
using namespace std;
int main() {
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            cout << i;
        }
        cout << endl;
    }
    return 0;
}

// for i in range(1,7):
//     for j in range(1,i+1):
//         print(i, end="")
//     print("")


// 1
// 22
// 333
// 4444
// 55555
