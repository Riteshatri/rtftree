# 🚀 rtftree --- Terraform Project Tree Generator CLI

> A powerful CLI tool to generate a clean and readable Terraform project
> tree structure --- with optional file content preview and smart
> exclude support.

------------------------------------------------------------------------

## 📌 Why rtftree?

Terraform projects often contain:

-   `.terraform/`
-   `terraform.tfstate`
-   `.terraform.lock.hcl`
-   `.git/`
-   provider binaries
-   large nested modules

Manually sharing structure becomes messy.

**rtftree solves this** by generating a structured tree view with:\*\*

-   📁 Folder hierarchy\
-   📄 File listing\
-   Optional file content preview\
-   Exclude support (like `.gitignore`)\
-   CLI usability\
-   Output to file option

------------------------------------------------------------------------

# ✨ Features

✅ Clean tree-style output\
✅ Optional file content display\
✅ Exclude files/folders/patterns\
✅ Wildcard support (`*.exe`, `.terraform*`)\
✅ Export output to file\
✅ Lightweight & Fast\
✅ Installable as CLI tool

------------------------------------------------------------------------

# 📦 Installation

### Local Install (Dev Mode)

``` bash
pip install -e .

OR

python -m pip install -e .
```

Or standard install:

``` bash
python -m pip install . 

OR

py -m pip install .
```

------------------------------------------------------------------------

# 🚀 Usage

Basic usage:

``` bash
rtftree <project-folder>
```

Example:

``` bash
rtftree .
```

------------------------------------------------------------------------

## 📁 Generate Only Structure

``` bash
rtftree . --no-content
```

------------------------------------------------------------------------

## 🚫 Exclude Files/Folders

``` bash
rtftree . --exclude .terraform .git terraform.tfstate *.exe

OR

rtftree . --exclude-file exclude.txt
```

Supports: - Exact names - Folder names - Wildcards

------------------------------------------------------------------------

## 💾 Save Output to File

``` bash
rtftree . -o infra_tree.txt
```

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

# 🧠 Real-World Terraform Exclude Example

``` bash
rtftree . --exclude .terraform terraform.tfstate terraform.tfstate.backup .terraform.lock.hcl .git *.exe
```

------------------------------------------------------------------------

# ⚙️ CLI Options

  -----------------------------------------------------------------------
  Option                       Description
  ---------------------------- ------------------------------------------
  `--no-content`               Show only structure (no file contents)

  `--exclude`                  Space-separated list of
                               files/folders/patterns to ignore

  `-o`, `--output`             Write output to a file
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🏗 Project Structure

    terraform-tree-tool/
    │
    ├── rtftree/
    │   ├── __init__.py
    │   └── cli.py
    │
    ├── pyproject.toml
    └── README.md

------------------------------------------------------------------------

# 🔥 DevOps Use Cases

-   Share Terraform structure in documentation
-   Generate infra overview for clients
-   Attach project layout in tickets
-   Create audit-ready infrastructure views
-   Documentation automation in CI/CD

------------------------------------------------------------------------

# 🚀 Future Enhancements

-   `.treeignore` support (like `.gitignore`)
-   Depth control (`--max-depth`)
-   Terraform-only mode (`*.tf` only)
-   JSON export
-   Markdown export
-   PyPI official release

------------------------------------------------------------------------

# 👨‍💻 Author

**Ritesh Sharma**\
DevOps \| Azure \| Terraform \| Kubernetes

------------------------------------------------------------------------

# 📄 License

MIT License

------------------------------------------------------------------------

# ⭐ If You Like This Tool

Give it a star ⭐ on GitHub and share it with your DevOps friends.
