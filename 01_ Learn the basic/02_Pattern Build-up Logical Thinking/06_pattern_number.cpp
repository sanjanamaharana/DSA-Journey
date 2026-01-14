# include <iostream>
using namespace std;
int main() {
    for(int i=5; i>=1; i--) {
        for(int j=i; j>0; j--) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}
// for i in range(5, 0,-1):
//     for j in range(i,0,-1):
//         print(j, end="")
//     print("")


// 54321
// 4321
// 321
// 21
// 1


# include <iostream>
using namespace std;
int main() {
    for(int i=5; i>=1; i--) {
        for(int j=1; j>=i; j++) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}

// for i in range(6, 0,-1):
//     for j in range(1,i):
//         print(j, end="")
//     print("")


// 12345
// 1234
// 123
// 12
// 1