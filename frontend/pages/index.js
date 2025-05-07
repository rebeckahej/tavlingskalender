// pages/index.js
import { useEffect, useState } from "react";

const HomePage = () => {
  const [lopp, setLopp] = useState([]); // Ingen typdeklaration här, bara en array

  useEffect(() => {
    // Här kan du anropa ditt API för att hämta tävlingar
    fetch('/api/lopp') // Eller din URL för att hämta tävlingar
      .then((response) => response.json())
      .then((data) => setLopp(data));
  }, []);

  return (
    <div>
      <h1>Tävlingar</h1>
      <ul>
        {lopp.map((loppItem, index) => (
          <li key={index}>
            {loppItem.namn} - {loppItem.datum} - {loppItem.plats}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
