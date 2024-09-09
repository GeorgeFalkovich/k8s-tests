#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Error: No commit message provided."
  echo "Usage: $0 <commit-message>"
  exit 1
fi

# Store the commit message
COMMIT_MESSAGE=$1

# Add all changes to the staging area
git add .

# Commit the changes with the provided message
git commit -m "$COMMIT_MESSAGE"

# Push the changes to the remote repository
git push

# Print a success message
echo "Changes have been successfully pushed to the remote repository."