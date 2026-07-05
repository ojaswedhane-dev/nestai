import "../styles/Recommendation.css";

export default function Recommendation() {
    return (
        <section className="recommendation-card">

            <div className="recommendation-title">
                🏆 Final Recommendation
            </div>

            <h2>Whitefield</h2>

            <p>
                Whitefield provides the strongest overall balance between
                affordability, education, healthcare accessibility, and commute
                convenience for the selected preferences.
            </p>

            <ul>

                <li>Excellent education ecosystem</li>

                <li>Strong healthcare availability</li>

                <li>Competitive rental prices</li>

                <li>Well connected by metro and road</li>

                <li>High overall LifeScore</li>

            </ul>

        </section>
    );
}