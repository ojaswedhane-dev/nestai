import "../styles/Checklist.css";

export default function Checklist() {
    return (

        <section className="checklist-card">

            <h2>✅ Relocation Checklist</h2>

            <div className="checklist-columns">

                <div>

                    <h3>Before Moving</h3>

                    <ul>

                        <li>Finalize accommodation</li>

                        <li>Arrange transportation</li>

                        <li>Transfer utilities</li>

                        <li>Update address</li>

                        <li>Prepare documents</li>

                    </ul>

                </div>

                <div>

                    <h3>After Moving</h3>

                    <ul>

                        <li>Visit nearby hospitals</li>

                        <li>Explore schools</li>

                        <li>Locate grocery stores</li>

                        <li>Register local services</li>

                        <li>Meet the neighborhood</li>

                    </ul>

                </div>

            </div>

        </section>

    );
}