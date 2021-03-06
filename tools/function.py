#! env/bin/python
# coding:utf-8
import socket


def get_domain(url):
    url1 = url
    if url.find("//") != -1:
        url1 = url.split('//')[1]
    if url1.find('/') != -1:
        domain = url1.split('/')[0]
    else:
        domain = url1
    return domain


def get_father_domain(domain):
    if domain == 'localhost':
        return domain
    domain1 = domain.split('.')
    if len(domain1) <= 2:
        return domain
    domain = '.'.join(domain1[1:])
    return domain


def get_first_domain(domain):
    domain1 = domain.split('.')
    if domain == 'localhost':
        return domain
    if len(domain1) <= 2:
        return domain
    if len(domain1) >= 3:
        if domain1[-1] == 'cn' and domain1[-2] == 'com':
            domain = '.'.join(domain1[-3:])
        else:
            domain = '.'.join(domain1[-2:])
    return domain


def get_ip(domain):
    # ip = socket.gethostbyname(domain)
    res = socket.getaddrinfo(domain, None)
    addrs = []
    for i in res:
        addr = i[4][0]
        if len(addr.split('.')) != 4:
            continue
        addrs.append(addr)
    return addrs


def get_root_url(url):
    a = url.split("//")
    if len(a) == 1:
        url.split('/')
        url = 'http://' + url[0]
    else:
        url = a[0] + '//' + a[1].split('/')[0]
    return url


if __name__ == '__main__':
    url = 'http://www.runoob.com'
    domain = get_domain(url)
    print domain
    ip = get_ip(domain)
    print ip