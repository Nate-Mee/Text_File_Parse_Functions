import os

# root_filepath - of top level folder - r"file path string".
# skip_folders - list of strings - skip folders with names containing provided strings (not case sensitive).
# required_files - list of strings - extract paths of files containing these strings.
# returns list of filepaths (strings).
def extract_file_paths(root_filepath, skip_folders, required_files):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(root_filepath):
        # traverse directory given as root_filepath
        for filename in filenames:
            for skip_string in skip_folders:
                # skip files in folders containing skip_folders strings
                if skip_string.lower() not in dirpath.lower():
                    for file_string in required_files:
                        # pull only paths containing required_files strings
                        if file_string.lower() in filename.lower():
                            file_paths.append(os.path.join(dirpath, filename))

    return file_paths

#---------------------------------------------------------------------------------------------------

import pandas as pd

# filepaths - list of assurance report filepath strings - pulls out data from the report.
# returns pandas dataframe containing the data.
def extract_assurance_report_data(filepaths):
    dict_list = []
    for path in filepaths:
        file_dict = {}
        fhand = open(path, 'r')
        # remove whitespace and split on ': '
        for line in fhand:
            line = line.rstrip()
            split = line.split(': ')
            # add lines which have a character after ': ' to file_dict
            if len(split) == 2 and split[1] != '':
                # clean commas from integers
                if ',' in split[1]:
                    split[1] = split[1].replace(',', '')
                file_dict[split[0]] = split[1]
        # add the dict created for the file to the list of dicts
        dict_list.append(file_dict)
    # convert the list of dicts into a pandas dataframe
    df = pd.DataFrame.from_dict(dict_list)
    # change datatypes of columns
    for column in df.columns:
        if 'Latest' in column:
            df[column] = pd.to_datetime(df[column], format='%d-%b-%y')
        else:
            df[column] = df[column].astype(int)
    return df
