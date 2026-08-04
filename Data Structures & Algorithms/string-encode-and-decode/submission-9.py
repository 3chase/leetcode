class Solution:
    
    def encode(self, strs: List[str]) -> str:
        message = []
        for s in strs:
            message.append('🥺' + str(len(s)) + '🥺' + s )
        return "".join(message)
    def decode(self, s: str) -> List[str]:
        messages = []
        i = 0
        while i < len(s):
            if s[i] == '🥺':
                k = i + 1
                while s[k] != '🥺':
                    k += 1
                num = int(s[i+1:k])
                messages.append(s[k + 1:k + 1 + num])
            i += len(str(num)) + 2 + num
        return messages
