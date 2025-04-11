package subsequences

// This imports the `fmt` package from the core collection. You find the core
// collection in `<odin>/core`, where `<odin>` is the folder where you installed
// Odin. `fmt` is just a subfolder of `core`. Again, packages are just folders!
import "core:fmt"

// This is a procedure. A procedure contains code that can be executed. This
// procedure is special: By default, the program starts in the procedure called
// `main`.
main :: proc() {
	// The `fmt.println` procedure is part of the `core:fmt` package. It prints
	// text to the "standard output stream", which could mean:
	// - Terminal
	// - Command prompt
	// - Code editor output window
	fmt.println("Hellope!") // Prints "Hellope!" to the console

}