import sys
sys.path.append("../")
from lib.util.plotter import * 
import matplotlib.pyplot as plt
from helper import * 
import numpy as np 

title = "Comparison between Naive and Levenshtein by Word Length ($k = 2$)"
save_path = "./output/runtime_by_word_len.png"

naive =  [0.014588117599487305, 0.009509086608886719, 0.0174868106842041, 0.027636051177978516, 0.03366684913635254, 0.04854607582092285, 0.06549191474914551, 0.09147810935974121, 0.12716102600097656, 0.17638587951660156]
lev  =  [0.009541749954223633, 0.018179655075073242, 0.0235288143157959, 0.03461122512817383, 0.03963494300842285, 0.03886890411376953, 0.06750702857971191, 0.05067086219787598, 0.05487990379333496, 0.062445878982543945]


words = ["m", "ti", "foo", "good", "email", "pretty", "manager", "perfectt", "wonderful", "university"]
lens  = np.array([len(w) for w in words])
fig = plt.figure() 

ax = plt.gca()
w = 0.3
ax.bar(lens - w/2, naive, width = w, color=blue, align='center')
ax.bar(lens + w/2, lev, width = w, color=light_purple, align='center')

plt.xticks(lens, words, rotation = 45)
ax.set_ylabel("runtime: log$(1 + t)$ /ms", fontsize=12)
ax.set_xlabel("Testing Word", fontsize=12)

plt.legend(["Naive", "Levenshtein"])
ax_set_title(ax, title, size = 16)
plt.tight_layout()
plt.savefig(save_path)

