class Command:
    def __init__(self, command):
        self.command = command
        self.output = []

    def add_output(self, string):
        self.output.append(string)

    def print(self):
        print(self.command)
        for line in self.output:
            print(f"  {line}")


class File:
    def __init__(self, name, size=0, is_dir=True, parent=None, level=0):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.parent = parent
        self.files = dict()
        self.level = level

        if parent and parent.name != "/":
            self.path = f"{parent.path}/{name}"
        elif self.name == "/":
            self.path = "/"
        else:
            self.path = f"/{name}"

    def execute_command(self, command):
        """Executes a command and returns the new working directory"""
        if command.command.startswith("cd"):
            return self.cd(command.command[3:])

        elif command.command.startswith("ls"):
            for line in command.output:
                if line.startswith("dir"):
                    self.add_subdirectory(line[4:])

                elif line[0].isnumeric():
                    size, name = line.split()
                    size = int(size)
                    self.add_subdirectory(name, size=size, is_dir=False)
            return self

    def add_subdirectory(self, name, size=0, is_dir=True):
        self.files[name] = File(
            name, size=size, is_dir=is_dir, parent=self, level=self.level + 1
        )
        if not is_dir:
            self.update_size(size)

    def update_size(self, size):
        self.size += size
        if self.parent:
            self.parent.update_size(size)

    def cd(self, directory):
        if directory == "..":
            return self.parent
        return self.files[directory]

    def print(self):
        if self.is_dir:
            info = f"(dir, size={self.size})"
        else:
            info = f"(file, size={self.size})"
        print("| " * self.level + f"{self.name} {info}")
        for file in self.files.values():
            file.print()


def parse_input(filename):
    commands = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if line.startswith("$"):
                commands.append(Command(line[1:].strip()))
            else:
                commands[-1].add_output(line.strip())

    return commands


def browse_filesystem(commands):
    root = File("/")
    wd = root

    files = {"/": root}

    for command in commands[1:]:
        wd = wd.execute_command(command)
        if wd.path not in files:
            files[wd.path] = wd

    return root, files


def main():
    filename = "input.txt"
    commands = parse_input(filename)

    root, files = browse_filesystem(commands)
    root.print()

    MAX_FILESIZE = 100000

    ans = 0
    for file in files.values():
        if file.is_dir and file.size <= MAX_FILESIZE:
            ans += file.size

    print(ans)


if __name__ == "__main__":
    main()
