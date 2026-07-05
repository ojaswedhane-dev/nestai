import "../styles/NeighborhoodCard.css";

export default function NeighborhoodCard({
    name,
    lifescore,
    housing,
    education,
    healthcare,
    commute,
    affordability,
    summary,
    recommended = false,
}) {
    return (
        <div className={`neighborhood-card ${recommended ? "recommended" : ""}`}>

            <div className="card-header">

                <div>
                    <h2>{name}</h2>

                    <p>{summary}</p>
                </div>

                <div className="lifescore-circle">

                    <span>{lifescore}</span>

                    <small>LifeScore</small>

                </div>

            </div>

            <div className="score-grid">

                <div className="score-box">
                    <h4>🏡 Housing</h4>
                    <span>{housing}</span>
                </div>

                <div className="score-box">
                    <h4>🏫 Education</h4>
                    <span>{education}</span>
                </div>

                <div className="score-box">
                    <h4>🏥 Healthcare</h4>
                    <span>{healthcare}</span>
                </div>

                <div className="score-box">
                    <h4>🚇 Commute</h4>
                    <span>{commute}</span>
                </div>

                <div className="score-box">
                    <h4>💰 Budget</h4>
                    <span>{affordability}</span>
                </div>

            </div>

            {recommended && (
                <div className="recommendation-badge">

                    ⭐ Recommended Choice

                </div>
            )}

        </div>
    );
}