

# include <iostream>
using namespace std;
int main() {
  //for ineger input
  int x;
  cout << "Enter an integer: ";
  cin >> x; //-2,147,483,648 to 2,147,483,647
  cout << "You entered: " << x << endl;

  //for character input
  char ch;
  cout << "Enter a character: ";
  cin >> ch;      //'a' to 'z', 'A' to 'Z', '0' to '9'
  cout << "You entered: " << ch << endl;

  //for float input
  float f;
  cout << "Enter a float number: ";
  cin >> f;     //1.2e-38 to 3.4e+38
  cout << "You entered: " << f << endl;

  //for double input
  double d;
  cout << "Enter a double number: ";
  cin >> d;     //1.7e-308 to 1.7e+308
  cout << "You entered: " << d << endl;

  //for string input
  string str;
  cout << "Enter a string: ";
  cin >> str;     //sequence of characters
  cout << "You entered: " << str << endl;
   cout << str.length() << endl;    //to find length of string

  //for boolean input
  bool b;
  cout << "Enter a boolean (0 or 1): ";
  cin >> b;    //rue(1) or false(0)
  cout << "You entered: " << b << endl;

  //for long input
  long l;
  cout << "Enter a long integer: "; 
  cin >> l;         //-2,147,483,648 to 2,147,483,647 or -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
  cout << "You entered: " << l << endl;

  //for short input
  short s;
  cout << "Enter a short integer: ";
  cin >> s;     //-32,768 to 32,767
  cout << "You entered: " << s << endl;

  //for unsigned int input
  unsigned int u;
  cout << "Enter an unsigned integer: ";
  cin >> u;     //0 to 4,294,967,295
  cout << "You entered: " << u << endl;


//for long long input
  long long ll;
  cout << "Enter a long long integer: ";
  cin >> ll;      //-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
  cout << "You entered: " << ll << endl;

  //for unsigned long input
  unsigned long ul;
  cout << "Enter an unsigned long integer: ";
  cin >> ul;      //0 to 4,294,967,295 or 0 to 18,446,744,073,709,551,615
  cout << "You entered: " << ul << endl;

  //for unsigned short input
  unsigned short us;
  cout << "Enter an unsigned short integer: ";
  cin >> us;        //0 to 65,535
  cout << "You entered: " << us << endl;

   // Printing the size of each data type
    cout << "Size of int: " << sizeof(int) << " bytes" << endl;
    cout << "Size of char: " << sizeof(char) << " byte" << endl;
    cout << "Size of float: " << sizeof(float) << " bytes" << endl;
    cout << "Size of double: " << sizeof(double) << " bytes"; << endl;


//     Size of int: 4 bytes
// Size of char: 1 byte
// Size of float: 4 bytes
// Size of double: 8 bytes

  return 0;
}


// Data Type 	Meaning	Typical Size (in Bytes)	Description
// bool	Boolean	1	Stores true or false values.
// char	Character	1	Stores a single character or small integer value.
// short	Short Integer	2	Stores small whole numbers.
// int	Integer	4	The standard integer type for general use.
// long	Long Integer	4 or 8	Used for larger integers.
// long long	Very Long Integer	8	Used for very large integer values.
// float	Floating-point	4	Stores fractional numbers with 6-7 digits of precision.
// double	Double Floating-point	8	Stores fractional numbers with about 15 digits of precision.
// long double	Extended precision float	8, 12, or 16	Provides even greater precision.
// wchar_t	Wide Character	2 or 4	Used for characters that require more memory (e.g., Unicode).