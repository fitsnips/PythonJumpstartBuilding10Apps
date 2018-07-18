#!/usr/bin/env python3
import collections

# different ways to define a dict
lookup = {}
lookup_b = dict()
lookup_c = {'age': 42, 'loc': 'Italy'}
lookup_d = dict(age=42, loc='Italy')

print(lookup_c)
print(lookup_c['loc'])

# print if cat exist as key in dict
if 'cat' in lookup:
    print(lookup['cat'])

lookup['cat'] = 'Fun code demos'

# print if cat exist as key in dict
if 'cat' in lookup:
    print(lookup['cat'])


# Second way:

User = collections.namedtuple('User',
                              'id, name, email')

users = [
    User(1, 'user1', 'user1@sampledomain.com'),
    User(2, 'user2', 'user2@sampledomain.com'),
    User(3, 'user3', 'user3@sampledomain.com'),
    User(4, 'user4', 'user4@sampledomain.com'),
]


# push the users into a dict ... so its indexed (correct wording?)
lookup = dict()
for u in users:
    lookup[u.email] = u

# very quick lookup using dict
print(lookup['user3@sampledomain.com'])


