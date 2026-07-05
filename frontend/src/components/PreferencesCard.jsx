import "../styles/PreferencesCard.css";

export default function PreferencesCard() {
    return (
        <section className="preferences-card">
            <h2>User Preferences</h2>

            <div className="preferences-grid">

                <div className="preference-item">
                    <span className="icon">📍</span>

                    <div>
                        <h4>Destination</h4>
                        <p>Bengaluru</p>
                    </div>
                </div>

                <div className="preference-item">
                    <span className="icon">💰</span>

                    <div>
                        <h4>Monthly Budget</h4>
                        <p>₹40,000</p>
                    </div>
                </div>

                <div className="preference-item">
                    <span className="icon">👨‍👩‍👧</span>

                    <div>
                        <h4>Family</h4>
                        <p>4 Members</p>
                    </div>
                </div>

                <div className="preference-item">
                    <span className="icon">🚇</span>

                    <div>
                        <h4>Maximum Commute</h4>
                        <p>40 Minutes</p>
                    </div>
                </div>

            </div>
        </section>
    );
}