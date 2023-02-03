from pynput import mouse



def on_click(x, y, button, pressed):
    if not pressed:
        return
    print(button.name)





# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
