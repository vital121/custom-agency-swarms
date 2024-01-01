# workdir.py
import os
import logging
from pathlib import Path
import platform

# Initialize logging
logging.basicConfig(level=logging.INFO)


def create_init_file(path: Path):
    """
    Creates an __init__.py file in the specified directory.
    """
    init_file = path / "__init__.py"
    init_file.touch()  # Creates the file if it doesn't exist
    logging.info(f"Created __init__.py at: {init_file}")


def create_agent_workdir_structure(base_dir: Path):
    """
    Creates the agent's working directory structure.
    """
    subdirectories = [
        "data/external",
        "data/interim",
        "data/processed",
        "data/raw",
        "notebooks",
        "reports",
        "reports/figures",
        "src",
        "src/features",
        "src/models",
        "src/visualization",
        "tests",
        "utils",
    ]

    for subdir in subdirectories:
        dir_to_create = base_dir / subdir
        dir_to_create.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created subdirectory: {dir_to_create}")

        # Create __init__.py in each subdirectory
        create_init_file(dir_to_create)

    # Create __init__.py in the root of the agent's working directory
    create_init_file(base_dir)


def init_agent_workdir(relative_path: str) -> str:
    """
    Initializes the agent's working directory.
    """
    # Determine current OS
    current_os = platform.system()

    # Construct the Path object
    if current_os == "Windows" and not relative_path.startswith("\\\\"):
        # For Windows, ensure correct format
        agent_workdir = Path.cwd() / Path(relative_path.replace("/", "\\"))
    else:
        # For Unix-like systems
        agent_workdir = Path.cwd() / relative_path

    logging.info(f"Initializing agent's working directory: {agent_workdir}")

    # Check if the directory exists, create if not
    if not agent_workdir.exists():
        logging.info(
            "Agent's working directory not found. Creating directory structure."
        )
        create_agent_workdir_structure(agent_workdir)
    else:
        logging.info("Agent's working directory already exists.")

    return str(agent_workdir.resolve())


# Example usage
if __name__ == "__main__":
    workdir = init_agent_workdir("agent_workdir")
    print(f"Agent Working Directory Initialized: {workdir}")