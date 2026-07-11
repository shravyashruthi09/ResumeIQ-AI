import { BarChart3 } from "lucide-react";

function CategoryScores({ analysis }) {
    if (!analysis) {
        return null;
    }

    const categories = analysis.category_scores || {};

    return (
        <div className="category-card">
            <h2 className="card-title">
                <BarChart3 size={28} />
                Category Scores
            </h2>

            <div className="category-list">
                {Object.entries(categories).map(([category, score]) => (
                    <div className="category-item" key={category}>
                        <div className="category-header">
                            <span>{category}</span>
                            <strong>{score}%</strong>
                        </div>

                        <div className="progress-bar">
                            <div
                                className="progress-fill"
                                style={{ width: `${score}%` }}
                            ></div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default CategoryScores;