def allocate_green_time(vehicle_count):
    if vehicle_count >= 40:
        return 60
    elif vehicle_count >= 30:
        return 50
    elif vehicle_count >= 20:
        return 40
    elif vehicle_count >= 10:
        return 30
    else:
        return 20
