import "./App.css";

import Header from "./components/Header";
import PreferencesCard from "./components/PreferencesCard";
import AgentStatus from "./components/AgentStatus";
import NeighborhoodCard from "./components/NeighborhoodCard";
import Recommendation from "./components/Recommendation";
import Checklist from "./components/Checklist";

const neighborhoods = [
  {
    name: "Whitefield",
    lifescore: 92,
    housing: 88,
    education: 95,
    healthcare: 90,
    commute: 84,
    affordability: 87,
    summary:
      "Excellent balance of affordability, schools, healthcare and connectivity.",
    recommended: true,
  },
  {
    name: "HSR Layout",
    lifescore: 88,
    housing: 82,
    education: 90,
    healthcare: 87,
    commute: 91,
    affordability: 83,
    summary:
      "Well-connected neighbourhood with strong education and lifestyle amenities.",
    recommended: false,
  },
];

export default function App() {
  return (
    <main className="app-container fade-in">

      <Header />

      <section className="dashboard-row">

        <PreferencesCard />

        <AgentStatus />

      </section>

      <section className="neighborhood-section">

        <h2 className="section-title">
          🏘 Candidate Neighborhoods
        </h2>

        <div className="neighborhood-grid">

          {neighborhoods.map((neighborhood) => (
            <NeighborhoodCard
              key={neighborhood.name}
              {...neighborhood}
            />
          ))}

        </div>

      </section>

      <section className="bottom-grid">

        <Recommendation />

        <Checklist />

      </section>

    </main>
  );
}