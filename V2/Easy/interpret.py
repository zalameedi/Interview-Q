class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(0, len(command)):
            if command[i] == 'G':
                result += 'G'
            if command[i] == "(":
                if command[i+1] == ")":
                    result += "o"
                elif command[i+1] == "a":
                    result += "al"
                    i += 3
        return result
            