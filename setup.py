import setuptools
from pathlib import Path

def get_data_files():
    files = [ ("fabsible/" + "/".join(x.parent.parts[3:]), ["/".join(x.parts)]) for x in Path('lib/fabsible/data').glob('**/*') if x.is_file() and ('/.git/' not in str(x) and not str(x).endswith('.git'))]
    return files

setuptools.setup(
    name="fabsible",
    version="0.0.1",
    author="TORGiren",
    author_email="exphost@fabrykowski.pl",
    description="A small example package",
    long_description="long description...",
    long_description_content_type="text/markdown",
    url="https://github.com/exphost/fabsible",
    package_dir={'':'lib'},
    packages=setuptools.find_packages('lib'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'ansible >= 2.8'
        ],
    scripts=[
      "bin/fabsible-hello",
      "bin/fabsible-hello2",
      "bin/fabsible-init",
      "bin/fabsible-play",
    ],
    include_package_data = True,
    data_files = get_data_files()

)
