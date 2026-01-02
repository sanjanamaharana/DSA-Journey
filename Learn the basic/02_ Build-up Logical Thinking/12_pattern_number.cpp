#include <iostream>
using namespace std;

int main() {
    int n = 6;

    for (int i = 1; i < n; i++) {
        // numbers increasing
        for (int j = 1; j < i; j++) {
            cout << j;
        }

        // spaces
        for (int j = 1; j < 2 * (n - i) - 1; j++) {
            cout << " ";
        }
        // numbers decreasing
        for (int j = i-1; j >= 1; j--) {
            cout << j;
        }

        cout << endl;
    }
    return 0;
}

// 1      1
// 12    21
// 123  321
// 12344321