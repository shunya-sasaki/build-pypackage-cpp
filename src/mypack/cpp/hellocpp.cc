/**
 * @file hellocpp.cc
 * @brief boost-python sample program 
 */
#include <iostream>
#include <boost/python.hpp>

namespace python = boost::python;

/**
 * @brief Output message to the standard output. 
 * 
 */
void hello_cpp()
{
    std::cout << "Hello World, Hello C++" << std::endl;
    return;
}

// The argument of BOOST_PYTHON_MODULE must be same to module name.
BOOST_PYTHON_MODULE(cpp){
    Py_Initialize();
    python::def("hello_cpp", hello_cpp);
}