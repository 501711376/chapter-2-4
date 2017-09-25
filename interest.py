p=10000
r=0.08
n=12
t=input("how many years are you investing for?")
t=float(t)
A=p * ( (1+r/n) **(n*t) )
print("Your final amount after",t,"years will be:",A)
