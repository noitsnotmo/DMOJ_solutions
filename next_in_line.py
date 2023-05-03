
# DMOJ Problem ccc13j1, Next in Line

# Input an age Y for the youngest child and M for the middle child.

y = int(input())

m = int(input())

# Output the age of the oldest.

o = m + (m - y)

print(o)