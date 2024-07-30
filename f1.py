i = 1
while i <= 5:
    print("SID ", end="")
    j = 1
    while j <= 4:
        print("Hello ", end="")
        j += 1
    print()  # Move to the next line after inner loop completes
    i += 1  # Increment the outer loop counter
