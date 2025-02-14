# CMake-C-Template

This repository serves as a comprehensive example for setting up a C23 project using CMake and CTest, providing a meticulously organized and scalable project structure.

The file `CMakeLists.txt` contains settings that I personally use -- and recommend -- for every C project.

## Project Structure

```
├── cmake-build-debug/      # Folder for built debug application binary
├── cmake-build-release/    # Folder for built release application binary
├── cmake-build-tests/      # Folder for built test application binaries
├── cmake-modules/          # Folder for any custom .cmake modules
├── lib/                    # Folder for any dependencies
├── include/                # Folder for all include files
├── src/                    # Folder for all source files
│   └── main.c              # Main entry of the application
├── test/                   # Folder for all tests
│   ├── sample.c            # A sample test that does nothing
│   ├── test.h              # Simple and useful assertion macros
│   └── CMakeLists.txt      # Test compile script
├── CMakeLists.txt          # Compile script
```

## Instructions

### Compiling

1. Configure the Debug Build:
    ```sh
    cmake -B cmake-build-debug/ -DCMAKE_BUILD_TYPE=Debug
    ```

2. Build the Debug Application
    ```sh
    cmake --build cmake-build-debug/
    ```

3. Run the compiled debug application
    ```sh
    ./cmake-build-debug/$(basename $PWD)
    ```

4. Debugging

    ```sh
    # Debugging using LLDB
    lldb cmake-build-debug/$(basename $PWD)
    # Debugging using GDB
    gdb cmake-build-debug/$(basename $PWD)
    ```

### Tests

1. Set up the testing environment
    ```sh
    cmake -S test/ -B cmake-build-tests/ -DCMAKE_BUILD_TYPE=Debug
    ```

2. Build the test application
    ```sh
    cmake --build cmake-build-tests/
    ```

3. Run the tests
    ```sh
    ctest --test-dir cmake-build-tests
    ```

### Releasing

1. Configure the release build
    ```sh
    cmake -B cmake-build-release/ -DCMAKE_BUILD_TYPE=Release
    ```

2. Build the release application
    ```sh
    cmake --build cmake-build-release/
    ```

3. Run the compiled release application
    ```sh
    ./cmake-build-release/$(basename $PWD)
    ```

## clangd

If you're using clangd, consider creating the following symbolic links to the project root:
```sh
ln -s cmake-build-debug/compile_commands.json .
ln -s cmake-build-tests/compile_commands.json test
```
This will ensure your Language Server Protocol (LSP) can find and analyze all your code accurately.

## Suggestions

To optimize your development workflow, consider incorporating the following aliases into your `~/.bashrc` or `~/.zshrc`:

```sh
alias build='cmake -B cmake-build-debug/ -DCMAKE_BUILD_TYPE=Debug'
alias build-release='cmake -B cmake-build-release/ -DCMAKE_BUILD_TYPE=Release'
alias build-tests='cmake -S test/ -B cmake-build-tests/ -DCMAKE_BUILD_TYPE=Debug'

alias compile='cmake --build cmake-build-debug/'
alias compile-release='cmake --build cmake-build-release/'
alias compile-tests='cmake --build cmake-build-tests/'

alias run='./cmake-build-debug/$(basename $PWD)'
alias run-release='./cmake-build-release/$(basename $PWD)'
alias run-tests='ctest --test-dir cmake-build-tests -R'

alias debug='lldb cmake-build-debug/$(basename $PWD)' # or gdb instead of lldb
```

These aliases simplify common development tasks such as building, running, and testing your project, promoting a more efficient and enjoyable development experience.

