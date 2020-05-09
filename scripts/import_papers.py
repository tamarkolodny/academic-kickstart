#!/usr/bin/env python

import sys
import os
import re
import shutil

tags = {'rational_recurrences': "understanding_models ", "greenai": "greenai", "embeddings": "word_representations", "artifacts": "improved_evaluation"}

def main(args):
    if len(args) < 3:
        print("Usage: {} <ifile> <odir>".format(args[0]))
        return -1

    ifile = args[1]
    odir = args[2]

    with open(ifile) as ifh:
        lines = [l.rstrip() for l in ifh]

    papers = []

    current_paper = None

    for i, l in enumerate(lines):
        if l.startswith('<script>TITLE('):
            if current_paper is not None:
                save_paper(current_paper, odir)
            current_paper = {"press_names": [], "press_urls": []}

            components = l[15:].replace("'", '"').split('"')
            title = components[0]
            local_tags = [x[:-2].strip().lower() for x in components[1].split(";")[1:-1]]
            current_paper['title'] = title
            current_paper['tags'] = local_tags
            print("Found {}, {}".format(title, local_tags))
        elif current_paper is not None:
            if l.find('<b>Green AI</b>') != -1:
                save_paper(current_paper, odir)
                current_paper = {"press_names": [], "press_urls": []}
                current_paper['title'] = "Green AI"
                current_paper['tags'] = ["greenai"]
            elif l.startswith('<i><script>document.write('):
                l= l[26:-18]
                elements = l.split('+')

                authors = []
                for element in elements:
                    if element[1] == '*':
                        authors[-1] += 'star'
                        continue
                    elif element[1] in [' ', ',']:
                        continue

                    element = element.replace('+', '').replace('"','')
                    subslements = element.split(", ")
                    
                    if len(subslements) == 1:
                        authors.append(element.lower())
                    else:
                        for subelement in subslements:
                            subelement = subelement.split(' ')[0]
                            authors.append(subelement.lower())
                current_paper['authors'] = authors
            elif l.find('CONFERENCE(') != -1:
                elements = l.split("'")
                conference = elements[3]
                award = None if len(elements) < 6 else elements[5]
                current_paper['venue'] = conference
                if award is not None and len(award) > 0:
                    current_paper['award'] = award
                elements = conference.split(" ")
                if len(elements) > 1:
                    year = elements[1]
                current_paper['date'] = year+"-07-01"
            elif l.find('<script>PRESS(') != -1:
                elements = l.split("'")

                name = elements[1]
                url = elements[3]
                current_paper["press_names"].append(name)
                current_paper["press_urls"].append(url)

            elif l.startswith("<div id=") and l.find("_abstract") != -1:
                end_index = l.find("_abstract")
                name = l[9:end_index]
                l = lines[i+1]
                current_paper['abstract'] = l.rstrip()
                current_paper['name'] = name
            elif l.startswith("DATA") or l.startswith("<script>DATA"):
                v = l.split("'")[1]
                current_paper['dataset'] = v
            elif l.startswith("WEBSITE") or l.startswith("<script>WEBSITE"):
                v = l.split("'")[1]
                current_paper['project'] = v
                
            else:
                for j in ['pdf', 'bib', 'slides', 'poster', 'video', 'code']:
                    # print("Cjheckoig {} in {}".format(i, l))
                    if l.startswith(j.upper()) or l.startswith("<script>"+j.upper()):
                        v = l.split("'")[1]
                        current_paper[j] = v
                        break

                    

    save_paper(current_paper, odir)

    return 0

def save_paper(paper, odir):
    publication_type = 1
    if 'name' not in paper:
        print('no name in ', paper)
    d = odir+"/"+paper["name"]
    try:
        os.mkdir(d)
    except FileExistsError:
        pass

    for k in ['poster', 'slides']:
        if k in paper and not paper[k].startswith('http'):
            paper[k] = k+'.pdf'
    
    k = 'code'
    if k in paper and not paper[k].startswith('http'):
        paper[k] = k+'.html'
    print(paper)
    
    shutil.copyfile('/Users/roysch/code/roys174.github.io/'+paper['bib'], d+"/cite.bib")

    with open(d+'/index.md', 'w') as ofh:
        ofh.write("---\n")
        k = 'title'
        ofh.write('{}: "{}"\n'.format(k, paper[k]))
    
        if len(paper['press_names']):
            press = " ".join('<a class="btn btn-outline-primary my-1 mr-1 btn-sm" href="{}"  target="_blank">{}</a>'.format(url,name) for name, url in zip(paper["press_names"], paper["press_urls"]))
            ofh.write("news: '{}'\n".format(press))

        if 'date' in paper:
            date = paper['date']
            if paper['name'] == 'mae':
                paper['authors'].insert(2, 'dianqi')
            elif paper['name'] == 'peeread':
                paper['authors'].insert(3, 'madeleine')
                paper['authors'].insert(4, 'sebastian')
            elif paper['name'] in ['lsdsem_uw_nlp', "language_constraint"]:
                paper['authors'].insert(3, 'lizilles')
        
        if paper['name'] == 'greenai':
            date = "2019-07-01"
            publication_type = 2
        elif paper['name'] == 'finetune':
            date= "2020-02-01"
            publication_type = 3
        elif paper['name'] == 'thesis':
            date= "2016-06-01"
            paper['pdf'] = 'publication/thesis/paper.pdf'
            ofh.write('publication: PhD Thesis\n')
            publication_type = 7

        ofh.write("authors:\n")
        for a in paper['authors']:
            ofh.write('- {}\n'.format(a))

        ofh.write('publication_types: ["{}"]\n'.format(publication_type))
        ofh.write('Date: {}\n'.format(date))
        ofh.write('publishDate: {}\n'.format("2020-04-01T00:00:00Z"))


        if 'venue' in paper:
            elements = paper['venue'].split(' ')

            award = ''
            if 'award' in paper:
                award = ' <span style="color:red">{}</span>'.format(paper['award'])

            if len(elements) > 1:
                ofh.write('publication: In *Proc. of {}*{}\n'.format(paper['venue'], award))
            else:
                ofh.write('publication: In *{}*\n'.format(paper['venue']))
                

        k = 'abstract'
        paper[k] = paper[k].replace('"', "'")
        ofh.write('{}: "{}"\n'.format(k, paper[k]))
        if len(paper['tags']) > 0:
            ofh.write('tags:\n')
            for t in paper['tags']:
                ofh.write('- {}\n'.format(tags[t]))

        first = 1
        for k in ['pdf', 'dataset', 'poster', 'slides', 'video', 'code', 'project']:
            if k in paper:
                if first:
                    ofh.write('links:\n')
                    first = 0

                ofh.write("url_{}: '{}'\n".format(k, paper[k]))
        ofh.write('---\n')
    # assert(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))