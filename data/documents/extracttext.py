import os
import yaml
import re

from newspaper import Article


def remove_prefix_from_path(path, prefix):
    path = os.path.normpath(path)
    prefix = os.path.normpath(prefix)
    if path.startswith(prefix):
        return path[len(prefix):].lstrip(os.sep)
    return path


def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        article = Article('')
        article.set_html(content)
        article.parse()
        return article.text


def clean_string(input_string):
    # Remove multiple spaces
    cleaned_string = re.sub(r'\s+', ' ', input_string)
    # Remove empty lines
    cleaned_string = os.linesep.join(
        [line for line in cleaned_string.splitlines() if line.strip()])
    return cleaned_string


def recurse_and_extract_text(root_folder):
    documents = []
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                text = extract_text_from_html(file_path)
                text = clean_string(text)
                file_path = remove_prefix_from_path(file_path, './raw/_site')
                if len(text) > 0:
                    documents.append({'key': file_path, 'document': text})

    with open('documents.yaml', 'w') as yaml_file:
        yaml.dump({'documents': documents},
                  yaml_file, default_flow_style=False)


if __name__ == "__main__":
    root_folder = './raw/'
    recurse_and_extract_text(os.path.expanduser(root_folder))
