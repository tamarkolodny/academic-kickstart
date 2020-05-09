---
title: "The Right Tool for the Job: Matching Model and Instance Complexities"
authors:
- me
- gabi
- swabha
- jesse
- noah
publication_types: ["1"]
Date: 2020-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of ACL 2020*
abstract: "As NLP models become larger, executing a trained model requires significant computational resources incurring monetary and environmental costs. To better respect a given inference budget, we propose a modification to contextual representation fine-tuning which, during inference, allows for an early (and fast) 'exit' from neural network calculations for simple instances, and late (and accurate) exit for hard instances. To achieve this, we add classifiers to different layers of BERT and use their calibrated confidence scores to make early exit decisions. We test our proposed modification on five different datasets in two tasks: three text classification datasets and two natural language inference benchmarks. Our method presents a favorable speed/accuracy tradeoff in almost all cases, producing models which are up to five times faster than the state of the art, while preserving their accuracy. Our method also requires almost no additional training resources (in either time or parameters) compared to the baseline BERT model. Finally, our method alleviates the need for costly retraining of multiple models at different levels of efficiency; we allow users to control the inference speed/accuracy tradeoff using a single trained model, by setting a single variable at inference time. We publicly release our code."
tags:
- greenai
links:
url_pdf: 'http://arxiv.org/abs/2004.07453'
url_code: 'https://github.com/allenai/sledgehammer'
---
