import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="xunit-wrapper",
    version="0.1.0",
    author="Fredrik Westermark",
    author_email="feffe.westermark@gmail.com",
    description="A wrapper for shell commands that generates xunit xml output",
    license="MIT",
    keywords="xunit junit xml shell command commands",
    url="https://github.com/feffe/xunit-wrapper",
    packages=["xunitwrapper"],
    install_requires=["junit-xml"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Quality Assurance",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": ["xunitwrap=xunitwrapper:wrap_shell_command"]},
    python_requires=">=3.6",
)
