import sys
sys.path.append("../")
from lib.util.plotter import * 
import matplotlib.pyplot as plt
from helper import * 
import numpy as np 

title = "Comparison between Naive and Levenshtein by $k$"
save_path = "./output/runtime_by_k.png"

naive =  [0.01125192642211914, 0.10906314849853516, 28.630791902542114]
lev   =  [0.01652812957763672, 0.06898093223571777, 0.24412322044372559]


k = len(naive)
fig = plt.figure() 
ax = plt.gca()
xs = np.array(range(1, 1 + k))
w = 0.3
ax.bar(xs - w/2, scale_down(naive), width = w, color=blue, align='center')
ax.bar(xs + w/2, scale_down(lev), width = w, color=light_purple, align='center')

ax.set_ylabel("runtime: log$(1 + t)$ /ms", fontsize=12)
ax.set_xlabel("Edit Distance: $k$", fontsize=12)
force_axis_integer(ax)

plt.legend(["Naive", "Levenshtein"])
ax_set_title(ax, title, size = 16)
plt.tight_layout()
plt.savefig(save_path)

