---
title: "A Formal Hierarchy of RNN Architectures"
news: '<a class="btn btn-outline-primary my-1 mr-1 btn-sm" href="https://lambdaviking.com/post/rr-hierarchy/"  target="_blank">blog</a>'
authors:
- will
- gail
- yoav
- me
- noah
- erany
publication_types: ["1"]
Date: 2020-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of ACL 2020*
abstract: "We develop a formal hierarchy of the expressive capacity of RNN architectures. The hierarchy is based around two formal properties: space complexity, which is a measure of the RNN's memory, and rational recurrence, defined as whether the recurrent update can be described by a weighted finite-state machine. We place several RNN variants within this hierarchy. For example, we prove that the LSTM is not rational, which formally separates it from the related QRNN (Bradbury et al., 2016). We also show how the expressive capacity of these models is expanded by stacking multiple layers or composing them with different pooling functions.  Our results build on the theory of 'saturated' RNNs (Merrill, 2019). While formally extending these findings to unsaturated RNNs is left to future work, we hypothesize that the practical learnable capacity of unsaturated RNNs obeys a similar hierarchy. Experimental findings from training unsaturated networks on formal languages support this conjecture."
tags:
- understanding_models 
links:
url_pdf: 'https://arxiv.org/abs/2004.08500'
---
