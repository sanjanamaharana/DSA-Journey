# include <iostream>
using namespace std;
int main() {
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}

// for i in range(1,7):
//     for j in range(1,i+1):
//         print(j, end="")
//     print("")


// 1
// 12
// 123
// 1234
// 12345

