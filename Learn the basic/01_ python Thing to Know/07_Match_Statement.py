# it is similar to switch case (C++,c) but not same

rollno = int(input("Enter your Roll number : "))

match rollno:
  case 1:
    print("sanjana")
  case 2:
    print("Prabhat")
  case 3:
    print("rahul")
  case 4:
    print("khusi")
  case _:
    print("you are not in this group.")

num = int(input(" Enter a day number (1–7)"))

match num:
  case 1:
    print("Sunday")
  case 2:
    print("Monday")
  case 3:
    print("Tuesday")
  case 4:
    print("Wednesday")
  case 5:
    print("Thursday")
  case 6:
    print("Friday")
  case 7:
    print("Saturday")
  case _:
    print("enter between 1-7")