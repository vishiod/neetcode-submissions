import math

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += str(len(s))
            ans += "#"
            ans += s
        
        return ans

    def decode(self, s: str) -> List[str]:
        
        if s == "0#":
            return [""]

        i, is_num_detected, len_to_look_for = 0, False, ""
        ans = []

        while i < len(s):

            if is_num_detected:
                look_for = int(len_to_look_for)
                j = i
                res = ""

                print("look_for: ", look_for)
                while j < min(look_for + i, len(s)):
                    res += s[j]
                    j += 1
                    print("j: ", j)
                
                len_to_look_for = ""
                is_num_detected = False
                i = j
                
                print("i: ", i)
                ans.append(res)

            else:
                
                if s[i] == "#" or s[i] == '#':
                    is_num_detected = True

                elif s[i].isdigit():
                    len_to_look_for += s[i]
                
                i += 1

        if s.endswith("0#"):
            ans.append("")

        return ans
