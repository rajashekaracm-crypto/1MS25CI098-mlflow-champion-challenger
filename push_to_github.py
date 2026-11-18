#!/usr/bin/env python3
"""
push_to_github.py
Pushes the initialized Git repository to GitHub using dulwich.
Supports environment variable GITHUB_TOKEN or interactive input.
"""

import os
import sys
import getpass
import dulwich.porcelain as porcelain

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REMOTE = "https://github.com/rajashekaracm-crypto/1MS25CI098-mlflow-champion-challenger.git"

def main():
    print("=" * 80)
    print(" GITHUB REPOSITORY PUSH UTILITY")
    print("=" * 80)
    print(f"Target Repository: {DEFAULT_REMOTE}")
    print(f"Local Path:        {REPO_PATH}\n")

    token = os.getenv("GITHUB_TOKEN")
    if not token and len(sys.argv) > 1:
        token = sys.argv[1].strip()

    if not token:
        print("GitHub requires authentication to push.")
        print("Please enter your GitHub Personal Access Token (PAT):")
        print("(You can generate one at https://github.com/settings/tokens with 'repo' scope)")
        try:
            token = input("Enter GitHub Token: ").strip()
        except EOFError:
            print("Error: No token provided via stdin or argument.")
            print("\nUsage:")
            print("  python push_to_github.py <YOUR_GITHUB_TOKEN>")
            print("  or: set GITHUB_TOKEN=<YOUR_GITHUB_TOKEN> && python push_to_github.py")
            sys.exit(1)

    if not token:
        print("Error: Empty token entered.")
        sys.exit(1)

    # Construct authenticated URL
    clean_url = DEFAULT_REMOTE.replace("https://", "")
    auth_url = f"https://{token}@{clean_url}"

    print("\nPushing commit history to 'main' branch on GitHub...")
    try:
        porcelain.push(REPO_PATH, auth_url, refspecs=b"refs/heads/main:refs/heads/main")
        print("\n" + "=" * 80)
        print(" [SUCCESS] Repository pushed to GitHub successfully!")
        print(f" View your project at: https://github.com/rajashekaracm-crypto/1MS25CI098-mlflow-champion-challenger")
        print("=" * 80)
    except Exception as e:
        print(f"\n[Push Failed]: {e}")
        print("\nTroubleshooting tips:")
        print("1. Ensure your GitHub Personal Access Token has the 'repo' scope enabled.")
        print("2. Verify that the repository 'rajashekaracm-crypto/1MS25CI098-mlflow-champion-challenger' exists on GitHub.")
        print("3. If using standard Git CLI, run: git push -u origin main")

if __name__ == "__main__":
    main()
