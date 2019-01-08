#!/usr/bin/env python3
import rpyc
conn = rpyc.connect("localhost", 12345)
c = conn.root

my_object = c.get_my_object()
print(my_object.solution)
my_object.solution = 43
