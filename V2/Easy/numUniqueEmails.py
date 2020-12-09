class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = 0
        email_list = []
        for e in emails:
            username = (e.split('@')[0].replace('.', '')).split('+')[0]
            domain = (e.split('@')[1])
            if (username + '@' + domain) not in email_list:
                email_list.append(username + '@' + domain)
        return len(email_list)