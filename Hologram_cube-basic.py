def print_cube():
    # Each string in the list represents one line of the hologram cube.
    cube_lines = [
        "       +-------+",
        "      /       /|",
        "     +-------+ |",
        "     |       | +",
        "     |       |/ ",
        "     +-------+  "
    ]
    
    for line in cube_lines:
        print(line)

if __name__ == "__main__":
    print_cube()
