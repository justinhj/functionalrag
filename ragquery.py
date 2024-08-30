import voyageai
import yaml
import numpy as np
import sys


def read_yaml_to_arrays(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        documents = [item['document'] for item in data['embeddings']]
        keys = [item['key'] for item in data['embeddings']]
        embeddings = [item['embedding'] for item in data['embeddings']]
    return documents, keys, embeddings


documents, keys, embeddings = read_yaml_to_arrays(
    'data/documents/embeddings.yaml')

vo = voyageai.Client()


def rag_query(query, topn):
    query_embedding = vo.embed(
        [query], model="voyage-large-2-instruct", input_type="query"
    ).embeddings[0]
    similarity_values = np.dot(embeddings, query_embedding)
    similarities = [{"index": idx, "similarity": sim} for idx, sim in
                    enumerate(similarity_values)]
    sorted_similarities = sorted(similarities, key=lambda x: x["similarity"],
                                 reverse=True)
    return sorted_similarities[:topn]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ragquery.py <query> <top_n>")
        sys.exit(1)

    query = sys.argv[1]
    try:
        top_n = int(sys.argv[2])

        result_keys = rag_query(query, top_n)
        for item in result_keys:
            print(f"Key: {keys[item['index']]}, Similarity: {item['similarity']}")
    except ValueError:
        print("The top_n parameter must be an integer.")
        sys.exit(1)
