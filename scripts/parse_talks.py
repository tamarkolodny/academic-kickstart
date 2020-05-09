#!/usr/bin/env python

import sys
import os
import re
import datetime


def main(args):
    if len(args) < 3:
        print("Usage: {} <ifile> <odir>".format(args[0]))
        return -1

    ifile = args[1]
    odir = args[2]

    with open(ifile) as ifh:
        lines = [l.rstrip().strip() for l in ifh]

    papers = []

    current_paper = {"summary": ""}
    inside = 0
    for i, l in enumerate(lines):
        if l.startswith('<script>TITLEF('):
            inside = 1
            elements = l.split("'")

            title = elements[3]
            slides = elements[1]
            name = "_".join(title.split(" ")[:2]).lower()
            current_paper["title"] = title
            current_paper["name"] = name
            current_paper['slides'] = slides
        elif inside and len(l) and l not in ["<br>", "<li>"]:
            if l == '</li>':
                save_paper(current_paper, odir)
                current_paper = {"summary": ""}
                inside = 0
            else:
                date_index = re.search(" \([0-9]{2}\/[0-9]{4}\)", l)
                if not date_index:
                    print("can't find date for {}".format(l))
                    assert 0
                
                date = l[date_index.start()+2:date_index.end()-1]
                date = datetime.datetime.strptime('01/'+date, '%d/%m/%Y').strftime('%Y-%m-%d')
                venue = l[:date_index.start()]
                current_paper["summary"] += venue+"<br>"
                current_paper['date'] = date


    return 0

def save_paper(paper, odir):
    print(paper)
    if 'name' not in paper:
        print('no name in ', paper)
    d = odir+"/"+paper["name"]
    try:
        os.mkdir(d)
    except FileExistsError:
        pass

    paper['summary'] = paper['summary'][:-4]
    with open(d+'/index.md', 'w') as ofh:
        ofh.write("---\n")
        for k in ['title', 'summary', 'date']: 
            ofh.write('{}: "{}"\n'.format(k, paper[k]))

        ofh.write('links:\n')
        ofh.write('url_slides: {}\n'.format(paper['slides']))
        ofh.write("---\n")
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))