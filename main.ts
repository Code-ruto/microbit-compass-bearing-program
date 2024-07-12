let bearing = 0
basic.forever(function on_forever() {
    
    bearing = input.compassHeading()
    if (bearing >= 0 && bearing < 45) {
        basic.showArrow(ArrowNames.North)
    } else if (bearing >= 45 && bearing < 90) {
        basic.showArrow(ArrowNames.NorthEast)
    } else if (bearing >= 90 && bearing < 135) {
        basic.showArrow(ArrowNames.East)
    } else if (bearing >= 135 && bearing < 180) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (bearing >= 180 && bearing < 225) {
        basic.showArrow(ArrowNames.South)
    } else if (bearing >= 225 && bearing < 270) {
        basic.showArrow(ArrowNames.SouthWest)
    } else if (bearing >= 270 && bearing < 315) {
        basic.showArrow(ArrowNames.West)
    } else if (bearing >= 315) {
        basic.showArrow(ArrowNames.NorthWest)
    }
    
    return
})
