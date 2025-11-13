from setuptools import setup, find_packages

setup(
    name="house_prices_mlops",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.2.0",
        "matplotlib>=3.7.0",
    ],
    author="Votre Équipe",
    description="MLOps project for house price prediction",
    python_requires=">=3.8",
)
