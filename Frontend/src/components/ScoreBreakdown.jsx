import { PieChart } from "lucide-react";

function ScoreBreakdown({ analysis }) {
    if (!analysis) {
        return null;
    }

    const breakdown = analysis.score_breakdown || {};

    return (
        <div className="breakdown-card">
            <h2 className="card-title">
                <PieChart size={28} />
                Score Breakdown
            </h2>

            <div className="breakdown-grid">
                {Object.entries(breakdown).map(([title, score]) => (
                    <div className="breakdown-item" key={title}>
                        <h4>{title}</h4>

                        <div className="score-number">
                            {score}
                        </div>

                        <div className="mini-progress">
                            <div
                                className="mini-fill"
                                style={{
                                    width: `${(score / 45) * 100}%`,
                                }}
                            ></div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ScoreBreakdown;