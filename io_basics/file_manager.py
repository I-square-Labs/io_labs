##########################################################################
#        for each file, check if file exists in media type mapping       #
#        if media type directory not exists, create media type directory #
#        move file to respective media type directory                    #
##########################################################################
import sys
import os
import shutil
from typing import (List, Dict)

USER_NAME:str = os.environ.get('USER', os.environ.get('USERNAME'))
DOWNLOAD_PATH: str = f"c:/Users/{USER_NAME}/Downloads/"
MEDIA_FILE_TYPE: Dict[str,List[str]] = {'Documents':['.txt','.pdf','.docx','.doc'],
                                        'Image':['.png','.jpg','.gif','.svg'],
                                        'Music':['.mp3'],
                                        'Video':['.mp4'],
                                        'Spreadsheet':['.xls','.csv','.xlsx'],
                                        'Webpage':['.html'],
                                        'Compressed':['.zip'],
                                        'Software':['.exe']

                                       }

def directory_file_manager(directory_path:str, 
                           media_file_type: Dict[str,List[str]] 
                           ) -> None:
    
    try:

        # get all directory files
        _directory_files: List = os.listdir(directory_path.strip())

        for _file in _directory_files:

            for _dir_name, _file_types in media_file_type.items():
                
                # check file extension from media file type
                if os.path.splitext(_file)[-1].lower() in _file_types:

                    _source_file_path: str = os.path.join(directory_path.strip(),_file)
                    _destination_file_path: str = os.path.join(directory_path.strip(),_dir_name.strip(),_file)

                    # make dir if not exist
                    if not os.path.isdir(os.path.dirname(_destination_file_path)):

                       os.makedirs(os.path.dirname(_destination_file_path), exist_ok=True)
                    
                    # move file 
                    shutil.move(_source_file_path, _destination_file_path)
                
    except Exception as ex:
        raise Exception(f"Something is broken, debug below:/n {str(ex)}")
    

if __name__ == "__main__":
    directory_file_manager(directory_path= DOWNLOAD_PATH, 
                           media_file_type= MEDIA_FILE_TYPE 
                          )
    


   



