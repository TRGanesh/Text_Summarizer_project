import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)]:%(message)s:')

project_name = 'text_summarizer'

# WE CAN ADD,,ANY NEW FILE WHICH WE WANT TO ADD IN OUR FOLDERS,THAT FILE WILL GETS GENERATED AUTOMATICALLY
list_of_files = [
   '.github/workflows/.gitkeep',
   f'src{project_name}/__init__.py',
   f'src{project_name}/components/__init__.py',
   f'src{project_name}/utils/__init__.py',
   f'src{project_name}/utils/common.py',
   f'src{project_name}/logging/__init__.py',
   f'src{project_name}/config/__init__.py',
   f'src{project_name}/config/configuration.py',
   f'src{project_name}/pipeline/__init__.py',
   f'src{project_name}/entity/__init__.py',
   f'src{project_name}/constants/__init__.py',
   'config/config.yaml',
   'params.yaml',
   'app.py',
   'main.py',
   'Dockerfile',
   'requirements.txt',
   'setup.py',
   'research/trials.ipynb',
   'test.py'
]

for filepath in list_of_files:
   filepath = Path(filepath)  # GIVES PATH ACCORDING TO THE SYSTEM
   filedir , filename = os.path.split(filepath)  # SPLITS THE FILE PATH INTO CORRESPONDING DIRECTORY & FILE NAME (__INIT__.PY) & RETURNS THEM AS TUPLE
   
   # CREATING THE FILE DIRECTORIES,,FOR THAT CHECKING WHETHER FILEDIR EXITS(EMPTY)
   if filedir != '':  # FILE DIRECTORY NOT EQALS TO EMPTY
      os.makedirs(filedir,exist_ok=True) # IF FOLDER NOT EXISTS,,THEN ONLY IT CREATES,,
      
      # LOGGING THE THINGS,,MEANS WHENEVER THESE DIRECTORIES ARE BEING CREATED,,SOME INFO WILL BE DISPLAYED
      logging.info(f'Creating directory : {filedir} for file : {filename}')
      
   # FROM ABOVE IF LOOP,,WE CREATED FILE DIRECTORIES
   # NOW,WE HAVE TO CREATE FILES,,IN THOSE DIRECTORIES
   if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass # JUST OPENING / CREATING FILE (NOT ADDING ANY MATTER INTO IT)
         logging.info(f'Creating empty file {filepath}')
   
   else:
      logging.info(f'{filepath} is already existing')
      
# AFTER THIS,,OPEN TERMINAL AND RUN THIS FILE
      
      