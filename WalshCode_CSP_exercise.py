import numpy as np

def walsh_code(n):
    n=int(n)
    if n == 1:
        return np.array([1])
    else:
        prev_code = walsh_code(n - 1)
        upper = np.hstack((prev_code, prev_code))
        lower = np.hstack((prev_code, -prev_code))
        return np.vstack((upper, lower))
q='q'
while True:
    n = input("\033[32m  Please enter the Order of Walsh Code that you want to generate , or enter 'q' to quit: ")  # Number of Walsh codes
    if n.isdigit() and int(n) >=1:
        print(walsh_code(n))
        continue
    elif n.isdigit() and int(n) <= 0:
        print("\033[34m The value of n should be greater than or equal to 1")
        continue

    elif n==q:
        print(" \033[37m Good Bye, Program to generate Walsh codes has been suspended.")
        break
    else:
        print (" \033[31m Error,  Enter a Valid Key... ")

