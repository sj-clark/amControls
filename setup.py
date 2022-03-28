from setuptools import setup, find_packages

setup(
    name='amcontrols',
    version=open('VERSION').read().strip(),
    author='Samuel Clark',
    url='https://github.com/xray-imaging/amcontrols',
    packages=find_packages(),
    include_package_data = True,
    description='Module to control Additive Manufacturing at beamline 32-ID',
    zip_safe=False,
)