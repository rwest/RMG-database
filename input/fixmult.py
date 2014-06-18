#!/usr/bin/env python
# encoding: utf-8

import os
import re

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):     
    for filename in files:
        path= os.path.join(root,filename)
        with open(path) as in:
            
    
