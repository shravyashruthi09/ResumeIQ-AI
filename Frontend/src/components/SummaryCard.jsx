import {
    User,
    Star,
    CheckCircle,
    AlertTriangle,
    Target,
} from "lucide-react";

function SummaryCard({ analysis }) {
    const summary = analysis?.resume_summary;

    if (!summary) {
        return null;
    }

    return (
        <div className="summary-card">
            <h2 className="card-title">Resume Summary</h2>

            <div className="summary-grid">
                <div className="summary-item">
                    <User size={22} />

                    <div>
                        <span>Candidate Type</span>
                        <strong>{summary.candidate_type}</strong>
                    </div>
                </div>

                <div className="summary-item">
                    <Star size={22} />

                    <div>
                        <span>Overall Rating</span>
                        <strong>{summary.overall_rating}</strong>
                    </div>
                </div>

                <div className="summary-item">
                    <Target size={22} />

                    <div>
                        <span>Strongest Area</span>
                        <strong>{summary.strongest_area}</strong>
                    </div>
                </div>

                <div className="summary-item">
                    <AlertTriangle size={22} />

                    <div>
                        <span>Weakest Area</span>
                        <strong>{summary.weakest_area}</strong>
                    </div>
                </div>

                <div className="summary-item">
                    <AlertTriangle size={22} />

                    <div>
                        <span>Top Missing Skill</span>
                        <strong>{summary.top_missing_skill}</strong>
                    </div>
                </div>

                <div className="summary-item">
                    <CheckCircle
                        size={22}
                        color={summary.ready_for_application ? "#16a34a" : "#dc2626"}
                    />

                    <div>
                        <span>Application Ready</span>

                        <strong>
                            {summary.ready_for_application ? "Yes" : "No"}
                        </strong>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default SummaryCard;