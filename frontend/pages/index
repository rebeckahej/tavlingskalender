import { useEffect, useState } from "react";

type Lopp = {
  namn: string;
  datum: string;
  plats: string;
  distans: string;
  url: string;
};

export default function Home() {
  const [loppen, setLoppen] = useState<Lopp[]>([]);
  const [filter, setFilter] = useState({ lan: "", distans: "" });

  useEffect(() => {
    const fetchData = async () => {
      const params = new URLSearchParams();
      if (filter.lan) params.append("lan", filter.lan);
      if (filter.distans) params.append("distans", filter.distans);
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}?${params.toString()}`);
      const data = await res.json();
      setLoppen(data);
    };
    fetchData();
  }, [filter]);

  return (
    <main className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Tävlingskalender</h1>

      <div className="flex gap-4 mb-6">
        <input
          placeholder="Filtrera på län"
          className="border px-3 py-2 rounded w-1/2"
          onChange={(e) => setFilter(f => ({ ...f, lan: e.target.value }))}
        />
        <input
          placeholder="Filtrera på distans"
          className="border px-3 py-2 rounded w-1/2"
          onChange={(e) => setFilter(f => ({ ...f, distans: e.target.value }))}
        />
      </div>

      <ul className="space-y-4">
        {loppen.map((lopp, i) => (
          <li key={i} className="border rounded p-4 shadow">
            <h2 className="text-xl font-semibold">{lopp.namn}</h2>
            <p>{lopp.datum} – {lopp.plats} – {lopp.distans}</p>
            <a href={lopp.url} target="_blank" className="text-blue-600 underline">Länk</a>
          </li>
        ))}
      </ul>
    </main>
  );
}
