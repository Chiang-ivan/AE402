# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:20:19 2020

@author: User
"""

class pet():
    def __init__(self,name,foot,hair):
        self.name = name
        self.foot = foot
        self.hair = hair
        
class cat(pet):
    def __init__(self,clean,bigeye):
        super.__init__()
        self.clean = clean
        self.bigeye = bigeye
        
class dog(pet):
    def __init__(self,tail,runfast):
        super.__init__()
        self.tail = tail
        self.runfast = runfast
        