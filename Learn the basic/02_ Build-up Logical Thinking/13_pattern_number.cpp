# include <iostream>
using namespace std;
int main() {
    int count =1;
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            
            cout << count<<" ";
            count++;
        }
        cout << endl;
    }
    return 0;
}

// count =1
// for i in range(1,7):
//     for j in range(1,i+1):
        
//         print(count," ", end="")
//         count += 1
//     print("")

// 1 
// 2 3 
// 4 5 6 
// 7 8 9 10 
// 11 12 13 14 15 


# include <iostream>
using namespace std;
int main() {
    int count =65;
    for(int i=0; i<=5; i++) {
        for(int j=1; j<=i; j++) {
            
            cout << static_cast<char>(count)<<" ";
            count++;
        }
        cout << endl;
    }
    return 0;
}

// A 
// B C 
// D E F 
// G H I J 
// K L M N O 

// count = 65
// for i in range(1,7):
//     for j in range(1,i+1):
//         print(chr(count)," ", end="")
//         count += 1
//     print("")