import "../styles/AgentStatus.css";

const agents = [
    {
        name: "Housing Agent",
        description: "Analyzing housing options",
        status: "Completed",
    },
    {
        name: "School Agent",
        description: "Evaluating nearby schools",
        status: "Completed",
    },
    {
        name: "Healthcare Agent",
        description: "Checking hospitals & clinics",
        status: "Completed",
    },
    {
        name: "Commute Agent",
        description: "Calculating commute routes",
        status: "Completed",
    },
    {
        name: "Budget Agent",
        description: "Estimating monthly expenses",
        status: "Completed",
    },
];

export default function AgentStatus() {
    return (
        <section className="agent-card">
            <h2>🤖 Agent Execution</h2>

            <div className="agent-list">
                {agents.map((agent) => (
                    <div className="agent-item" key={agent.name}>
                        <div>
                            <h3>{agent.name}</h3>
                            <p>{agent.description}</p>
                        </div>

                        <span className="status completed">
                            {agent.status}
                        </span>
                    </div>
                ))}
            </div>
        </section>
    );
}