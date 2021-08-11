def coordinatesToDecimal(degreeslat, degreeslong, minuteslat, minuteslong):
    # Equation for the conversion
    minutesconvlat = minuteslat / 60
    lat = degreeslat + minutesconvlat

    print(lat)

    minutesconvlong = minuteslong / 60
    long = degreeslong + minutesconvlong

    print(long)


def main():
    print('Insert latitude degrees: ')
    latitude_degrees = input()
    print('Insert latitude minutes: ')
    latitude_minutes = input()
    print('Insert longitude degrees: ')
    longitude_degrees = input()
    print('Insert longitude minutes: ')
    longitude_minutes = input()

    coordinatesToDecimal(latitude_degrees, longitude_degrees, latitude_minutes, longitude_minutes)


if __name__ == "__main__":
    main()
