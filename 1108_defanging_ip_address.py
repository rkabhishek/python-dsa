class Solution:
    def defangIPaddrCharConcat(self, address: str) -> str:
        ans = ""
        for ch in address:
            if ch == ".":
                ans += "[.]"
            else:
                ans += ch

        return ans

    def defangIPaddrListJoin(self, address: str) -> str:
        ans = []
        for ch in address:
            if ch == ".":
                ans.append("[.]")
            else:
                ans.append(ch)

        return "".join(ans)

    def defangIPaddrReplace(self, address: str) -> str:
        return address.replace(".", "[.]")
