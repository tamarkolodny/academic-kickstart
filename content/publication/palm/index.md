---
title: "PaLM: A Hybrid Parser and Language Model"
authors:
- hao
- me
- noah
publication_types: ["1"]
Date: 2019-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of EMNLP 2019*
abstract: "We present PaLM, a hybrid <b>p</b>arser and neural <b>l</b>anguage <b>m</b>odel. Building on an RNN language model, PaLM adds an attention layer over text spans in the left context. An unsupervised constituency parser can be derived from its attention weights, using a greedy decoding algorithm. We evaluate PaLM on language modeling, and empirically show that it outperforms strong baselines. If syntactic annotations are available, the attention component can be trained in a supervised manner, providing syntactically-informed representations of the context, and further improving language modeling performance."
tags:
- understanding_models 
links:
url_pdf: 'https://arxiv.org/abs/1909.02134'
url_code: 'https://github.com/Noahs-ARK/PaLM'
---
