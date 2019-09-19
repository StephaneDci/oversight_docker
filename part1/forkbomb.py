#!/usr/bin/env python
import os

# Be Careful : very Dangerous , use with cgroup only!!!

i=0
while True:
    os.fork()
    print(i)
    i=i+1
