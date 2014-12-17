import os
import sys

Series = ['fileConstruct','kwOnFile']

i = 0
for s in Series:
    if i == 1:
        runFile = s + ".py"
        i+=1
    else:
        runFile = s + ".py"
        i+=1
    os.system(runFile)
    