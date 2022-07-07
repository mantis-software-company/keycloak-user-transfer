import setuptools

setuptools.setup(
    name="keycloak-user-transfer",
    version="1.0.0",
    author="Furkan Kalkan",
    author_email="furkankalkan@mantis.com.tr",
    description="Yet another tool for transferring users from PostgreSQL to Keycloak using Keycloak REST API.",
    url="https://github.com/mantis-software-company/change-event-service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['httpx~=0.23.0', 'psycopg2-binary~=2.9.3', 'PyYAML~=6.0',  'retry~=0.9.2'],
    python_requires=">3.8.*, <4",
    scripts=['src/keycloak-user-transfer']
)