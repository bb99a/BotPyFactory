# Development Guidelines

## Working with Virtual Environments

- **Activating the Virtual Environment**: Always activate your virtual environment before working on your project. This ensures that any Python packages you install or run are confined to this environment.

- **Installing Dependencies**: After activating your virtual environment, use `pip install` to install any packages you need for your project. It’s a good practice to keep a `requirements.txt` file with all the necessary package names and versions.

- **Deactivating the Virtual Environment**: Once you're done working in the virtual environment, you can deactivate it by simply typing `deactivate` in the command prompt.

## Managing Dependencies

- To generate a `requirements.txt` file that lists all your project’s dependencies, you can use `pip freeze > requirements.txt` while your virtual environment is activated. This is useful for reproducing the environment on other machines or by other developers working on the same project.

- When setting up the project on a new machine, or if someone else is working on the project, install all dependencies by running `pip install -r requirements.txt` after activating the virtual environment.

## Version Control

- Don’t forget to add your `env` directory to `.gitignore` before pushing your code to a version control system like Git. This prevents your entire virtual environment from being uploaded, which can contain platform-specific binaries that are not suitable for version control.

- Instead, share the `requirements.txt` file, which allows others to recreate the virtual environment with the same dependencies.
