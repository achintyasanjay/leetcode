from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # want to store this in a hashmap with each subdomain as a key
        # key = subdomain, value = count
        # need to parse the array by splitting string by periods

        subdomains = defaultdict(int)

        for domain in cpdomains:
            count, full_domain = domain.split(" ")
            count = int(count)
            subDomain = full_domain.split('.')
            for i in range(len(subDomain)):
                sub = '.'.join(subDomain[i:])
                subdomains[sub] += count
        output = []
        for key, val in subdomains.items():
            res = f"{val} {key}"
            output.append(res)

        return output

        # Time Complexity: O(N * M), where N is the number of domains in cpdomains
        # and M is the maximum number of subdomains in a domain.
        # We iterate through each domain once, and for each domain, we process
        # each of its subdomains.

        # Space Complexity: O(K), where K is the total number of unique subdomains
        # across all domains. In the worst case, this could be equal to the total
        # number of subdomains across all domains if they are all unique.