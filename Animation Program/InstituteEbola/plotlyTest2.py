# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py  
 
# (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *
 
import numpy as np  # (*) numpy for math functions and arrays

# (*) Import module keep track and format current time
import datetime 
import time 

import sys
import re
import datetime as dt
import matplotlib


#init counter
count = 0

#init x and y arrays for axis vals
x = []
yx = []

# store lines of text and dates
lines = []
date = []

with open('noRepeat.txt', 'r') as f:
    lines = f.read()

# strip all dates from the supplied file
text = lines.split("\n")
dateFormat = '\d{4}-\d{2}-\d{2}'
for s in text:
    match = re.search(dateFormat, s)
    if match:
        date.append(dt.datetime.strptime(match.group(), '%Y-%m-%d').date())
    else:
        #print "no match on for:  " + s 
        continue

# we know all the entries contain the keyword; sorting will no have
# a negative impact
date.sort()

print date

#Count number of ALL tweets per day
i = 0
temp = date[0]
for i in range(len(date)):
    if temp == date[i]:
        count = count + 1
        i = i + 1
    else:
        x.append(temp)
        yx.append(count)
        temp = date[i]
        count = 1
print yx
tls.set_credentials_file(stream_ids=[
        "r510f777cl",
        "hrrxpb1uag"
    ])

stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list 
stream_id = stream_ids[0]

# Make instance of stream id object 
stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream         # (!) embed stream id, 1 per trace
)

data = Data([trace1])

# Add title to layout object
layout = Layout(title='Time Series')

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='s7_first-stream')

# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
s = py.Stream(stream_id)

# (@) Open the stream
s.open()

i = 0    # a counter
k = 5    # some shape parameter
N = len(x)  # number of points to be plotted

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5) 

datenums = matplotlib.dates.date2num(x)

while i<N:
    # Current time on x-axis, random numbers on y-axis
    x=datetime.datetime(2014,10,i+1)
    y=yx[i]
    
    # (-) Both x and y are numbers (i.e. not lists nor arrays)
    
    # (@) write to Plotly stream!
    s.write(dict(x=x,y=y))  
    
    # (!) Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot (more in 7.2).
            
    time.sleep(0.5)  # (!) plot a point every 80 ms, for smoother plotting
    i+=1
	
# (@) Close the stream when done plotting
s.close() 