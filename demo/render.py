from draw import * 
import sys
sys.path.append("../")
from config import * 
from util import * 
from lev_trie_gen import * 
import string
from lib.util.timer import * 

NOT_FOUDN = "http://shorelineseafoodinc.com/assets/images/404.png"

timer = Timer()
corpus_trie  = load_data(corpus_trie_path) 
generater = LevTrieGenerator(corpus_trie)
print("Using Corpus:")
print("----------------------")
print(corpus_trie.stats())
print() 

def render(w, test_w, k):
    """
    Args:
        w: 
        test_w: 
        k: 

    Return: 
    """ 
    figures = render_dfa_walker(w, test_w, k)
    section_template = string.Template(open("./section.html").read())
    html_template = string.Template(open("./main.html").read())

    sections = []
    for (t, f) in figures:
        fig  = "{}.svg".format(f) if f is not None else NOT_FOUDN
        curr_sec = section_template.substitute(title = t, fig = fig)
        sections.append(curr_sec)
    body_html = "\n".join(sections)


    output = "{}_{}_k_{}.html".format(w, test_w, k)

    timer.start("Generating Candidates for {} Takes".format(w))
    print("--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    candidates = generater.gen_candidates(w, k)
    timer.stop_and_report("Generating Candidates for {} Takes".format(w))
    can_str = ", ".join(sorted(candidates))

    html = html_template.substitute(body = body_html, lev_w = w, test_w = "{} (k = {})".format(test_w, k), candidates = can_str)
    with open(output, "w") as f:
        f.write(html)

    print("{} rendered!".format(output))
    
    return output 

