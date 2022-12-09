from ConverPDFToImageFunc import convertPDFBatch
import argparse

# Code Driver
if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-i", "--InputPath", help="Input Directory")
    parser.add_argument("-o", "--OutputPath", help="Output Directory")
    parser.add_argument("-p", "--PrefixPage",
                        help="Prefix for rename image results", default='page')

    # Read arguments from command line
    args = parser.parse_args()
    if args.InputPath and args.OutputPath:
        convertPDFBatch(args.InputPath, args.OutputPath, args.PrefixPage)
    else:
        print("python pdf_to_image.py -h")
