from setuptools import setup, find_packages

setup(
    name="rdp_holiday",
    version="0.1",
    description="A Dumb RDP to JSON tool https://www.youtube.com/watch?v=ceR4TDuqE5A",
    author="Will Metcalf",
    author_email="william.metcalf@gmail.com",
    url="https://github.com/wmetcalf/rdp_holiday", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "certvalidator",
        "asn1crypto",
        "mscerts",
    ],
    entry_points={
        "console_scripts": [
            "rdp_holiday=rdp_holiday.rdp_holiday:main", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
