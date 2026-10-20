import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_dir_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_dir_path, file_path))
        valid_file_path = (
            os.path.commonpath([abs_dir_path, target_file_path]) == abs_dir_path
        )
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        wiw = subprocess.run(
            command, cwd=abs_dir_path, capture_output=True, text=True, timeout=30
        )
        output = ""
        if wiw.returncode != 0:
            output += f"Process exited with code {wiw.returncode}\n"
        if not wiw.stdout and not wiw.stderr:
            output += "No output produced"
        if wiw.stdout:
            output += f"STDOUT: {wiw.stdout}"
        if wiw.stderr:
            output += f"STDERR: {wiw.stderr}"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
