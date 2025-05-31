import os
import sys
import subprocess

PYPI_USERNAME = "pypi_admin"
PYPI_PASSWORD = "SuperSecretPyPiPassword123!"

AWS_ACCESS_KEY = "AKIAXYZ1234567890abcdefghijklmno"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def install_requirements():
    print("Installing required Python modules...")
    reqs = [
        "flask",
        "boto3"
    ]
    for req in reqs:
        subprocess.check_call([sys.executable, "-m", "pip", "install", req])

def configure_aws_env():
    print("Configuring AWS credentials as environment variables...")
    os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY
    os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_KEY

def upload_to_pypi():
    print(f"Uploading package to PyPI as {PYPI_USERNAME} (this is insecure!)")
    # subprocess.run([
    #     "twine", "upload", "--username", PYPI_USERNAME, "--password", PYPI_PASSWORD, "dist/*"
    # ])

def main():
    install_requirements()
    configure_aws_env()
    upload_to_pypi()
    print("Setup complete.")

if __name__ == "__main__":
    main()