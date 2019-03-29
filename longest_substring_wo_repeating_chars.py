def lengthOfLongestSubstring(s):
    counter = 1
    beg = 0
    idx = 0
    seq = set()
    while True:
        if idx < len(s):
            seq.add(s[idx])
            if s[idx+1] in seq:
                s.find(s[idx+1], beg)
                seq = set([char for char in s[]])

print(lengthOfLongestSubstring('pwwkew'))