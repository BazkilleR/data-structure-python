"""Labs 08.03 - Set Covering"""
import json

def main(cities, num_stations):
    """Optimized Set Covering Algorithm"""
    stations = [json.loads(input()) for _ in range(num_stations)]  # Read stations

    uncovered_cities = set(cities)  # Track cities that still need coverage
    selected_stations = []

    while uncovered_cities:
        # Find the best station (the one covering the most uncovered cities)
        best_station = None
        best_coverage = set()

        for station in stations:
            coverage = set(station["Cities"]) & uncovered_cities
            if len(coverage) > len(best_coverage):
                best_station = station
                best_coverage = coverage

        if not best_station:
            break  # No more stations can contribute

        # Select the best station and update uncovered cities
        selected_stations.append(best_station["Name"])
        uncovered_cities -= best_coverage  # Remove covered cities from the set

    selected_stations.sort()  # Sort the station names alphabetically
    print(selected_stations)

# Read input
main(json.loads(input()), int(input()))
