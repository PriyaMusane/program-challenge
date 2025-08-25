def reverseWords(s: str) -> str:
    # split() without arguments automatically removes extra spaces
    words = s.split()
    # reverse the list
    reversed_words = words[::-1]
    # join back with single space
    return " ".join(reversed_words)

# Example
s = "  the   sky   is   blue  "
print(reverseWords(s))  # Output: "blue is sky the"
