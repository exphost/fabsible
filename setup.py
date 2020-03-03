import setuptools
import os
from pathlib import Path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_data_files():
    files = [ ("fabsible/" + "/".join(x.parent.parts[3:]), ["/".join(x.parts)]) for x in Path('lib/fabsible/data').glob('**/*') if x.is_file() and ('/.git/' not in str(x) and not str(x).endswith('.git'))]
    return files

setuptools.setup(
    name="fabsible",
    version="0.0.6",
    author="TORGiren",
    author_email="exphost@fabrykowski.pl",
    description="Ansible framework using object-oriented configuration",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/exphost/fabsible",
    package_dir={'':'lib'},
    packages=setuptools.find_packages('lib'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Installation/Setup",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.6',
    install_requires=[
        'ansible >= 2.8',
        'jmespath >= 0.9.4',
        ],
    scripts=[
      "bin/fabsible-init",
      "bin/fabsible-play",
    ],
    include_package_data = True,
    data_files = get_data_files()

)
