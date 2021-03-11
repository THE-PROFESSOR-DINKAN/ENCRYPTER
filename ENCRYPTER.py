# script is made by referring vu1n3rable script
#special thanks to  vu1n3rable for helping
from pyfiglet import Figlet
#this commad is for making banner
def banner(word):
custom_fig =Figlet(font='banner3-D')
print(custom_fig.renderText(word))
banner("ENCRYPTER")
print("                                             version 1.0")

print("""                      
                  DISCLIMER:
        """)
print("........................................................")
print("          # DON'T USE LOWER CASE ALBHABET")
print("          #DON'T USE NUMBERS   ")
print("          #DON'T USE SPECIAL CHARACTERS")
print("          #USE ONLY UPPER CASE ALBHABETS")
  #this program is designed to make an encription for the texts only in upper case.
  
A = "d0c"
B = "ce3"
C = "42c"
D = "728"
E = "653"
F = "652"
G = "b06"
H = "280"
I = "05b"
J = "a09"
K = "da5"
L = "e61"
M = "072"
N = "bc3"
O = "572"
P = "1b6"
Q = "41b"
R = "c83"
S = "5b9"
T = "7ac"
U = "e10"
V = "274"
W = "c8c"
X = "01a"
Y = "a91"
Z = "e48"



while True:
  result = ""
  input_text = ""
  wrong_input = ""
  condition = ""
  wrong_data =['a','b','c','d','e','f','g','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
  inp = input("ENTER THE TEXT TO CONVERT INTO HASH :")
  for i in wrong_data:
    if i in input_text:
      print("USED WRONG FORMAT NO LOWERCASE LETTERS AND NUMBERS")
      condition = "False"
      break
      continue

  if "False" in condition:
      continue
  else:
    length = len(inp)

  for i in range (length):
    if inp[i] == 'A':
      result += A

    elif inp[i] =='B':
      result += B  

    elif inp[i] =='C':
      result += C  

    elif inp[i] =='D':
      result += D

    elif inp[i] =='E':
      result += E   

    elif inp[i] =='F':
      result += F  

    elif inp[i] =='G':
      result +=G   

    elif inp[i] =='H':
      result += H  

    elif inp[i] =='I':
      result+= I 

    elif inp[i] =='J':
      result+= J 

    elif inp[i] =='K':
      result+= K

    elif inp[i] =='L':
      result+=   L
    
    elif inp[i] =='M':
      result+=  M

    elif inp[i] =='N':
      result+=   N
    
    elif inp[i] =='O':
      result+=  O

    elif inp[i] =='P':
      result+=   P
  
    elif inp[i] =='Q':
      result+=  Q

    elif inp[i] =='R':
      result+=   R
   
    elif inp[i] =='S':
      result+=  S

    elif inp[i] =='T':
      result+=   T
   
    elif inp[i] =='U':
      result+=  U

    elif inp[i] =='V':
      result+=   V

    elif inp[i] =='W':
      result+=  W

    elif inp[i] =='X':
      result+=   X

    elif inp[i] =='Y':
      result+=  Y

    elif inp[i] =='Z':
      result+=   Z


    else:
      print("YOU HAVE ENTERED AN UNSUPPORTED CHARECTOR")
      wrong_input = 'True'
      break

  if wrong_input =='True':
    continue
        
  else:
    print('YOUR HASH IS   : {}'.format(result))
