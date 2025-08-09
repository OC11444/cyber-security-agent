#!/bin/bash
set -e

REPO_DIR=$(pwd)
GITIGNORE=".gitignore"

# Step 1: Create/update .gitignore with basic large files to ignore
echo "Updating $GITIGNORE..."
cat > $GITIGNORE <<EOF
# Virtual environments
venv/
.venv/

# Large model files
vosk-model-small-en-us-0.15/

# Python cache
__pycache__/
*.py[cod]

# Logs
logs/
*.log
output.log

# Workspace config
workspace.code-workspace

# IDE config files
.vscode/
.idea/
EOF

echo ".gitignore updated."

# Step 2: Find large files >10MB not ignored yet, add them to .gitignore
echo "Scanning for large files >10MB..."
LARGE_FILES=$(find . -type f -size +10M ! -path "./venv/*" ! -path "./.venv/*" ! -path "./vosk-model-small-en-us-0.15/*" | sed 's|^\./||')

if [ -n "$LARGE_FILES" ]; then
    echo "Adding the following large files/folders to .gitignore:"
    echo "$LARGE_FILES"
    for file in $LARGE_FILES; do
        dir=$(dirname "$file")
        # Add directory to gitignore if not already present
        if ! grep -qx "$dir/" $GITIGNORE; then
            echo "$dir/" >> $GITIGNORE
            echo "Added $dir/ to $GITIGNORE"
        fi
    done
else
    echo "No additional large files found."
fi

# Step 3: Clean git cache to apply new .gitignore
echo "Checking if this is initial commit..."
if git rev-parse --verify HEAD >/dev/null 2>&1; then
    echo "Not initial commit, removing ignored files from git index..."
    if [ -n "$(git ls-files)" ]; then
        git rm -r --cached .
    else
        echo "No tracked files to remove from index."
    fi
else
    echo "Initial commit detected, skipping git rm."
fi

echo "Adding files to git..."
git add .

# Commit only if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
else
    if git rev-parse --verify HEAD >/dev/null 2>&1; then
        git commit -m "Automated commit: Add/update project files excluding large files"
    else
        git commit -m "Initial commit - automated commit excluding large files"
    fi
fi

# Step 4: Push with retry on failure due to large files or LFS
push_repo() {
    git push origin main
}

attempt=1
max_attempts=3

while ! push_repo; do
    echo "Push failed. Checking for large files tracked in git..."

    # Find files tracked by git that are >10MB (could cause push failure)
    LARGE_TRACKED=$(git ls-files -z | xargs -0 du -h 2>/dev/null | sort -hr | head -10 | awk '{print $2}')

    if [ -z "$LARGE_TRACKED" ]; then
        echo "No large tracked files found. Exiting with error."
        exit 1
    fi

    echo "Large tracked files found:"
    echo "$LARGE_TRACKED"

    # Add their folders to .gitignore and clean history
    for file in $LARGE_TRACKED; do
        dir=$(dirname "$file")
        if ! grep -qx "$dir/" $GITIGNORE; then
            echo "$dir/" >> $GITIGNORE
            echo "Added $dir/ to $GITIGNORE"
        fi
    done

    echo "Cleaning git cache and history of ignored files..."

    if [ -n "$(git ls-files)" ]; then
        git rm -r --cached .
    else
        echo "No tracked files to remove from index."
    fi
    git add .

    # Commit changes after removing large files
    if git diff-index --quiet HEAD --; then
        echo "No changes to commit after cleanup."
    else
        git commit -m "Remove large files from repo"
    fi

    # Clean git history of large files (optional, requires BFG or filter-repo)
    echo "Cleaning git history with BFG Repo-Cleaner..."
    if command -v bfg >/dev/null 2>&1; then
        # Build a comma-separated list of folders from .gitignore
        FOLDERS_TO_CLEAN=$(grep '/$' $GITIGNORE | tr '\n' ',' | sed 's/,$//')
        if [ -n "$FOLDERS_TO_CLEAN" ]; then
            bfg --delete-folders "$FOLDERS_TO_CLEAN" .
            git reflog expire --expire=now --all
            git gc --prune=now --aggressive
        else
            echo "No folders found in .gitignore to clean with BFG."
        fi
    else
        echo "BFG Repo-Cleaner not found. Skipping history cleaning."
    fi

    attempt=$((attempt + 1))
    if [ "$attempt" -gt "$max_attempts" ]; then
        echo "Maximum push attempts reached. Exiting."
        exit 1
    fi

    echo "Retrying push (attempt $attempt)..."
done

echo "Push succeeded!"

# Step 5: Final info message
echo "Repo is clean and pushed without large files. Workflow complete."
