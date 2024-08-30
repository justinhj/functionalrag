# RAG play
## What this?
A simple example of generating embeddings from a website and then querying them using a user query's embedding.
Not really RAG but whatev.
## How?
I am using the voyageapi embeddings api to process all the documents on my site. Then when a query is entered we calculate the embedding and use cosine similarity to find the nearest matching documents.
https://docs.voyageai.com/docs/embeddings
## Data
For grabbing the data, in my example I use my website repository at https://github.com/justinhj/justinhj.github.io.

## Generate embeddings
generateembeddings.py uses the voyage api embeddings api to create a new embeddings.yaml that includes the documents and keys

## RAG query generator
Run with query and optionally the number of results to return and it will return the nearest matching articles by nearest cosine.
ragquery.py

Examples:

```bash
Key: 2007/10/24/c-and-c-function-pointers.html, Similarity: 0.7219962317075135
Key: talks.html, Similarity: 0.702334435278166
Key: 2018/05/04/hacker-news-api-4.html, Similarity: 0.6962310721555498
Key: 2019/06/10/monoids-for-production.html, Similarity: 0.6813700904160662
Key: 2010/12/15/f-vs-c.html, Similarity: 0.6794065323389931

> python ragquery.py 'pointers in c' 5
Key: 2007/10/24/c-and-c-function-pointers.html, Similarity: 0.7593628981277829
Key: 2009/05/14/linking-mingw32-with-psapi.html, Similarity: 0.5921157057862669
Key: 2009/02/16/algorithm-bug-fixes.html, Similarity: 0.5791199816943892
Key: 2008/05/27/using-find-and-printf.html, Similarity: 0.5748169153475651
Key: 2019/06/10/monoids-for-production.html, Similarity: 0.5745724492258085

> python ragquery.py 'video game ai' 5
Key: 2007/10/09/avoiding-ten-common-game-ai-mistakes.html, Similarity: 0.7418870497777483
Key: 2009/02/16/who-uses-a-code.html, Similarity: 0.6060142847730559
Key: 2009/02/16/algorithm-bug-fixes.html, Similarity: 0.5932392265916293
Key: 2009/03/18/vancouver-game-companies.html, Similarity: 0.56107726981772
Key: 2010/12/15/f-vs-c.html, Similarity: 0.5397341003976411

> python ragquery.py 'path finding' 5
Key: 2009/02/16/algorithm-bug-fixes.html, Similarity: 0.7795118773814612
Key: 2007/10/09/avoiding-ten-common-game-ai-mistakes.html, Similarity: 0.7339350552028187
Key: 2009/02/16/who-uses-a-code.html, Similarity: 0.7192187376961887
Key: 2009/03/18/vancouver-game-companies.html, Similarity: 0.5651499527823654
Key: 2009/09/08/directional-window-movement-in-emacs.html, Similarity: 0.5580793489970282
```
