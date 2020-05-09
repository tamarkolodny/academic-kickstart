---
title: "Show Your Work: Improved Reporting of Experimental Results "
news: '<a class="btn btn-outline-primary my-1 mr-1 btn-sm" href="https://www.wired.com/story/artificial-intelligence-confronts-reproducibility-crisis/"  target="_blank">Wired</a>'
authors:
- jesse
- suchin
- dallas
- me
- noah)
publication_types: ["1"]
Date: 2019-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of EMNLP 2019*
abstract: "Research in natural language processing proceeds, in part, by demonstrating that new models achieve superior performance (e.g.,  accuracy) on held-out test data,  compared to previous  results.   In  this  paper,  we  demonstrate that test-set performance scores alone are insufficient  for  drawing  accurate  conclusions about which model performs best.  We argue for reporting additional details, especially performance  on  validation  data  obtained  during model development.  We present a novel technique  for  doing  so: <i>expected  validation  performance</i> of the best-found model as a function  of  computation  budget  (i.e.,  the  number of hyperparameter search trials or the overall training  time).   Using  our  approach,  we  find multiple recent model comparisons where authors would have reached a different conclusion  if  they  had  used  more  (or  less)  computation. Our  approach  also  allows  us  to  estimate  the  amount  of  computation  required  to obtain a given accuracy; applying it to several recently published results yields massive variation across papers, from hours to weeks.  We conclude with a set of best practices for reporting  experimental  results  which  allow  for robust future comparisons, and provide code to allow researchers to use our technique."
tags:
- greenai
links:
url_pdf: 'https://arxiv.org/abs/1909.03004'
url_code: 'https://github.com/allenai/allentune'
---
