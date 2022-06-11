from setuptools import setup
from setuptools import Extension

ext_module = Extension(
    name="pypack.cpp",
    sources=["src/pypack/cpp/hellocpp.cc"],
    libraries=["boost_python39"],
    include_dirs=[
        "/opt/homebrew/include",
        "/opt/homebrew/Cellar/python@3.10/3.10.4/Frameworks/Python.framework/Versions/3.10/include/python3.10",
    ],
    library_dirs=[
        "/opt/homebrew/lib",
        "/opt/homebrew/Cellar/python@3.10/3.10.4/Frameworks/Python.framework/Versions/3.10/lib/python3.10",
    ],
    extra_compile_args=['-std=c++11']
)

setup(py_module=["pypack"], ext_modules=[ext_module])
