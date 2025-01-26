import streamlit as st
import subprocess

def check_command_installed(command):
    try:
        # Run the command to check if it's installed
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode("utf-8").strip()  # Return the version information
        else:
            return None
    except FileNotFoundError:
        return None

# Streamlit UI
st.title("Command Installation Checker")

st.write("Check whether GitHub-related tools are installed in this environment.")

# Check for Git
git_version = check_command_installed("git")
if git_version:
    st.success(f"✅ Git is installed: {git_version}")
else:
    st.error("❌ Git is not installed.")

# Check for GitHub CLI (gh)
gh_version = check_command_installed("gh")
if gh_version:
    st.success(f"✅ GitHub CLI is installed: {gh_version}")
else:
    st.error("❌ GitHub CLI is not installed.")
