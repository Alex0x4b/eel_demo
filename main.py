import eel


# Give folder containing web files
eel.init('web')


# Expose this function to Javascript
@eel.expose
def add_values(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "input type error"


# Start
eel.start('index.html', size=(500, 200), mode='my_portable_chromium')
