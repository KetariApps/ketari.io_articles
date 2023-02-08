---
author: Zach Garrett
tags: nlp linguistics research tokenization
path: tkn
---

## Tokenization via Dynamic Sliding Window Regression  

1. ### Definitions  

```
Let D be a string
Let S be a persistent directed graph of encountered tokens
Let W be the current slice of D
Let O be the index of the first element in W from D[0]
Let L be the index of the last element in W from D[0]
Let R be the ordered list of tokens from D which are also nodes in S
```

2. ### Algorithm

```
Let O = 0
Let L = 0
Let R = []
While L <= |B|
    Let W = D[dO:dL]

    For each entry (a, b) in R + W:
        If node a not exists in S, add node a to S
        If node b not exists in S, add node b to S
        Add a directed arc from node a to node b in S

    If W exists in S
        L ++
        Let X = |R| - 1
        R = R[r0:rX] + W

    If W not exists in S
        L = 1
        O = O + L - 1
Return R
```

3. ### Theory

The possible permutations of size n from english letters (not including symbols or spaces) is n^26. The system becomes more accurate over time because the combinations which are meaningful in a language are more likely to be encountered by the algorithm than combinations that aren’t meaningful. Therefore, as the count of relationships of a node in S increases (relative to other nodes with the same number of characters) the probability of that node being a meaningful token also increases. The intended use of this algorithm is unsupervised, language agnostic tokenization. 
