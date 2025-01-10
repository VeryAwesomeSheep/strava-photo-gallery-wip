document.addEventListener('DOMContentLoaded', function () {
  const activityBoxes = window.activitiesData;  // Access the data passed from Flask

  activityBoxes.forEach((activity, index) => {
    if (activity.distance === 0) {
      // Skip activities with no distance (no GPS data)
      return;
    }

    const mapId = `map-${index + 1}`;
    const mapContainer = document.getElementById(mapId);

    if (mapContainer) {
      const map = L.map(mapId).setView([0, 0], 13);
      L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      try {
        const decodedPolyline = L.Polyline.fromEncoded(activity.polyline).getLatLngs();
        const polyline = L.polyline(decodedPolyline, { color: 'red', weight: 4 }).addTo(map);
        map.fitBounds(polyline.getBounds());
      } catch (error) {
        console.error(`Error decoding polyline for activity ${index + 1}:`, error);
      }
    }
  });
});
