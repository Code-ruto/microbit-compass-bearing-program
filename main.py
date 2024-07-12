bearing = 0

def on_forever():
    global bearing
    bearing = input.compass_heading()
    if bearing >= 0 and bearing < 45:
        basic.show_arrow(ArrowNames.NORTH)
    elif bearing >= 45 and bearing < 90:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif bearing >= 90 and bearing < 135:
        basic.show_arrow(ArrowNames.EAST)
    elif bearing >= 135 and bearing < 180:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif bearing >= 180 and bearing < 225:
        basic.show_arrow(ArrowNames.SOUTH)
    elif bearing >= 225 and bearing < 270:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif bearing >= 270 and bearing < 315:
        basic.show_arrow(ArrowNames.WEST)
    elif bearing >= 315:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        pass
basic.forever(on_forever)
