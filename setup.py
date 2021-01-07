from setuptools import setup, find_packages
import re


def get_version():
    with open('./riskpy/__init__.py', 'rb') as f:
        version = re.search(
            r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
        ).group(1)

    return version

setup(
    name="riskpy",
    version=get_version(),
    author="zhouzhuofu",
    author_email="zhuofu.zhou@qq.com",
    packages=find_packages(),
)
