---
title: "Symmetric Patterns and Coordinations: Fast and Enhanced Representations of Verbs and Adjectives"
authors:
- me
- roi
- ari
publication_types: ["1"]
Date: 2016-07-01
publishDate: 2020-04-01T00:00:00Z
publication: In *Proc. of NAACL 2016*
abstract: "State-of-the-art word embeddings, which are often trained on bag-of-words (BOW) contexts, provide a high quality representation of aspects of the semantics of nouns. However, their quality decreases substantially for the task of verb similarity prediction. In this paper we show that using symmetric pattern contexts (SPs, e.g., ``X and Y'') improves word2vec verb similarity performance by up to 15% and is also instrumental in adjective similarity prediction. The unsupervised SP contexts are even superior to a variety of dependency contexts extracted using a supervised dependency parser. Moreover, we observe that SPs and dependency coordination contexts (Coor) capture a similar type of information, and demonstrate that Coor contexts are superior to other dependency contexts including the set of all dependency contexts, although they are still inferior to SPs. Finally, there are substantially fewer SP contexts compared to alternative representations, leading to a massive reduction in training time. On an 8G words corpus and a 32 core machine, the SP model trains in 11 minutes, compared to 5 and 11 hours with BOW and all dependency contexts, respectively."
tags:
- word_representations
links:
url_pdf: 'papers/sp_sg/sp_sg_naacl_camera_ready.pdf'
url_poster: 'papers/sp_sg/sp_sg_naacl_poster.pdf'
url_code: 'papers/sp_sg/sp_sg.html'
---
