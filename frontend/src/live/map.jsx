import React, { useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';
import 'leaflet-geosearch/dist/geosearch.css';

const Map = () => {
  useEffect(() => {
    // Check if map already exists and remove it
    const existingMap = L.DomUtil.get('map');
    if (existingMap != null) {
      existingMap._leaflet_id = null;
    }

    const map = L.map('map',{draggable: true,}).setView([28.6139, 77.2090], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', ).addTo(map);

    const provider = new OpenStreetMapProvider();

    const searchControl = new GeoSearchControl({
      provider: provider,
      style: 'bar',
      showMarker: true,
      showPopup: true,
      autoClose: true,
    });

    map.addControl(searchControl);
  }, []);

  return (
    <div id="map" style={{ height: '90vh', width: '100vw' }} />
  );
};

export default Map;