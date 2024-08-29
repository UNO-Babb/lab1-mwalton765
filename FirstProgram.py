#FirstProgram.py
#Name: Michael J. Walton
#Date: 8/28/2024
#Assignment: Lab 1 First Program

def main():
  print("First Program")
  #Say hello
  print('Hello')
  #Ask for the user's name
  name = input('What is your name? ')
  #Use the user's name in the program.
  print('Hello', name)
  #Ask the user for their age.
  age = input('What is your age? ')
  age = int(age)
  born = 2024 - age
  #Tell the user what year they were born in.
  print('You were born in', born)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
