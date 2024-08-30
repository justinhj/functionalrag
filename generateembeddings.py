import voyageai
import yaml


def read_yaml_to_array(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        documents = [item['document'] for item in data['documents']]
        keys = [item['key'] for item in data['documents']]
    return documents, keys


vo = voyageai.Client()

documents, keys = read_yaml_to_array('data/documents/documents.yaml')

# Embed the documents
embeddings = documents_embeddings = vo.embed(
    documents, model="voyage-large-2-instruct", input_type="document"
).embeddings

data = {
    "embeddings": [
        {"key": key, "document": doc, "embedding": emb}
        for key, emb, doc in zip(keys, embeddings, documents)
    ]
}

# Write to YAML file
with open('data/documents/embeddings.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
