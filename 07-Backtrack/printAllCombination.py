def abc(word, n):
    # Base case: if the word's length exceeds n, stop recursion
    if len(word) > n:
        return

    # If the word has exactly n characters, print it
    if len(word) == n:
        print(word)
        return

    # Recur by appending 'a', 'b', and 'c' to the word
    abc(word + 'a', n)
    abc(word + 'b', n)
    abc(word + 'c', n)

# Call the function with an empty string and desired length
abc('', 3)  # Change 2 to any other number for different lengths
