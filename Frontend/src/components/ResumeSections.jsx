import { LayoutList } from "lucide-react";

function ResumeSections({ analysis }) {
    if (!analysis) return null;

    const sections = analysis.resume_sections || {};

    return (
        <div className="sections-card">
            <h2 className="card-title">
                <LayoutList size={28} />
                Resume Sections
            </h2>

            <div className="section-score">
                Section Score :
                <strong> {sections.section_score}/100</strong>
            </div>

            <div className="section-grid">

                <div className="section-box">
                    <h3>Missing Essential Sections</h3>

                    {sections.essential_missing?.length ? (
                        <ul>
                            {sections.essential_missing.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>None 🎉</p>
                    )}

                </div>

                <div className="section-box">
                    <h3>Recommended Sections</h3>

                    {sections.recommended_missing?.length ? (
                        <ul>
                            {sections.recommended_missing.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>None 🎉</p>
                    )}

                </div>

            </div>
        </div>
    );
}

export default ResumeSections;