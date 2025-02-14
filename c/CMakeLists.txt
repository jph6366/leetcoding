cmake_minimum_required(VERSION 3.27)

get_filename_component(PROJECT_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)
project(${PROJECT_NAME} VERSION 0.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake-modules)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_compile_options(-std=gnu2x -Wall -Wextra -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -Wno-sign-conversion)
include_directories(include lib)

add_executable(${PROJECT_NAME}
    src/main.c
)

set_target_properties(${PROJECT_NAME} PROPERTIES VERSION ${PROJECT_VERSION})
target_compile_definitions(${PROJECT_NAME} PRIVATE
    PROJECT_NAME="${PROJECT_NAME}"
    PROJECT_VERSION_MAJOR=${PROJECT_VERSION_MAJOR}
    PROJECT_VERSION_MINOR=${PROJECT_VERSION_MINOR}
    PROJECT_VERSION_PATCH=${PROJECT_VERSION_PATCH}
)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(${PROJECT_NAME} PRIVATE -g3 -fsanitize=undefined -fsanitize-trap)
    target_compile_definitions(${PROJECT_NAME} PRIVATE LOG_LEVEL=7)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_definitions(${PROJECT_NAME} PRIVATE LOG_LEVEL=-1)
endif()

target_link_libraries(${PROJECT_NAME} PRIVATE)

