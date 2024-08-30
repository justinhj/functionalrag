# RAG play
## Data
For grabbing the data, in my example I use my website repository at https://github.com/justinhj/justinhj.github.io.

## Generate embeddings
generateembeddings.py uses the voyage api embeddings api to create a new embeddings.yaml that includes the documents and keys

## RAG query generator
Run with query and optionally the number of results to return and it will return the nearest matching articles by nearest cosine.
ragquery.py

