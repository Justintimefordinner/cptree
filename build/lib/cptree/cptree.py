import os
from pathlib import Path


class DirectoryTree:
    """Generates a directory tree representation."""

    def __init__(self, root_dir, dir_only=False, output_file=None):
        """
        Initialize the DirectoryTree object.

        Args:
            root_dir (str or Path): The root directory to generate the tree for.
            dir_only (bool, optional): Only include directories in the tree. Defaults to False.
            output_file (str or Path, optional): The file to write the tree output to. Defaults to None.
        """
        self.root_dir = Path(root_dir)
        self.dir_only = dir_only
        self.output_file = output_file
        self._tree = []

    def generate(self):
        """Generate the directory tree."""
        self._tree_body(self.root_dir, "")

        if self.output_file:
            with open(self.output_file, "w", encoding="utf-8") as file:
                file.write("\n".join(self._tree))
        else:
            print("\n".join(self._tree))

    def _tree_body(self, directory, prefix):
        """
        Generate the tree body for a directory.

        Args:
            directory (Path): The directory to generate the tree body for.
            prefix (str): The prefix string for the current level of the tree.
        """
        entries = sorted(directory.iterdir())

        for index, entry in enumerate(entries):
            is_last_entry = index == len(entries) - 1
            connector = "└──" if is_last_entry else "├──"

            if entry.is_dir():
                self._add_directory(entry, index, len(entries), prefix, connector)
            elif not self.dir_only:
                self._add_file(entry, prefix, connector)

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        """
        Add a directory entry to the tree.

        Args:
            directory (Path): The directory to add to the tree.
            index (int): The index of the directory in the current level.
            entries_count (int): The total number of entries in the current level.
            prefix (str): The prefix string for the current level of the tree.
            connector (str): The connector string to use for the directory entry.
        """
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        prefix += "│  " if index != entries_count - 1 else "    "
        self._tree_body(directory, prefix)
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        """
        Add a file entry to the tree.

        Args:
            file (Path): The file to add to the tree.
            prefix (str): The prefix string for the current level of the tree.
            connector (str): The connector string to use for the file entry.
        """
        self._tree.append(f"{prefix}{connector} {file.name}")
