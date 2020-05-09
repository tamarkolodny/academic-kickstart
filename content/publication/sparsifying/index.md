---
title: "RNN Architecture Learning with Sparse Regularization "
authors:
- jesse
- me
- hao
- noah
publication_types: ["1"]
Date: 2019-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of EMNLP 2019*
abstract: "Neural models for NLP typically use large numbers of parameters to reach state-of-the- art performance, which can lead to excessive memory usage and increased runtime. We present a structure learning method for learning sparse, parameter-efficient NLP models. Our method applies group lasso to rational RNNs (Peng et al., 2018), a family of models that is closely connected to weighted finite-state automata (WFSAs). We take advantage of rational RNNs’ natural grouping of the weights, so the group lasso penalty directly removes WFSA states, substantially reducing the number of parameters in the model. Our experiments on a number of sentiment analysis datasets, using both GloVe and BERT embeddings, show that our approach learns neural structures which have fewer parameters without sacrificing performance relative to parameter-rich baselines. Our method also highlights the interpretable properties of rational RNNs. We show that sparsifying such models makes them easier to visualize, and we present models that rely exclusively on as few as three WFSAs after pruning more than 90% of the weights. We publicly release our code."
tags:
- greenai
- understanding_models 
links:
url_pdf: 'https://arxiv.org/abs/1909.03011'
url_code: 'https://github.com/dodgejesse/sparsifying_regularizers_for_RRNNs'
---
