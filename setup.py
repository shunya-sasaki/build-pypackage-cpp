from setuptools import setup
from setuptools import Extension

ext_module = Extension(
    name="mypack.cpp",
    sources=["src/mypack/cpp/hellocpp.cc"],
    libraries=["boost_python310"],
    include_dirs=[
        "/opt/homebrew/include",
        "/opt/homebrew/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/include/python3.10",
    ],
    library_dirs=[
        "/opt/homebrew/lib",
    ],
    extra_compile_args=['-std=c++11']
)

setup(py_module=["mypack"], ext_modules=[ext_module])
