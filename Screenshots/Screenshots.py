from pathlib import Path
import pyscreenshot
from datetime import datetime

# Get the folder where this Python file is located
project_folder = Path(__file__).parent

# Create Screenshots folder
screenshots_folder = project_folder / "Screenshots"
screenshots_folder.mkdir(exist_ok=True)

# Capture screen
image = pyscreenshot.grab()

# Create automatic filename
filename = datetime.now().strftime(
    "screenshot_%Y-%m-%d_%H-%M-%S.png"
)

# Complete path
filepath = screenshots_folder / filename

# Save screenshot
image.save(filepath)

print(f"Screenshot saved to: {filepath}")