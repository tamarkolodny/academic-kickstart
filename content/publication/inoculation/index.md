---
title: "Inoculation by Fine-Tuning: A Method for Analyzing Challenge Datasets"
authors:
- nelson
- me
- noah
publication_types: ["1"]
Date: 2019-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of NAACL 2019*
abstract: "Several datasets have recently been constructed to expose brittleness in models trained on existing benchmarks. While model performance on these <i>challenge datasets</i> is significantly lower compared to the original benchmark, it is unclear what particular weaknesses they reveal. For example, a challenge dataset may be difficult because it targets phenomena that current models cannot capture, or because it simply exploits blind spots in a model's specific training set. We introduce <i>inoculation by fine-tuning</i>, a new analysis method for studying challenge datasets by exposing models (the metaphorical patient) to a small amount of data from the challenge dataset (a metaphorical pathogen) and assessing how well they can adapt. We apply our method to analyze the NLI 'stress tests' (Naik et al., 2018) and the Adversarial SQuAD dataset (Jia and Liang,2017). We show that after slight exposure, some of these datasets are no longer challenging, while others remain difficult. Our results indicate that failures on challenge datasets may lead to very different conclusions about models, training datasets, and the challenge datasets themselves."
tags:
- improved_evaluation
links:
url_pdf: 'https://arxiv.org/abs/1904.02668'
url_slides: 'https://cs.stanford.edu/~nfliu/papers/liu+schwartz+smith.naacl2019.slides.pdf'
url_code: 'https://github.com/nelson-liu/inoculation-by-finetuning'
---
