import numpy as np
import numpy as np
import plotly
import plotly.plotly as py
from helper import *
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='dengl11', api_key='STvfIKmz3XwcKtfhlAS4')

naive=  [[0.00029206275939941406, 0.09076905250549316], [0.00024509429931640625, 0.04193687438964844], [0.000263214111328125, 0.04201817512512207], [0.00034999847412109375, 0.11099004745483398], [0.0004229545593261719, 0.13772106170654297]]
lev=    [[0.009863138198852539, 0.0629570484161377], [0.009034872055053711, 0.047952890396118164], [0.009441137313842773, 0.044248104095458984], [0.012179136276245117, 0.06292009353637695], [0.01417231559753418, 0.07550907135009766]]


# lev = scale_down2d(lev)
# naive = scale_down2d(naive)
lev = np.array(lev)
naive = np.array(naive)


k = 2
tests = ["date", "book", "food", "pretty", "teacher"]
ks    = list(range(1, k + 1))

x = []
y = []
z_naive = []
z_lev = []

lens = list(range(1, len(tests) + 1))
for l in lens:
    for k in ks:
        x.append(l)
        y.append(k)
        z_naive.append(naive[l-1][k-1])
        z_lev.append(lev[l-1][k-1])



marker=dict(
    size=12,
    color='#7bb6d6',                # set color to an array/list of desired values
    opacity=1
)

trace_naive = go.Scatter3d(x=x, y=y, z=z_naive, mode='markers', marker = marker, name = "Naive" )

marker["color"] = '#cab2d6'

trace_lev = go.Scatter3d(x=x, y=y, z=z_lev, mode='markers', marker = marker, name = "Levenshtein" )


big_tickfont=dict(size=16)
mid_tickfont=dict(size=14)
label_font=dict(size=20)
title_font=dict(size=16)
data = [trace_naive, trace_lev]

scene = dict(xaxis = dict( ticktext = tests, tickvals= lens, tickfont = big_tickfont, title='words', titlefont = label_font, backgroundcolor="rgb(230, 230, 200)", showbackground=True,),
             yaxis = dict( ticktext = ks, tickvals = ks, title='k', tickfont = mid_tickfont, titlefont = label_font, backgroundcolor="rgb(230, 200,200)", showbackground=True),
             zaxis = dict( title='runtime / ms', tickfont = mid_tickfont, titlefont = label_font,backgroundcolor="rgb(230, 230,230)", showbackground=True))

titel = "Weighted Candidate Generation Runtime Comparison"
layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0), scene = scene, title='', titlefont = title_font, autosize=True)

fig = go.Figure(data=data, layout=layout)
