import time
import hashlib
import pyfiglet
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('SHAR.PY'))

def stringinput():

 a_string = input ("enter the sentence you want to encrypt\n\n")

 print ("\n")
 time.sleep(1)

 print ("Sentence is: " + a_string)
#maybe add something here - is this correct if yes continue if no redo the string input function
 time.sleep(1)

 hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()

 print ("\nyour hashed sentence is:")

 time.sleep(1)

 print (hashed_string)

 endprocessoption()

def fileencryption():

 filepath = input ("Please enter the full file path of the file you want to encrypt\n\n File Path : ")

 with open(filepath , 'rb') as f:
  for line in f:
    hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
    print (hashed_line)
 endprocessoption()

def usrsel():

 option = input ("\nplease select string or file to encript.\n\n file : [1] \n \n string : [2] \n \n Input: ")
 if option == ("1"):
      fileencryption()
 if option == ("2"):
           stringinput()
 else:
     usrsel()

def end():
 print("\n\ngoodbye")
 time.sleep(2)

def endprocessoption():
 opt = input ("\n\nwould you like to encrypt some more data? \n y/n?")
 if opt == ("y"):
    usrsel()
 else:
     end()



usrsel()


#thoughts - modify the utf encoding? maybe find a way to import fancy figlet stuff?
#perhaps instead of outputting the hashed file contents into the prompt maybe put the contents
#into a new hashed.txt. file -- hashedfile n+1 -- python open or close file creation? with and as commands?