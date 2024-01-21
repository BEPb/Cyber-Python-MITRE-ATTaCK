import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1]

def DNSRequest(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoAnswer):
        return
    return ips

def SubdomainSearch(domain, dictionary,nums):
    # successes = []
    for word in dictionary:
        subdomain = word+"."+domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)

# domain = "google.com"
domain = "hoster.by"
d = "subdomains.txt"
dictionary = []
with open(d,"r") as f:
    try:
        dictionary = f.read().splitlines()
    except dns.resolver.NoAnswer:
        print(f'{domain}: No answer')

SubdomainSearch(domain,dictionary,True)
