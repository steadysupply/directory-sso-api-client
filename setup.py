"""
Export Directory API client
"""
import ast
import pip.download
from pip.req import parse_requirements
import re
from setuptools import setup, find_packages


def get_version():
    pattern = re.compile(r'__version__\s+=\s+(.*)')

    with open('directory_sso_api_client/version.py', 'rb') as src:
        return str(ast.literal_eval(
            pattern.search(src.read().decode('utf-8')).group(1)
        ))


def get_requirements():
    return [str(r.req) for r in list(parse_requirements(
        'requirements.txt',
        session=pip.download.PipSession()
    ))]


setup(
    name='directory_sso_api_client',
    version=get_version(),
    url='https://github.com/uktrade/directory-sso-api-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Export Directory.',
    packages=find_packages(),
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=get_requirements()
)
