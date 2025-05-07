import { useEffect, useState } from "react";

export default function Home() {
  const [lopp, setLopp] = useState([]);

  // Hämtar data från API när komponenten laddas
  useEffect(() => {
    fetch('https://tavlingskalender.onrender.com/lopplista')  // Din Render-URL här
      .then((res) => res.json())
      .then((data) => setLopp(data))  // Uppdaterar state med datan från API
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Tävlingar</h1>
      <ul>
        {/* Rendera lopp-data från API */}
        {lopp.map((loppItem, index) => (
          <li key={index} style={{ marginBottom: '20px' }}>
            <h2>{loppItem.namn}</h2>
            <p><strong>Datum:</strong> {loppItem.datum}</p>
            <p><strong>Plats:</strong> {loppItem.plats}</p>
            <p><strong>Distans:</strong> {loppItem.distans}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

