class Solution:
    
    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            message += ('🥺' + str(len(s)) + '🥺' + s )
        return message
    def decode(self, s: str) -> List[str]:
        messages = []
        i = 0
        while i < len(s):
            if s[i] == '🥺':
                k = i + 1
                digits = 0
                while s[k] != '🥺':
                    digits += 1
                    k += 1
                num = int(s[i+1:i+1+digits])
                messages.append(s[i + digits + 2:i + digits + 2 + num])
            i += digits + 2 + num
        return messages
