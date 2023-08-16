# Text_File_Parse_Functions
Function definitions to parse text files and extract information.

## General
### extract_file_paths(root_filepath, skip_folders, required_files)
#### Dependencies:
    import os
#### Notes:
  root_filepath - of top-level folder.  
  skip_folders - list of strings - skip folders with names containing provided strings (not case sensitive).  
  required_files - list of strings - extract paths of files containing these strings.  
  returns a list of file paths (strings).  

  
## Specific
### extract_assurance_report_data(filepaths)
#### Dependencies:
    import pandas as pd
#### Notes:
  filepaths - list of assurance report strings - pulls out data from the report.  
  returns pandas dataframe containing the data.  
