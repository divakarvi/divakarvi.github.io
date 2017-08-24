#! /usr/bin/env python
import os

cmd = 'grip --export --title=FAQ faq.md'
print(cmd)
os.system(cmd)

cmd = 'grip --export --title=Fixes fixes.md'
print(cmd)
os.system(cmd)
