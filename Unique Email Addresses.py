class Solution:
# O(n*s) time, O(n*s) space
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(Solution._unique_emails(emails))
    
    def _unique_emails(emails):
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            full = local + '@' + domain
            unique_emails.add(full)
        
        return unique_emails