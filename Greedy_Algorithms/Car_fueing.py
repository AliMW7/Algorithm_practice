"""
Input: A car which can travel at most L
kilometers with full tank, a source
point A, a destination point B and
n gas stations at distances
x1 ≤ x2 ≤ x3 ≤ · · · ≤ xn in
kilometers from A along the path
from A to B.
Output: The minimum number of refills to
get from A to B, besides refill at A.

"""
full_tank = int(input("Full tank ==>"))
number_of_refills = int(input("Number of refills ==>"))
lst_reFills = list(map(int, input("Enter refills with space first number is A and last number is B100 like(0 60 90 100 150 200) ==>").split()))
def min_refills(lst_reFills, number_of_refills, full_tank):
    num_refills = 0
    current_reFills = 0
    while(current_reFills < number_of_refills-1):
        last_reFills = current_reFills
        while(current_reFills < number_of_refills-1 and lst_reFills[current_reFills+1] - lst_reFills[last_reFills] <= full_tank):
            current_reFills += 1
            
        if current_reFills == last_reFills:
            return "IMPOSSIBLE"
        if current_reFills == number_of_refills-1:
            break
        if current_reFills < number_of_refills:
            num_refills += 1

    return num_refills

print(min_refills(lst_reFills, number_of_refills, full_tank))