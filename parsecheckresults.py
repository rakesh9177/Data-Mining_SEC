import argparse
import csv
import os
import shutil

import pandas as pd


def create_parser():
    """Argument Parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,
                        default="./data", help="path to form10k parsed data")
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    form10k_path = os.path.join(args.data_dir, 'form10k.parsed')
    mda_path = os.path.join(args.data_dir, 'mda')

    dir_list_form10k = os.listdir(form10k_path)
    dir_list_mda = os.listdir(mda_path)

    TotalFilesParsed = len(dir_list_form10k)
    TotalMDAfiles = len(dir_list_mda)

    successlist = []
    failurelist = []


    new_form10k_list = [x[:-4] for x in dir_list_form10k]
    new_mda_list = [x[:-4] for x in dir_list_mda]


    for mda in new_mda_list:
        if mda in new_form10k_list:
            successlist.append(mda)
            new_form10k_list.remove(mda)

    failurelist = new_form10k_list

    with open(os.path.join(args.data_dir,'result.csv'),'w') as result:
        writer = csv.writer(result)
        writer.writerow(['Form10K', 'MDA Parsing Status'])
        for s in successlist:
            writer.writerow([s, "SUCCESS"])
        for f in failurelist:
            writer.writerow([f, "FAILED"])



if __name__ == '__main__':
    main()


