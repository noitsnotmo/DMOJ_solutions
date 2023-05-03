
# DMOJ Problem wc18c3j1, An Honest Day's Work

# Input liters of paint, how many liters it takes to paint one badge, and Pokedollar-value of each badge.

p = int(input())

b = int(input())

d = int(input())

# Determine how many badges are made and multiply by the dollar amount per badge.

badges_made = p // b

badge_money = badges_made * d

# Output total Pokedollars made, including 1 Pokedollar per leftover liter of paint.

print(badge_money + (p % b))

