def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Assume first word is prefix
    prefix = strs[0]

    for word in strs[1:]:
        # Shrink prefix until it matches the start of current word
        while word.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example
print(longestCommonPrefix(["flower", "flow", "flight"])) 
