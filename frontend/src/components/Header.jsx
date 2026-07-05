import { useEffect, useState } from "react";
import "../styles/Header.css";

export default function Header() {
    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {
        if (darkMode) {
            document.documentElement.setAttribute("data-theme", "dark");
        } else {
            document.documentElement.removeAttribute("data-theme");
        }
    }, [darkMode]);

    return (
        <header className="header">
            <div className="header-top">
                <div className="header-left">
                    <h1>🏡 NestAI</h1>
                    <p>Move with Confidence</p>
                </div>

                <div className="header-right">
                    <button
                        className="theme-toggle"
                        onClick={() => setDarkMode(!darkMode)}
                    >
                        {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
                    </button>
                </div>
            </div>

            <div className="system-status">
                <span>🟢 Backend Connected</span>
                <span>🤖 5 Specialist Agents</span>
                <span>🌐 Browser MCP</span>
                <span>🗺️ Google Maps MCP</span>
            </div>
        </header>
    );
}