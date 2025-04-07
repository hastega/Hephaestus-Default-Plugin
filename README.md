# Hephaestus Default Plugin

This repository contains the default plugin for [Hephaestus](link-to-hephaestus-repo-or-docs), a powerful command-line interface (CLI) tool built in Python. This plugin serves as a starting point and provides essential functionalities that are commonly used within the Hephaestus ecosystem.

## What is Hephaestus?

Hephaestus is a versatile CLI application designed to streamline various tasks through the use of plugins. It allows users to extend its core functionality by installing and managing custom plugins.

## What is this Plugin?

This is the **default plugin** for Hephaestus. It's designed to:

*   Provide a basic set of commands and functionalities.
*   Serve as a template for creating new Hephaestus plugins.
*   Demonstrate best practices for plugin development within the Hephaestus framework.
*   Offer core features that are useful for most users.

**Current Features:**

*   *(List the features that are implemented in the default plugin. If it's a fresh start, you can put placeholders like the ones below)*
    *   `help`: Displays help information about Hephaestus and its plugins.
    *   `version`: Shows the current version of Hephaestus and the default plugin.
    *   `list`: Lists all installed plugins.
    * `example`: An example command to show how to implement a command.

**Future Features:**

* *(List the features that you plan to implement in the future)*
    * `config`: Command to manage the configuration of the plugin.
    * `update`: Command to update the plugin.

## Getting Started with Development

This section guides you through setting up your development environment and starting to work on this plugin.

### Prerequisites

*   **Python 3.8+:** Ensure you have Python 3.8 or a later version installed.
*   **Hephaestus:** You need to have Hephaestus installed to test the plugin. You can install it using pip:
    ```bash
    pip install hephaestus
    ```
    *(Replace `hephaestus` with the actual package name if it's different)*
*   **Virtual Environment (Recommended):** It's highly recommended to use a virtual environment to isolate your project's dependencies.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

### Installation (for Development)

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    *(Replace `<repository-url>` and `<repository-directory>` with the actual values)*

2.  **Install in Editable Mode:**
    ```bash
    pip install -e .
    ```
    This installs the plugin in "editable" mode, so changes you make to the code are immediately reflected without needing to reinstall.

3. **Install Hephaestus**
    ```bash
    pip install hephaestus
    ```

### Plugin Structure

The plugin should follow this basic structure:

```shell
default-plugin-hep/
├── init.py
├── commands/ # Directory for command implementations
│   ├── init.py
│   └── example/
│       └── init.py
├── utils/ # Directory for utils implementations
│   ├── init.py
│   └── const.py
├── manifest.json # Project metadata and dependencies
├── README.md # This file
├── __init__.py # Plugin's main logic
└── ... # Other files (tests, etc.)
```

## Contributing

We welcome contributions to Hephaestus! If you're interested in helping out, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them with clear messages.
4. **Submit a pull request** to the main repository.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

HASTEGA - [HASTEGA](https://www.hastega.it/) - <connect@hastega.it>

David Rainò - [CTO](https://www.linkedin.com/in/david-rain%C3%B2-548084a1/) - <d.raino@hastega.it>

Daniel Angelozzi - [MAINTAINER](https://www.linkedin.com/in/pablo1255/) - <d.angelozzi@hastega.it>