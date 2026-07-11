import { FileText } from "lucide-react";

function ResumeQuality({ analysis }) {
    if (!analysis) return null;

    const quality = analysis.resume_quality || {};

    return (
        <div className="quality-card">
            <h2 className="card-title">
                <FileText size={28} />
                Resume Quality
            </h2>

            <div className="quality-grid">
                <div className="quality-box">
                    <h3>Quality Score</h3>
                    <div className="quality-score">
                        {quality.quality_score}/10
                    </div>
                </div>

                <div className="quality-box">
                    <h3>Formatting</h3>
                    <p>{quality.formatting || "Good"}</p>
                </div>

                <div className="quality-box">
                    <h3>Readability</h3>
                    <p>{quality.readability || "Good"}</p>
                </div>

                <div className="quality-box">
                    <h3>Achievements</h3>
                    <p>{quality.quantified_achievements ? "Present" : "Needs Improvement"}</p>
                </div>
            </div>
        </div>
    );
}

export default ResumeQuality;