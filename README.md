# batch-image2pdf
Utitlity batch processing of convert document PDF to Image. This converter based on Poppler engine to help convert batch document PDF to images.

# Feature
- Able to selective convert based on file extensions, only pdf file will proceed.
- Able to compress document PDF to images.
- Able to grouping conversion result into output specific output folder.

# Environtment
- Python 3.6+ (https://www.python.org/downloads/)
- Poppler (https://github.com/freedesktop/poppler)
- pdf2image (https://pypi.org/project/pdf2image/)

# Help
Get help command and parameter usage for this repository
```bash
    python pdf_to_image.py -h
```

# How to run (output name with default prefix)
You can use predefined prefix name to output filename images. Batch compress result will be saved at your "output" directory definition
```bash
    python pdf_to_image.py -i <directory_input> -o <directory_output>
```

https://user-images.githubusercontent.com/19168382/206652281-b7f0c1a6-1943-41fe-a10c-4fe8ec651f9f.mov



# How to run (from custom output directory)
You can use custom prefix name to output filename images. Batch compress result will be saved at your "output" directory definition
```bash
    python pdf_to_image.py -i docs -o output_images -p my-page
```

https://user-images.githubusercontent.com/19168382/206653326-7c2d347a-7c6c-47be-a101-941ef6b89ac3.mov


# Parameters Descriptions
- -i = assign parameter input directory
- -o = assign parameter output directory
- -p = assign parameter prefix name output


