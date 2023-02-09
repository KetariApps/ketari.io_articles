---
author: Zach Garrett
date: Feb 6, 2023
path: tkn
tags: nlp linguistics research tokenization
title: Tkn
---

## Tokenization via Dynamic Sliding Window Regression

### Overview

Tokenization is the process of breaking down a larger body of text into smaller units called tokens. In the context of Natural Language Processing (NLP), tokenization is used to split text into meaningful elements such as words, punctuation marks, and numbers. The goal of tokenization is to convert unstructured text into a structured form that can be processed by NLP algorithms and models. Despite their pervasiveness in the NLP pipeline, existing tokenization algorithms have several limitations:

- Ambiguity: Tokenization algorithms can struggle with ambiguity, especially when it comes to determining where one word ends and another begins. For example, in English, contractions such as "I'm" can be difficult to tokenize accurately.

- Complex Word Structures: Tokenization algorithms may not handle complex word structures, such as compound words or multi-word expressions, accurately. This can result in incorrect tokenization and affect the accuracy of NLP models.

- Language-Specific Issues: Tokenization algorithms can vary in accuracy depending on the language they are used on. For example, in some languages, words are not separated by white spaces, making tokenization more challenging.

- Out-of-Vocabulary (OOV) Tokens: Tokenization algorithms may encounter tokens that are not present in their vocabulary. This can be particularly problematic for NLP models that rely on a fixed vocabulary, as OOV tokens may not be processed correctly.

- Unicode Issues: Tokenization algorithms can struggle with handling Unicode characters, such as emoji or non-Latin script, accurately.

### Theory

A core commonality among all languages is the use of repeating patterns of characters, called "morphemes", to convey meaning. Morphemes are the smallest units of meaning in a language, and they can be combined to form words and sentences. This repetition of morphemes is a fundamental aspect of language and is found in all languages, regardless of their complexity or origin.

Another important aspect of this repetition of morphemes is that the number of morphemes in a language is typically much smaller than the number of words, and even smaller than the number of possible character permutations. This relationship between the number of morphemes and the number of character permutations is a commonality among all languages and enables speakers to efficiently convey complex ideas using a relatively small set of building blocks. The use of recurring patterns and structures in language also allows speakers to quickly recognize and understand words, even if they are unfamiliar with them, by breaking them down into their constituent morphemes. For example, the possible permutations of n characters from english letters is n^26, but the set of english words is around 170,000, the set of morphemes is generally agreed to be less than 60,000, and the number of letters is only 26.

This tokenization algorithm uses a dynamic sliding window approach to parse tokens from a body of text. It maintains a persistent directed graph of encountered tokens (S), where each token is represented as a node. The algorithm uses a sliding window (W) to scan the body of text and grow the window if the current window is found in S. If the window is not found in S, a new window begins where the last one ended. In either case, the window is added to S. Because of this approach, S will contain many tokens that are not actual morphemes, but the probability of encountering the same non-morpheme window later is low. As a result, the number of morphemes will be a small percentage of tokens in S, but for a token in S of length n, the tokens that are most likely to be morphemes will have the most relationships. This algorithm allows the system to learn the morphemes of any language without any prior information. The goal of this project is to provide a single, unsupervised, language agnostic tokenization algorithm which addresses the above issues.

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

### Addressing the issues of current tokenization algorithms

- This algorithm can be thought of as a system for recognizing repetitious patterns in the input data. The system doesn't need to know any characteristics of the data at its onset. Regardless of the language, the morphemes will emerge as the nodes in the graph with high centrality relative to nodes with the same number of characters.

- If the current window (W) exists in the set of previously encountered tokens (S), the window grows to include the next character. If the window is not found in S, a new window starts from the last window's end. This approach allows the algorithm to decompose unknown words into morphemes. This is useful for handling complex word structures, including semantic composition.
