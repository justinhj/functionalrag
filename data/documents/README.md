# Data
I downloaded my website to a folder and ran the following to copy the data to the data folder:
```bash
fd '.*\.html' _site -0 | rsync --files-from=- --from0 ./ ~/projects/functionalrag/data/documents/raw/
```

Run extracttext.py which extracts the article text, removes excess spaces and empty lines and write the documents to a yaml file `documents.yaml`.


