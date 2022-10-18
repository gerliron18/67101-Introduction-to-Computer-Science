#!/usr/bin/env python3
import sys
import tempfile
import zipfile
import shutil
import os
from autotest import filelist_test,res_code
from test import run_all_tests


def run():
    EX = "ex7"
    required = ["README", "ex7.py"]

    print("Test script for " + EX)

    if not os.path.isfile(EX + ".zip"):
       print("File not found. Exiting...")
       print("Make sure " + EX + ".zip is in the same directory.")
       exit(-1)

    try:
        if not filelist_test(EX + ".zip", required, format='zip'):
            exit(-1)
    except Exception as i:
        res_code("zipfile",output="Testing zip file failed...")
        exit(-1)

    # Make a temp dir
    tmp_dir = tempfile.mkdtemp()

    # Extract the zip
    zip_ref =  zipfile.ZipFile(EX + ".zip", 'r')
    zip_ref.extractall(tmp_dir)
    zip_ref.close()

    # Add to path
    sys.path.append(tmp_dir)

    # Run tests
    run_all_tests(EX + "tests")
    run_all_tests(EX + "tests_full")

    # Delete temp dir
    shutil.rmtree(tmp_dir)

if __name__ == "__main__":
    run()
