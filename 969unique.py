from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for email in emails:
            parts = email.split('@')
            localname = parts[0].replace('.', '')
            if '+' in localname:
                localname = localname[:localname.index('+')]

            adr = localname+"@"+parts[1]
            if adr not in uniq:
                uniq.add(localname+"@"+parts[1])
        return len(uniq)


sol = Solution()

print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))