cmake_minimum_required(VERSION 3.27)
project(Test)

set(CMAKE_C_STANDARD 23)
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/../cmake-modules)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_compile_options(-std=gnu2x -Wall -Wextra -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -Wno-sign-conversion)
include_directories(../include ../lib)

include(CTest)
enable_testing()

add_executable(sample sample.c)
add_test(NAME it_works COMMAND $<TARGET_FILE:sample>)

