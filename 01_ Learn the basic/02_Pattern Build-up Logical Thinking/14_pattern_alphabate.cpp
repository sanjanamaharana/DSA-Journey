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
// count = 64
// for i in range(1,7):
//     for j in range(1,i+1):
//         print(chr(count+j)," ", end="")
//     print("")


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
// count = 64
// for i in range(6,0,-1):
//     for j in range(1,i):
//         print(chr(count+j)," ", end="")
//     print("")


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

// count = 64
// for i in range(5,0,-1):
//     for j in range(i,0,-1):
//         print(chr(count+i)," ", end="")
//     print("")


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
// count = 64
// for i in range(0,6):
//     for j in range(0,i+1):
//         print(chr(count+i)," ", end="")
//     print("")


// A
// BB
// CCC
// DDDD
// EEEEE

// count = 69
// for i in range(0,6):
//     for j in range(0,i+1):
//         print(chr(count-i)," ", end="")
//         # count += 1
//     print("")
// E  
// D  D  
// C  C  C  
// B  B  B  B  
// A  A  A  A  A  