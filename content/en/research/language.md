+++
identifier = 'research__language'
title = 'Language'
description = 'Research at Lab4SLC on machine translation, language analysis, and applications of natural language processing.'
type = 'docs'
icon = 'fa-solid fa-language'
parent = 'Research'
weight = 22
hide_summary = true
+++

## Machine Translation
### The Relationship between Latency and Accuracy in Simultaneous Machine Translation
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/ogura.mp4" label="Japanese-language video introducing simultaneous machine translation research" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2025 Annual Conference" >}}
<ul>
<li>Study low-latency simultaneous translation between Japanese and Korean, which have similar word order</li>
<li>Use BS-SiMT, which learns from data when to wait before generating a translation</li>
<li>Show that some delay is necessary to maintain accuracy even when the source and target languages have similar word order</li>
<li>Next step: develop more advanced translation strategies, including paraphrasing, to reduce latency</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

### Japanese-to-English Machine Translation with Reading Information
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/yamada.mp4" label="Japanese-language video introducing Japanese-to-English machine translation research" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2025 Annual Conference" >}}
<ul>
<li>Use large language models to translate descriptions of monuments to poems from the <em>Man'yōshū</em></li>
<li>Improve translation by providing readings for difficult personal and place names that frequently occur in the descriptions</li>
<li>Use a large language model to identify difficult words and manually annotate their readings</li>
<li>Next step: automatically create and expand reading-information resources for difficult words</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

## Language Analysis
### Data Augmentation for Japanese Named Entity Recognition
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/okazaki.mp4" label="Japanese-language video introducing research on Japanese named entity recognition" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2025 Annual Conference" >}}
<ul>
<li>Identify key named entities in text, including proper names and numerical expressions</li>
<li>Automatically create additional training data by replacing named entities with others of the same type</li>
<li>Use large language models to generate effective replacement data</li>
<li>Next step: improve data augmentation by accounting for writing style and context</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

## Applications of Natural Language Processing
### Japanese Grammatical Error Correction
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2026/yoneda.mp4" label="Japanese-language video introducing research on Japanese grammatical error correction" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2026 Annual Conference" >}}
<ul>
<li>Automatically correct grammatical errors made by beginning learners of Japanese</li>
<li>Analyze accuracy in correcting inflectional-ending errors for <em>na</em>-adjectives (adjectival nouns)</li>
<li>Find that correction accuracy tends to decrease for words written in hiragana</li>
<li>Next step: evaluate Japanese grammatical error correction using large language models</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

### Analysis of Social Media Posts Related to Mental Health Difficulties
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/takabatake.mp4" label="Japanese-language video introducing research on social media analysis" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2025 Annual Conference" >}}
<ul>
<li>Identify language in social media posts that is associated with mental health difficulties</li>
<li>Use large language models to extract keywords that may be characteristic of people experiencing mental distress</li>
<li>Analyze the extracted expressions in a large collection of social media posts</li>
<li>Next steps: extract longer expressions and infer the meaning of entire posts</li>
</ul>
<div align="right">In collaboration with Professor Yoshinobu Kano, Shizuoka University</div>
{{< /card >}}
{{< /cardpane >}}

### Suggestions for Revising Written Text
{{< cardpane >}}
{{< card >}}
    {{< video src="/videos/2025/sawada.mp4" label="Japanese-language video introducing research on writing support" >}}
{{< /card >}}
{{< card header="**Research Highlights**" footer="JSAI 2025 Annual Conference" >}}
<ul>
<li>Use large language models to help people revise their writing</li>
<li>Ask a large language model to identify points for improvement in Japanese research paper abstracts</li>
<li>Evaluate three types of prompts using nearly 100 abstracts</li>
<li>Next step: extend the approach to types of writing other than research papers</li>
</ul>
{{< /card >}}
{{< /cardpane >}}

For related publications, see the [publication list](../publications/).
