import setuptools
import io
from KrxApi.__version__ import __version__


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


metadata = dict(
    name="KrxApi",
    version=__version__,
    description="A python package for get stock data of Korea. Data source is Korea Exchange(KRX)",
    long_description=long_description(),
    url="https://github.com/osakaBlues/KrxApi",
    install_requires=[
        "pandas",
        "requests"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3"
)


def setup_package():
    setuptools.setup(**metadata)


if __name__ == "__main__":
    setup_package()
