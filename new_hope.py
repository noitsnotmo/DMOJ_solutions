
# DMOJ problem wc15c2j1, A New Hope

# Input an integer between 1 and 5.

n = int(input())

# Multiply integer by 'far'.

far = (n - 1) * 'far, '

# Output "A long time ago in a galaxy far, far away..." with the number of 'far's specified by integer. NOTE: each far must be separated by a comma EXCEPT the last one.

print('A long time ago in a galaxy ' + far + 'far away...')