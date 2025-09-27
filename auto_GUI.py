import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.FAILSAFE = True

dir = r"C:\Users\Goblin\OneDrive\Pictures\Screenshots\ALMANAC\\"

#─── User inputs ──────────────────────────────────────────────────────────
model = input("Model/scenario name (e.g. gfdl or arise_01): ").strip()
# file_path = input("Full path to weather file: ").strip()

co2_file = r"C:\Users\Goblin\OneDrive\Desktop\ALMANAC-Inputs\co2_ssp245_annual_2015_2100.txt"
df = pd.read_csv(co2_file, sep=' ', header=None, names=["year", "co2"])
df = df[(df["year"] >= 2040) & (df["year"] <= 2059)]
df["co2"] = df["co2"].round().astype(int)

# confirm co2 values
print(df.to_string(index=False))
proceed = input("\nContinue? (y/n): ").strip().lower()
if proceed != 'y':
    exit()

scenarios = [
    {"year": int(row.year), "co2": int(row.co2), "exp_name": f"{model}_{int(row.year)}"}
    for row in df.itertuples(index=False)
]

#───────────────────────────────────────────────────────────────────────────

def wait(sec=0.7):
    time.sleep(sec)

def wait_and_click(image_path, confidence=0.9, timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        time.sleep(0.5)
    raise Exception(f"Image not found after {timeout}s: {image_path}")


def click_near_image(image_path, dx=0, dy=0, confidence=0.9, timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        loc = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if loc:
            pyautogui.click(loc[0] + dx, loc[1] + dy)
            return True
        time.sleep(0.5)
    print(f"Image not found: {image_path}")
    return False


def load_weather(path):
    # step 1,2
    wait_and_click(dir+"ALMANAC_inputs.png"); wait()
    wait_and_click(dir+"Define_weather.png"); wait()
    # for label in ["precip", "temp", "humidity", "wind", "solar"]:
    #     wait_and_click(*clicks[label])
    #     wait()

    # # send full path
    # wait_and_click(*clicks["file"]); wait()
    # pyautogui.write(path, interval=0.02); wait()
    # wait_and_click(*clicks["load weather"]); wait()      # Load
    # wait_and_click(*clicks["ok"]); wait()      # OK
    # wait_and_click(*clicks["exit_weather"]); wait()       # Close

def open_scenario():
    wait_and_click(dir+"ALMANAC_inputs.png"); wait()
    wait_and_click(dir+"edit_inputs_v2.png"); wait()
    wait_and_click(dir+"scenario_def.png"); wait(2)

def make_scenario(year, co2, exp_name):
    wait_and_click(dir+"add_new_scen.png"); wait()
    pyautogui.write(exp_name, interval=0.02)
    pyautogui.press('enter'); wait()
    click_near_image(dir+"NBYR.png", dx=100)  # adjust dx as needed
    pyautogui.hotkey("ctrl", "a")  # select all
    pyautogui.press("backspace")   # delete selection
    pyautogui.write('15', interval=0.02)
    click_near_image(dir+"IYR.png", dx=100)  # adjust dx as needed
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(str(year), interval=0.02)
    pyautogui.press("tab"); wait()
    pyautogui.press("enter"); wait() # close warning popup
    click_near_image(dir+"CO2.png", dx=100)  # adjust dx as needed
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(str(co2), interval=0.02)
    wait_and_click(dir+"save_edits.png"); wait()     # Save

def run_scenarios_via_keyboard(scenarios, model_prefix, max_rows=300):
    target_names = {s["exp_name"] for s in scenarios}
    found = set()

    print(f"Looking for {len(target_names)} scenarios matching '{model_prefix}'...")
    
    pyautogui.press("right"); wait(0.1)     # move columns
    
    for i in range(max_rows):
        pyautogui.hotkey("ctrl", "c")
        run_name = pyperclip.paste().strip()

        if run_name.startswith(model_prefix) and run_name in target_names and run_name not in found:
            print(f"> Found and running: {run_name}")

            wait_and_click(dir+"update_input_files.png")
            pyautogui.press("enter"); wait()    # close popup
            wait_and_click(dir+"run_almanac.png")
            time.sleep(4)  # wait for popup to appear
            wait_and_click(dir+"ok.png")
            found.add(run_name)

            if len(found) == len(target_names):
                print("All matching scenarios completed.")
                break
            wait_and_click(dir+"scrollbar.png") # click back to popup scroll area
        
        pyautogui.press("down"); wait(0.1)

    if len(found) < len(target_names):
        print(f"Only found {len(found)} out of {len(target_names)} scenarios.")


def main():
    # Create scenarios
    # open_scenario()

    for s in scenarios:
        make_scenario(**s)
    
    wait_and_click(dir+"exit.png"); wait()     # Exit

    # Run scenarios
    if input("\nRun scenarios now? (y/n): ").strip().lower() == 'y':
        print("Please **open** the **run scenarios window** in ALMANAC.")
        print("You have 5 sec to focus the target app...")
        time.sleep(5)
        run_scenarios_via_keyboard(scenarios, model)
    
    # wait_and_click(dir+"exit.png"); wait()     # Exit

    print("Done.")

if __name__ == "__main__":
    print("You have 5 sec to focus the target app...")
    time.sleep(5)
    main()
