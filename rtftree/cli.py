import os
import argparse
import fnmatch
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown


# ---------------------------------------
# Utility Functions
# ---------------------------------------

def load_exclude_patterns(exclude_list, exclude_file):
    patterns = exclude_list.copy()

    if exclude_file and os.path.exists(exclude_file):
        with open(exclude_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)

    return patterns


def should_exclude(name, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(name, pattern):
            return True
    return False


# ---------------------------------------
# Tree Builder
# ---------------------------------------

def build_tree(directory, parent_tree, show_content=True, patterns=None):
    patterns = patterns or []

    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        parent_tree.add("[red]Permission Denied")
        return

    for item in items:
        if should_exclude(item, patterns):
            continue

        path = os.path.join(directory, item)

        if os.path.isdir(path):
            branch = parent_tree.add(f"[bold blue]📁 {item}")
            build_tree(path, branch, show_content, patterns)
        else:
            file_branch = parent_tree.add(f"[green]📄 {item}")

            if show_content:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        if not lines:
                            file_branch.add("[dim][empty file]")
                        else:
                            for line in lines[:20]:
                                file_branch.add(f"[dim]{line.rstrip()}")
                except Exception:
                    file_branch.add("[red][Error reading file]")


# ---------------------------------------
# Markdown Builder
# ---------------------------------------

def build_markdown(directory, show_content=True, patterns=None, prefix=""):
    patterns = patterns or []
    output = ""

    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        return ""

    for item in items:
        if should_exclude(item, patterns):
            continue

        path = os.path.join(directory, item)

        if os.path.isdir(path):
            output += f"{prefix}- 📁 **{item}**\n"
            output += build_markdown(path, show_content, patterns, prefix + "  ")
        else:
            output += f"{prefix}- 📄 `{item}`\n"

            if show_content:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        if lines:
                            output += f"{prefix}  ```\n"
                            for line in lines[:20]:
                                output += f"{prefix}  {line}"
                            output += f"{prefix}  ```\n"
                        else:
                            output += f"{prefix}  `[empty file]`\n"
                except:
                    output += f"{prefix}  `[Error reading file]`\n"

    return output


# ---------------------------------------
# Main CLI
# ---------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Terraform Tree CLI Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "folder",
        help="Project folder path"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output file path"
    )

    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        metavar="PATTERN",
        help=(
            "Exclude files/folders using names or wildcards.\n\n"
            "Examples:\n"
            "  --exclude .terraform .git terraform.tfstate\n"
            "  --exclude *.exe *.lock.hcl\n\n"
            "Supported:\n"
            "  • Exact file names (terraform.tfstate)\n"
            "  • Folder names (.terraform)\n"
            "  • Wildcards (*.exe, .terraform*)\n"
        ),
    )

    parser.add_argument(
        "--exclude-file",
        help=(
            "Path to file containing exclude patterns.\n"
            "One pattern per line.\n"
            "Lines starting with # are ignored."
        )
    )

    parser.add_argument(
        "--no-content",
        action="store_true",
        help="Show only folder/file structure (no file content preview)"
    )

    parser.add_argument(
        "--markdown",
        action="store_true",
        help="Export output in Markdown format"
    )

    args = parser.parse_args()

    patterns = load_exclude_patterns(args.exclude, args.exclude_file)
    folder_name = os.path.basename(os.path.abspath(args.folder))

    # MARKDOWN MODE
    if args.markdown:
        md_content = f"# 📁 Terraform Project: {folder_name}\n\n"
        md_content += build_markdown(
            args.folder,
            show_content=not args.no_content,
            patterns=patterns,
        )

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"\n✅ Markdown file written to: {args.output}")
        else:
            console = Console()
            console.print(Markdown(md_content))
        return

    # TREE MODE
    tree = Tree(f"[bold cyan]📁 Terraform Project: {folder_name}")

    build_tree(
        args.folder,
        tree,
        show_content=not args.no_content,
        patterns=patterns,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            file_console = Console(file=f, force_terminal=False, color_system=None)
            file_console.print(tree)
        print(f"\n✅ File written to: {args.output}")
    else:
        console = Console()
        console.print(tree)
