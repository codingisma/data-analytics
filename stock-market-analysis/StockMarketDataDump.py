from utils.FileDownloader import *
from utils.TransformPandas import *
import utils.Constants
import time

def main():
    # Your main code goes here
    cleanup_files()
    write_headers()
    download_data()

    transform_data()
if __name__ == "__main__":
    main()