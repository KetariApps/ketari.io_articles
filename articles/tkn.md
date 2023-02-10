---
author: Zach Garrett
date: Feb 6, 2023
path: tkn
tags: nlp linguistics research tokenization
title: Tkn
---

## Tokenization via Dynamic Sliding Window Regression

### Overview

Tokenization is the process of breaking down a larger body of text into smaller units called tokens. In the context of Natural Language Processing (NLP), tokenization is used to split text into meaningful elements such as words, punctuation marks, and numbers. The goal of tokenization is to convert unstructured text into a structured form that can be processed by NLP algorithms and models. The goal of this project is to develop an approach to tokenization which addresses the following issues:

- Ambiguity: Tokenization algorithms can struggle with ambiguity, especially when it comes to determining where one word ends and another begins. For example, in English, contractions such as "I'm" can be difficult to tokenize accurately.

- Complex Word Structures: Tokenization algorithms may not handle complex word structures, such as compound words or multi-word expressions, accurately. This can result in incorrect tokenization and affect the accuracy of NLP models.

- Language-Specific Issues: Tokenization algorithms can vary in accuracy depending on the language they are used on. For example, in some languages, words are not separated by white spaces, making tokenization more challenging.


### Theory

A core commonality among all languages is the use of repeating patterns of characters, called "morphemes", to convey meaning. Morphemes are the smallest units of meaning in a language, which are combined to form words and sentences. Morphological repetition and composition are fundamental building blocks of language which can be observed in all languages, regardless of their complexity or origin.

A feature of the morphological nature of language is that the morphemes of a language are typically a smaller set than the number of words, which are in turn a smaller set than the permutations of characters. This feature enables speakers to convey complex ideas using a small set of building blocks, and gives language inherent adaptability. To use English as an example, the number of letters is 26, the set of morphemes is generally agreed to be less than 60,000, the set of english words is around 170,000, while the possible permutations of n characters from english letters is n^26.

This tokenization algorithm uses a dynamic sliding window approach to parse tokens from a body of text. It maintains a persistent directed graph of encountered tokens (S), where each token is represented as a node. The window (W) scans the body of text and grows if its content is a node in S. If the window is not a node in S, a new window begins where the last one ended. In either case, the window is added to S. Because of this approach, S will contain many nodes that are not morphemes, but the probability of encountering the same non-morpheme later is low. As a result, the morphemes will be a small percentage of nodes in S, but they will have a high degree of centrality relative to other nodes with the same number of characters.

### Algorithm

```
Let D be a string
Let S be a persistent directed graph of encountered tokens
Let O = 0
Let L = 0
Let R = []

While L <= |D|

    Let W = D[dO:dL]

    If W exists in S
        L ++
        Replace the last node in R with W

    If W not exists in S
        Add node W to S
        L = 1
        Let O_n = O + L - 1
        If O_n < 0
            O = 0
        Else
            O = O_n

    Add a directed arc the second to last node in R to node W in S

Return R
```

### Addressing limitations of current tokenization algorithms

- This algorithm can be thought of as a system for recognizing repetitious patterns in the input data. The system doesn't need to know any characteristics of the data at its onset. Regardless of the language, the morphemes will emerge as the nodes in the graph with high centrality relative to nodes with the same number of characters.

- If the current window (W) exists in the set of previously encountered tokens (S), the window grows to include the next character. If the window is not found in S, a new window starts from the last window's end. This approach allows the algorithm to decompose unknown words into morphemes. This is useful for handling complex word structures, including semantic composition.
