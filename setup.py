import setuptools
'''
with open("README.md", "r") as fh:
    long_description = fh.read()
'''
setuptools.setup(
    name='py_tool_box',  
    version='0.1',
    author="Wang Shengyu",
    author_email="wang.d.shengyu@gmail.com",
    description="A tool box",
    long_description="no long desc",
    long_description_content_type="text/markdown",
    url="https://github.com/wangshengyu/nonono",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pytoolbox=py_tool_box.command:run'
        ],
    },
 )
