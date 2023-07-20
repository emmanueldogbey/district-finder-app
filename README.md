This is a small web app that returns the district for any user-supplied location.

The app uses Geopy's geocoding module through the Nominatim service to return coordinates for defined locations.

An admin boundaries file is derived from OSM Boundaries, and this is used to return a district name after a simple feature intersect is completed.

The primary limitation of this app is that the Nominatim service may not return point coordinates for each user supplied location. It is very likely only more common locations will get district names returned.
