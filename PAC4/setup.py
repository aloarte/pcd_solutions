from setuptools import setup, find_packages

setup(
    name='PAC4_aloarter',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)