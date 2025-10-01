name1=str(input("Enter your name: "))
name2=str(input("Enter your partner name: "))
Bothnames=name1+name2
s_letters=Bothnames.lower()
t=s_letters.count('t')
r=s_letters.count('r')
u=s_letters.count('u')
e=s_letters.count('e')
true=t+r+u+e
l=s_letters.count('l')
o=s_letters.count('o')
v=s_letters.count('v')
e=s_letters.count('e')
love=l+o+v+e
lovescore = int(str(true) + str(love))
if lovescore < 10 or lovescore > 90:
    print("You are made for each other.")
elif lovescore <= 40 or lovescore >= 50:
    print("You are very lucky to have your partner.")
else:
    print("You are the unique couple in the world.")
