import subprocess

def is_command_output_contains_text(command, text):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.returncode == 0 and text in result.stdout
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

command = "git add"  # Команда
text = "cmonnigga"  # Текст

result = is_command_output_contains_text(command, text)
print(result)
