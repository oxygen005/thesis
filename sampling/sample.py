# Get 100 subdomains
# for every root domain

count_subdomains = {}

# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty                                                                                                                                                            y
def is_not_blank(s):
    return bool(s and not s.isspace())

def is_blank(s):
    return not is_not_blank(s)

with open('../dns_resolution/massdns/experiment3-alive.txt', 'r') as domains:
    with open('experiment3-sampled.txt', 'w') as sampled:
        for subdomain in domains:
            try:
                sample = subdomain
                if is_blank(subdomain):
                    continue
                domain_components = subdomain.split('.')
                if len(domain_components) != 3:
                    continue
                domain_name = domain_components[-3]
                tld = domain_components[-1] # TLDs such as .co.uk are not present in our list                                                                                                                                                             t in our list
                root_domain = domain_components[-2] + '.' + tld
                if root_domain not in count_subdomains:
                    count_subdomains[root_domain] = 1
                    sampled.write(sample)
                else:
                    if count_subdomains[root_domain] < 100:
                        count_subdomains[root_domain] += 1
                        sampled.write(sample)
            except (ValueError, IndexError) as e:
                print('Failed on ' + subdomain)
                print(e)
