# 🚀 rtftree --- Terraform Project Tree Generator CLI

> A professional-grade CLI tool to generate clean, structured, and
> shareable Terraform project trees --- with smart exclude support,
> colored output, and Markdown export.

------------------------------------------------------------------------

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![CLI](https://img.shields.io/badge/type-CLI-orange.svg)
![Terraform](https://img.shields.io/badge/terraform-supported-purple.svg)

------------------------------------------------------------------------

## 📌 Why rtftree?

Terraform projects often include:

-   `.terraform/`
-   `terraform.tfstate`
-   `.terraform.lock.hcl`
-   `.git/`
-   Provider binaries
-   Deeply nested modules

Sharing structure manually becomes messy and unreadable.

🔥 **rtftree solves this problem** by generating a clean, structured tree
view of your infrastructure project --- ready for documentation,
sharing, and audits.

------------------------------------------------------------------------

# ✨ Features

✅ Beautiful tree-style output\
✅ 🎨 Colored CLI output\
✅ Optional file content preview\
✅ Smart exclude support (like `.gitignore`)\
✅ Wildcard pattern support (`*.exe`, `.terraform*`)\
✅ Exclude via file (`--exclude-file`)\
✅ Markdown export mode (`--markdown`)\
✅ Output to file (`-o`)\
✅ Lightweight & Fast\
✅ Installable as a CLI tool

------------------------------------------------------------------------

# 📦 Installation

## 🔹 Local Install (Development Mode)

``` bash
python -m pip install -e .
```

## 🔹 Standard Install

``` bash
python -m pip install .
```

## 🔹 After PyPI Publish (Global Install)

``` bash
pip install rtftree
```

------------------------------------------------------------------------

# 🚀 Usage

## Basic Usage

``` bash
rtftree <project-folder>
```

Example:

``` bash
rtftree .
```

------------------------------------------------------------------------

## 📁 Structure Only (No File Content)

``` bash
rtftree . --no-content
```

------------------------------------------------------------------------

## 🚫 Exclude Files & Folders

### Direct Patterns

``` bash
rtftree . --exclude .terraform .git terraform.tfstate *.exe
```

### Using Exclude File

``` bash
rtftree . --exclude-file exclude.txt
```

Example `exclude.txt`:

    .terraform
    .git
    terraform.tfstate
    *.exe
    .terraform.lock.hcl

Supported:

-   Exact file names
-   Folder names
-   Wildcards

------------------------------------------------------------------------

## 💾 Save Output to File

``` bash
rtftree . -o infra_tree.txt
```

------------------------------------------------------------------------

## 📝 Markdown Export Mode

Generate Markdown-ready structure:

``` bash
rtftree . --markdown -o structure.md
```

Perfect for:

-   GitHub documentation
-   Wiki pages
-   Confluence
-   Client documentation

------------------------------------------------------------------------

# 🖥 Example Output

    📁 Terraform Project: infra

    ├── 📁 modules
    │   ├── 📄 main.tf
    │   │   resource "azurerm_resource_group" "rg" {
    │   │       name     = "example"
    │   │       location = "East US"
    │   │   }
    │   └── 📄 variables.tf
    │       variable "location" {
    │           type = string
    │       }
    └── 📄 provider.tf

------------------------------------------------------------------------

# ⚙️ CLI Options

  Option             Description
  ------------------ ------------------------------------
  `--no-content`     Show only folder/file structure
  `--exclude`        Space-separated patterns to ignore
  `--exclude-file`   Load exclude patterns from file
  `--markdown`       Export output in Markdown format
  `-o`, `--output`   Write output to file

------------------------------------------------------------------------

# 🏗 Project Structure

    rtftree/
    │
    ├── rtftree/
    │   ├── __init__.py
    │   └── cli.py
    │
    ├── pyproject.toml
    └── README.md

------------------------------------------------------------------------

# 🔥 DevOps Use Cases

-   Share Terraform structure in tickets
-   Infrastructure documentation
-   CI/CD pipeline documentation
-   Client infrastructure overview
-   Audit reporting
-   Pre-deployment reviews

------------------------------------------------------------------------

# 🌍 PyPI Publishing

Once published to PyPI, anyone can install globally:

``` bash
pip install rtftree
```

This makes rtftree a globally accessible DevOps utility tool.

------------------------------------------------------------------------

# 🧠 Roadmap

-   `.treeignore` auto-detection
-   `--max-depth` option
-   Terraform-only mode (`*.tf`)
-   JSON export
-   GitHub Action integration
-   Auto documentation mode

------------------------------------------------------------------------

# 👨‍💻 Author

**Ritesh Sharma**\
DevOps \| Azure \| Terraform \| Kubernetes

------------------------------------------------------------------------

# 📄 License

MIT License

------------------------------------------------------------------------

# ⭐ Support

If you find this tool useful:

⭐ Star the repository\
🚀 Share with DevOps community\
🛠 Contribute improvements

------------------------------------------------------------------------

> Built with ❤️ for DevOps Engineers