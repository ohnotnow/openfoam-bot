# OpenFOAM Bot

OpenFOAM Bot is a Python-based tool designed to streamline the creation of OpenFOAM simulation configuration files with the help of large language models (LLMs). The tool guides users through the process by interpreting project requirements, generating structured specifications, and producing the necessary OpenFOAM file structure. This accelerates simulation setup, especially for users with complex or unique simulation requirements.

---

## Features
- **Interactive Workflow**: Engage in an interactive Q&A process to clarify ambiguous or missing simulation parameters.
- **Automated File Generation**: Automatically produce a minimal but valid OpenFOAM directory structure, including `system`, `constant`, and `0` directories.
- **Solver Recommendations**: Leverage AI to recommend solvers, boundary conditions, and numerical schemes tailored to the user's project.

---

## Installation

### Prerequisites
- **Python 3.11+** installed on your system.
- Basic familiarity with OpenFOAM.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ohnotnow/openfoam-bot.git
   cd openfoam-bot
   ```

2. Install dependencies using `uv` (recommended):
   ```bash
   uv sync
   ```
   > Note: Learn more about `uv` [here](https://docs.astral.sh/uv/).

---

## Usage

Run the main script to start generating OpenFOAM simulation files:

```bash
uv run main.py
```

### Workflow
1. **Input your project description** (optional):
   The tool will prompt you to describe the overall context of your simulation.
2. **Specify simulation requirements**:
   Provide details about the desired OpenFOAM simulation.
3. **Answer clarifying questions**:
   If the tool identifies ambiguous or missing information, it will prompt you for clarification.
4. **Receive generated files**:
   The tool will output a complete set of OpenFOAM configuration files in an XML-like format. Copy these into the appropriate directories for your simulation.

---

## File Structure Overview
The tool generates the following OpenFOAM file structure:

```
project_folder/
|-- system/
|   |-- controlDict
|   |-- fvSchemes
|   |-- fvSolution
|
|-- constant/
|   |-- turbulenceProperties
|   |-- thermophysicalProperties
|   |-- transportProperties
|
|-- 0/
    |-- U
    |-- p
    |-- T (if applicable)
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

---

## Contact
For questions or feedback, please reach out through the [GitHub repository](https://github.com/ohnotnow/openfoam-bot/issues).
