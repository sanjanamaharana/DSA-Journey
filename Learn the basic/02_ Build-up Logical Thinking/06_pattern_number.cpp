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

// 54321
// 4321
// 321
// 21
// 1


# include <iostream>
using namespace std;
int main() {
    for(int i=5; i>=1; i--) {
        for(int j=1; j>=5; j++) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}

// 12345
// 1234
// 123
// 12
// 1