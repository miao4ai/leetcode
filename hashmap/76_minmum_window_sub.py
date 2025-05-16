from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        required = len(need)

        left = 0
        res = (float("inf"), 0, 0)  # (window_len, left, right)

        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if (right - left + 1) < res[0]:
                    res = (right - left + 1, left, right)

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return s[res[1]:res[2] + 1] if res[0] != float("inf") else ""
