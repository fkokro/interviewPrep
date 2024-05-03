"""You have the option to roll a die up to three times. You will earn the face value of the die. 
You have the option to stop after each throw and walk away with the money earned. 
The earnings are not additive. What is the expected payoff of this game?"""

Solution

"""
To find the expected value of the third roll, we must find the expected value of the 2nd and 1st role.
The expected value 1st role:
"""

"""

fair sided die (x) = 1/6
{1,2,3,4,5,6}

EV1 = sum(x_i*p(x_i))
EV1 = [(1/6)*(1+2+3+4+5+6)] = [(1/6) * 21] = 3.5
Since the expected value for the first role is 3.5, we will only role again if this number isn't met or exceeded.
Given our target outcome is not met ie 4,5,6 - the second role expected value is the expected value of throw 1 and throw 2 given the above outcomes.

EV2 = [(1/2)EV1 + (1/2)EV(4,5,6)] = [(1/2)*3.5 + (1/2)*(1/3*[4+5+6])] = 4.25


Same logic applies for roll three, we would only roll again if expect value for roll 2 not met, since the expected value is 4.25
EV3 = [(1/2)EV2 +(1/2)EV3] = [(1/2)*4.25 +(1/2)(1/3*4+5+6)] = 4.67

Now, the overall expected value is 
e[x] = [(2/3)*4.25 + (1/3) * (1/2)(5+6)] = 4.67
"""