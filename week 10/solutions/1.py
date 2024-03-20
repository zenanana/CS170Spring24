"""https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/"""

from collections import defaultdict
def minNumberOfFrogs(croakOfFrogs: str) -> int:
    # "croak"
    counts = defaultdict(int)
    min_frogs, active_frogs = 0, 0

    consec_chars = {
        'r': 'c',
        'o': 'r',
        'a': 'o',
        'k': 'a'
    }

    for char in croakOfFrogs:
        if char == 'c': 
            counts['c'] += 1
            active_frogs += 1
        elif char in consec_chars:
            if counts[consec_chars[char]] < 1: return -1
            else: 
                counts[consec_chars[char]] -= 1
                if char != 'k': counts[char] += 1
                else: active_frogs -= 1
        min_frogs = max(min_frogs, active_frogs)

    for v in counts.values():
        if v != 0: return -1

    return min_frogs



