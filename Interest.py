p=int(input("Enter the principal : "))
r=int(input("Enter the rate : "))
t=int(input("Enter the time : "))
SI = (p*r*t)/100
print(SI)
CI = p*(1+(r/100))**t
print(CI)