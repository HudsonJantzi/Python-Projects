import os
import keyboard

recording = True
sd_card_path = 'D://'  # Replace this with the correct path 

def write_input_to_file(event):
    global recording

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            recording = False
        elif event.name == 'enter':
            with open(os.path.join(sd_card_path, "keyboard_input.txt"), 'a') as file:
                file.write('\n')
        else:
            with open(os.path.join(sd_card_path, "keyboard_input.txt"), 'a') as file:
                file.write(event.name)
    elif event.event_type == keyboard.KEY_UP and event.name != 'enter':
        with open(os.path.join(sd_card_path, "keyboard_input.txt"), 'a') as file:
            file.write(' ')

if __name__ == "__main__":
    print("Press ESC + ENTER to stop recording and save.")
    keyboard.on_press(write_input_to_file)

    # Check for both Esc and Enter key presses to stop recording
    while recording:
        if keyboard.is_pressed('esc') and keyboard.is_pressed('enter'):
            recording = False

    keyboard.unhook_all()
    print("Recording stopped. Keyboard input saved to", os.path.join(sd_card_path, "keyboard_input.txt"))
