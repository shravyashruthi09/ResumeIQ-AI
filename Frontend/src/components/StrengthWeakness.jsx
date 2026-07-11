import { ThumbsUp, ThumbsDown } from "lucide-react";

function StrengthWeakness({ analysis }) {
    if (!analysis) return null;

    const strengths = analysis.resume_strengths || [];
    const weaknesses = analysis.resume_weaknesses || [];

    return (
        <div className="strength-card">
            <h2 className="card-title">
                <ThumbsUp size={28} />
                Strengths & Weaknesses
            </h2>

            <div className="strength-grid">

                <div className="strength-box">
                    <h3>✅ Strengths</h3>

                    {strengths.length ? (
                        <ul>
                            {strengths.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No strengths detected.</p>
                    )}
                </div>

                <div className="weakness-box">
                    <h3>
                        <ThumbsDown size={18} />
                        Weaknesses
                    </h3>

                    {weaknesses.length ? (
                        <ul>
                            {weaknesses.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No weaknesses detected.</p>
                    )}
                </div>

            </div>
        </div>
    );
}

export default StrengthWeakness;