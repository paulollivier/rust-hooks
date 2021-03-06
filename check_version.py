#!/usr/bin/env python
import os
import re
import toml

V_RE = re.compile(r'\d+\.\d+\.\d+')

cargo_v = toml.load(open('Cargo.toml'))['package']['version']
git_raw = os.popen('git describe --abbrev=0 --tags').read().strip('\n')
print("latest git version is %s, cargo version is %s" % (git_raw, cargo_v))
git_v = V_RE.search(git_raw)
if git_v is None:
    print("no git tag found")
    exit(0)
git_v = git_v.group(0)

cv, gv = cargo_v.split('.'), git_v.split('.')
for i in [0, 1, 2]:
    if gv[i] > cv[i]:
        print("last git tag is greater than cargo.toml's version")
        exit(1)
    elif cv[i] > gv[i]:
        print("Cargo version is greater than git. Don't forget to tag!")
        exit(0)
