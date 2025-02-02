import os
import argparse
import time
import shutil
import sys
sys.path.append('../src')
from clustering import Clustering

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--design", help="design_name: ariane, MegaBoom_x2 ", type = str, default = "ariane")
    parser.add_argument("--fixed_file", help="fixed file generated by grouping", type = str, default = "./fix_files_grouping/ariane.fix")
    parser.add_argument("--global_net_threshold",  help = "large net threshold", type = int, default = 500)
    parser.add_argument("--Nparts",  help = "number of clusters (only for hmetis, default  = 500)", type = int, default = 500)
    parser.add_argument("--setup_file", help = "setup file for openroad (default = setup.tcl)", type = str, default = "setup.tcl")
    args = parser.parse_args()

    design = args.design

    # The fixed file should be generated by our grouping script in the repo.
    fixed_file = args.fixed_file
    global_net_threshold = args.global_net_threshold
    Nparts = args.Nparts
    setup_file = args.setup_file

    # To use the grouping function, you need to specify the directory of src file
    src_dir = "../src"
    result_dir = "./results"
    n_cols = 27
    n_rows = 23
    openroad_exe = "./openroad"  # Please specify your own openroad exe file

    Clustering(design, src_dir, fixed_file, n_cols, n_rows, global_net_threshold, Nparts, setup_file, openroad_exe)



