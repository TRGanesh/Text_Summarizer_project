import setuptools

with open('README.md','r',encoding='utf-8') as f:
   long_description = f.read()
   
__version__ = '0.0.0'

REPO_NAME = 'Text_Summarizer_project'
AUTHOR_USER_NAME = 'TRGanesh'
SRC_REPO = 'text_summarizer'
AUTHOR_EMAIL = 'trtr2823@gmail.com'

setuptools.setup(
   name = SRC_REPO,
   version = __version__,
   author = AUTHOR_USER_NAME,
   author_email = AUTHOR_EMAIL,
   description = 'Small Python Package for Text Summarization',
   long_description = long_description,
   long_description_content_type = 'text/markdown',
   url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
   project_urls = {
      'Bug Tracker' : f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
   },
   package_dir = {'':'src'},
   packages = setuptools.find_packages(where='src')
)