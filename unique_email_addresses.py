#started at 3:57 PM
class Solution:
	def numUniqueEmailes(self, emails: 'List[str]') --> 'int':
		#emails may contains '.' or '+'s
		actual_emails = []
		for email in emails:
			local, domain = email.split('@')
			if local.find('+') != -1:
				local = local[:local.find('+')].replace('.','')
			else:
				local = local.replace('.', '')
			actual_emails.append(local+'@'+domain)
		
		return len(set(actual_emails))
#finished at 4:31 PM

# Runtime: 44 ms, faster than 99.71% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 6.5 MB, less than 78.65% of Python3 online submissions for Unique Email Addresses.
			


