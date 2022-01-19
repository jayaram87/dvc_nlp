from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO = "DVC-NLP-CMP"
AUTHOR_USER_NAME = "jayaram87"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for DVC-NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO}",
    author_email="jayaramraja1987@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)