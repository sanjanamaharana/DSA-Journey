# include <iostream>
using namespace std;
int main() {
    int count =64;
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            cout << static_cast<char>(count+j);
        }
        cout << endl;
    }
    return 0;
}

// A
// AB
// ABC
// ABCD
// ABCDE

# include <iostream>
using namespace std;
int main() {
    int count =64;
    for(int i=5; i>=1; i--) {
        for(int j=1; j<=i; j++) {
            cout << static_cast<char>(count+j);
        }
        cout << endl;
    }
    return 0;
}

// ABCDE
// ABCD
// ABC
// AB
// A

# include <iostream>
using namespace std;
int main() {
    int count =64;
    for(int i=5; i>=1; i--) {
        for(int j=1; j<=i; j++) {
            cout << static_cast<char>(count+i);
        }
        cout << endl;
    }
    return 0;
}
// EEEEE
// DDDD
// CCC
// BB
// A

# include <iostream>
using namespace std;
int main() {
    int count =64;
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            cout << static_cast<char>(count+i);
        }
        cout << endl;
    }
    return 0;
}

// A
// BB
// CCC
// DDDD
// EEEEE