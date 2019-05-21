import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='resumeparser',
    version='0.0.1',
    description='A utility to make parse data from resumes.',
    packages=['resumeparser'],
    url='https://github.com/awais786/ResumeParser',
    install_requires=[
        'gensim==3.7.1',
        'pandas==0.24.2',
        'pdfminer.six==20181108',
        'spacy==2.1.3',
        'PyYAML==5.1'
    ],
)
