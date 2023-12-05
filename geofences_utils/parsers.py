from shapely.wkt import loads


# Function to format coordinates as 'lat,lng'
def format_coordinates(coords):
    return ";".join([f"{lat},{lng}" for lng, lat in coords])


def parse_wkt_to_csv(wkt: str) -> (str, int):
    """Parse WKT to CSV

    Args:
        wkt (str): WKT

    Returns:
        str: CSV -> 'lat,lng;lat,lng'
    """
    formatted_string = ""
    number_of_coordinates = 0

    # Parse the WKT string into a Shapely geometry object
    geometry = loads(wkt)

    # Extract coordinates and format as 'lat,lng'
    if geometry.geom_type == "Point":
        formatted_string = format_coordinates([(geometry.y, geometry.x)])
        number_of_coordinates = 1

    elif geometry.geom_type == "LineString":
        coordinates = list(geometry.coords)
        formatted_string = format_coordinates(coordinates)
        number_of_coordinates = len(coordinates)

    elif geometry.geom_type == "Polygon":
        coordinates = list(geometry.exterior.coords)
        formatted_string = format_coordinates(coordinates)
        number_of_coordinates = len(coordinates)

    elif geometry.geom_type == "GeometryCollection":
        formatted_string = ""
        number_of_coordinates = 0
        for geom in geometry.geoms:
            if formatted_string:
                formatted_string += ";"
                number_of_coordinates += 1

            if geom.geom_type == "Point":
                formatted_string += format_coordinates([(geom.y, geom.x)])
            elif geom.geom_type == "LineString":
                formatted_string += format_coordinates(list(geom.coords))
            elif geom.geom_type == "Polygon":
                formatted_string += format_coordinates(list(geom.exterior.coords))
            # Handle other geometry types as needed

    else:
        formatted_string = None  # Handle other geometry types if needed
        number_of_coordinates = 0

    return formatted_string, number_of_coordinates
