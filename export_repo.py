import os
import shutil
from pathlib import Path

source_dir = Path(r"a:\framers hub")
staging_dir = source_dir / "export_staging"
downloads_dir = Path(r"C:\Users\ajayb\Downloads")
zip_path = downloads_dir / "UzhavarHub_Export.zip"

if staging_dir.exists():
    shutil.rmtree(staging_dir)
staging_dir.mkdir(parents=True)

# List of files and folders to include based on checklist
items_to_copy = [
    "uzhavarhub_project",             # A
    "backend/models.py",              # B
    "backend/urls.py",                # C
    "backend/views.py",               # C
    "backend/templates",              # C (templates)
    "ai_services",                    # D
    "run_all_experiments.py",         # E
    "seed_db.py",                     # E
    "generate_templates.py",          # E
    "data",                           # E
    "tests",                          # F
    "tests.py",                       # F
    ".github",                        # F
    "requirements.txt",               # G
    "REPRODUCE.md",                   # G
    "Dockerfile",                     # G
    "Procfile",                       # H
    "backend/admin.py",               # Core
    "backend/forms.py",               # Core
    "backend/services.py",            # Core
    "backend/api.py",                 # Core API
    "backend/migrations",             # DB
    "manage.py",                      # Core
    "results",                        # E
    "paper",                          # H
    "no_mock_data_audit.py",          # G
    "README.md",                      # I
    "RESEARCH_READINESS.md",
    "RESEARCH_DESIGN_PLAN.md",
    "RESEARCH_NOTES.md",
    "export_research_data.py",
    "no_mock_data_audit_result.txt",
    "test_listing.py",
    "MANUAL_TEST_STEPS.md"
]

# Generate a tree output and save it in the staging dir
tree_output = staging_dir / "project_structure.txt"
os.system(f'tree /F /A "{source_dir}" > "{tree_output}"')

for item in items_to_copy:
    src_path = source_dir / item
    if src_path.exists():
        dst_path = staging_dir / item
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        if src_path.is_dir():
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dst_path)

# Zip the staging dir
shutil.make_archive(str(downloads_dir / "UzhavarHub_Export"), 'zip', staging_dir)

# Clean up staging dir
shutil.rmtree(staging_dir)

print(f"Export successful! Saved to {zip_path}")
