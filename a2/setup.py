import setuptools
import subprocess


required_packages = [
    'vaderSentiment',
    'NRCLex',
    'pandas',
    'sentic',
    'textblob',
]

setuptools.setup(
    name='A2',
    version='1.0.0',
    description='Package for CGSC 3601 A2.',
    url='#',
    author='Sean Riley',
    install_requires=required_packages,
    author_email='seanriley@cmail.carleton.ca',
    packages=setuptools.find_packages(),
    zip_safe=False
)

cmd = ['python3','-m','textblob.download_corpora']
subprocess.run(cmd)
