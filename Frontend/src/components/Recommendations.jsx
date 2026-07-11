import { Lightbulb } from "lucide-react";

function Recommendations({ analysis }) {
    if (!analysis) return null;

    const recommendations = analysis.recommendations || [];

    return (
        <div className="recommend-card">
            <h2 className="card-title">
                <Lightbulb size={28} />
                AI Recommendations
            </h2>

            {recommendations.length ? (
                <ul className="recommend-list">
                    {recommendations.map((item, index) => (
                        <li key={index}>
                            💡 {item}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No recommendations.</p>
            )}
        </div>
    );
}

export default Recommendations;