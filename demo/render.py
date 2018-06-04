from draw import * 
import sys
sys.path.append("../")
from util import * 
from levenshtein import * 
import string

NOT_FOUDN = "http://shorelineseafoodinc.com/assets/images/404.png"

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
    html = html_template.substitute(body = body_html, lev_w = w, test_w = test_w)
    with open(output, "w") as f:
        f.write(html)
    print("{} rendered!".format(output))
    return output 

