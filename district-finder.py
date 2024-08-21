import folium
import geopandas as gpd
from geopy.geocoders import Nominatim
from shapely.geometry import Point


def main():
    location = input("Enter a location: ").strip()
    d_boundaries = get_district_boundaries_file()
    latitude, longitude = get_coordinates(location)

    if latitude and longitude:
        display_map(latitude, longitude, d_boundaries)
    else:
        print("Location not found.")

# Geocode address to generate longitude and latitude
def get_coordinates(location):
    geolocator = Nominatim(user_agent="map_app")
    location_data = geolocator.geocode(location)
    if location_data:
        latitude = location_data.latitude
        longitude = location_data.longitude
        return latitude, longitude
    else:
        return None, None
    
def get_district_boundaries_file():
    
    d_boundaries = gpd.read_file("gh_admin_boundaries.geojson") 

    return d_boundaries[d_boundaries["admin_level"] == 6]

# Interactive mapping and visualization with folium. 
# Currently saves html file until I figure out interactive display
def display_map(latitude, longitude, d_boundaries):
    style_function = lambda x: {"color": "#000",
                                "opacity": 0.7,
                                "fillColor": "#000"}

    m = folium.Map(location=[latitude, longitude], zoom_start=7)
    folium.GeoJson(d_boundaries, name="District Boundaries", style_function=style_function).add_to(m)
    folium.LayerControl().add_to(m)
    m.save('map.html')  # Save the map to an HTML file
    print("Map created and saved as 'map.html'. Please open the HTML file to view the map.")

if __name__ == '__main__':
    main()

