import pyautogui
import time

print("You'll enter a label, then move your mouse to the position and press Enter.")
print("Press Ctrl+C when done.\n")

positions = []

try:
    while True:
        label = input("Label for this position: ").strip()
        input("Move mouse to position and press Enter...")
        x, y = pyautogui.position()
        positions.append((label, x, y))
        print(f"Recorded: {label} = ({x}, {y})")
except KeyboardInterrupt:
    print("\nRecording finished.")

with open("labeled_clicks.txt", "w") as f:
    for label, x, y in positions:
        f.write(f"{label},{x},{y}\n")

print("\nLabeled positions saved to labeled_clicks.txt.")
