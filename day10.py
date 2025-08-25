from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    # Return only the grouped values
    return list(anagram_map.values())


# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
