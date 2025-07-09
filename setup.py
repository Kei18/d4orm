from setuptools import setup, find_packages

setup(name='d4orm',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'pandas',
        'matplotlib',
        'imageio',
        'tqdm',
        'tyro',
        'jax',
        'jaxopt'
        ]
)
