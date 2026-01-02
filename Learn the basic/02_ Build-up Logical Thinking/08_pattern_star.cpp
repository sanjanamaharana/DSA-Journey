#include <iostream>
using namespace std;

int main() {
    int n = 5;

    for (int i = 0; i < n; i++) {
        // spaces
        for (int j = 0; j < i; j++) {
            cout << " ";
        }

        // stars
        for (int j = 0; j < 2 * (n - i) - 1; j++) {
            cout << "*";
        }

        cout << endl;
    }
    return 0;
}




#include <iostream>
using namespace std;

int main() {
    int n=5;
    for (int i = n; i >=0; i--) {
        //space
        for(int j=n-i-1;j>0;j--){
            cout<< " ";
        }
        //star
        for(int j=2*i+1; j>0;j--){
            cout<< "*";
        }
        //space
        for(int j=n-i-1;j>0;j--){
            cout<< " ";
        }
        cout<< endl;
    }
    return 0;
}



//***********
// *********
//  ******* 
//   *****  
//    ***   
//     *    


#include <iostream>
using namespace std;

int main() {
    int n=5;
    for (int i = n; i >=0; i--) {
        //space
        for(int j=0;j<n-i-1;j++){
            cout<< " ";
        }
        //star
        for(int j=0; j<2*i+1;j++){
            cout<< "*";
        }
        //space
        for(int j=0;j<n-i-1;j++){
            cout<< " ";
        }
        cout<< endl;
    }
    return 0;
}

// ***********
// *********
//  ******* 
//   *****  
//    ***   
//     *    