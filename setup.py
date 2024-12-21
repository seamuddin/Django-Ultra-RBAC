from setuptools import setup, find_packages

setup(
    name="django-ultra-rbac",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="A flexible RBAC system for Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seamuddin/django-ultra-rbac",
    author="Seam Uddin",
    author_email="seamuddin.me@gmail.com",
    install_requires=[
        "Django>=3.2",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
    ],
)
