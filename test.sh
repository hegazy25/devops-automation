#!/bin/bash

# This is a comment
echo "Hello from Bash!"

# Assign variable
APP_NAME="MyApp"
VERSION=1.0
BUILD_DIR="./build"

# Use variable
echo $APP_NAME
echo "App: $APP_NAME"


# Variables (no spaces around =)
APP_NAME="MyApp"
VERSION="1.0"
ENVIRONMENT="staging"
PORT=8080

# Use variables with $
echo "App: $APP_NAME"
echo "Version: $VERSION"
echo "Environment: $ENVIRONMENT"
echo "Port: $PORT"

# String concatenation
FULL_NAME="${APP_NAME}_v${VERSION}"
echo "Full name: $FULL_NAME"

# String length
echo "App name length: ${#APP_NAME}"

# Get current date/time
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
echo "Timestamp: $TIMESTAMP"

ENVIRONMENT=$1  # First argument from command line
VERSION=$2      # Second argument

# Check if arguments provided
if [ -z "$ENVIRONMENT" ]; then
    echo "Error: Environment argument required"
    exit 1
fi

if [ -z "$VERSION" ]; then
    echo "Error: Version argument required"
    exit 1
fi

# Check if environment is valid
if [ "$ENVIRONMENT" = "production" ]; then
    echo "⚠️ WARNING: Deploying to PRODUCTION"
    echo "This is a critical action!"
elif [ "$ENVIRONMENT" = "staging" ]; then
    echo "✅ Deploying to STAGING (safe)"
elif [ "$ENVIRONMENT" = "dev" ]; then
    echo "✅ Deploying to DEV (safe)"
else
    echo "❌ Invalid environment: $ENVIRONMENT"
    exit 1
fi

# Numeric comparison
if [ "$VERSION" -lt 1 ]; then
    echo "Version must be >= 1"
    exit 1
fi

# File checks
if [ -f "config.yaml" ]; then
    echo "✅ Config file exists"
else
    echo "❌ Config file not found"
    exit 1
fi

# Directory checks
if [ -d "./build" ]; then
    echo "✅ Build directory exists"
else
    echo "❌ Build directory not found"
    exit 1
fi

echo "All checks passed!"
