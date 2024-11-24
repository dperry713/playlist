# Define the root project directory
$rootDir = "my_api"

# Define the subdirectories to create
$subDirs = @(
    "app",
    "app/models",
    "app/routes",
    "app/services",
    "config"
)

# Define the files to create with their paths
$files = @(
    "app/models/__init__.py",
    "app/models/song.py",
    "app/models/playlist.py",
    "app/routes/__init__.py",
    "app/routes/song.py",
    "app/routes/playlist.py",
    "app/services/__init__.py",
    "app/services/database.py",
    "app/__init__.py",
    "app/extensions.py",
    "config/config.py",
    "requirements.txt"
)

# Create the root directory if it does not exist
if (-not (Test-Path -Path $rootDir)) {
    New-Item -ItemType Directory -Path $rootDir -Force
}

# Create the subdirectories if they do not exist
foreach ($subDir in $subDirs) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $subDir
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force
    }
}

# Create the files if they do not exist
foreach ($file in $files) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $file
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType File -Path $fullPath -Force
    }
}

Write-Output "Project directory structure and files created successfully!"