---
title: "A Mixture of <i>h-1</i> Heads is Better than <i>h</i> Heads"
authors:
- hao
- me
- dianqi
- noah
publication_types: ["1"]
Date: 2020-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of ACL 2020*
abstract: "Multi-head attentive neural architectures have achieved state-of-the-art results on a variety of natural language processing tasks. Evidence has shown that they are overparameterized; attention heads can be pruned without significant performance loss. In this work, we instead 'reallocate' them-the model learns to activate different heads on different inputs. Drawing connections between multi-head attention and mixture of experts, we propose the <b>m</b>ixture of <b>a</b>ttentive <b>e</b>xperts model (MAE). MAE is trained using a block coordinate descent algorithm that alternates between updating (1) the responsibilities of the experts and (2) their parameters. Experiments on machine translation and language modeling show that MAE outperforms strong baselines on both tasks. Particularly, on the WMT14 English to German translation dataset, MAE improves over 'transformer-base' by 0.8 BLEU, with a comparable number of parameters. Our analysis shows that our model learns to specialize different experts to different inputs."
links:
url_pdf: 'https://arxiv.org/abs/2005.06537'

---
