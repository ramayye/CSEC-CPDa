# Read input values
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Initialize width counter
width = 0

# Calculate the required width
for height in heights:
    if height > h:
        width += 2  # Needs to bend
    else:
        width += 1  # Walks normally

# Print the result
print(width)
