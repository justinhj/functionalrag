# Data
## Step 1: Copy the site html 
I downloaded my website to a folder and ran the following to copy the data to the data folder:
```bash
fd '.*\.html' _site -0 | rsync --files-from=- --from0 ./ ~/projects/functionalrag/data/documents/raw/
```


