import os

import setuptools


def read(rel_path):
    base_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_path, rel_path), 'r') as f:
        return f.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError('Unable to find version string.')


if __name__ == '__main__':
    setuptools.setup(
        name='paddle-fid',
        version=get_version(os.path.join('src', 'paddle_fid', '__init__.py')),
        author='Yu Kaimin',
        description=('Package for calculating Fréchet Inception Distance (FID) using PaddlePaddle'),
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        url='https://github.com/mseitzer/pytorch-fid',
        package_dir={'': 'src'},
        packages=setuptools.find_packages(where='src'),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
        ],
        python_requires='>=3.5',
        entry_points={
            'console_scripts': [
                'paddle-fid = paddle_fid.fid_score:main',
            ],
        },
        install_requires=[
            'numpy',
            'pillow',
            'scipy',
        ]
    )
