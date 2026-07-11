import { CheckCircle, XCircle, PlusCircle } from "lucide-react";

function SkillsAnalysis({ analysis }) {
    if (!analysis) {
        return null;
    }

    const matchedSkills = analysis.matched_skills || [];
    const missingSkills = analysis.missing_skills || [];
    const additionalSkills = analysis.additional_skills || [];

    return (
        <div className="skills-card">
            <h2 className="card-title">Skills Analysis</h2>

            <div className="skills-grid">

                {/* Matched Skills */}
                <div className="skill-column">
                    <h3 className="matched-title">
                        <CheckCircle size={20} />
                        Matched Skills
                    </h3>

                    <div className="skill-list">
                        {matchedSkills.length > 0 ? (
                            matchedSkills.map((skill, index) => (
                                <span key={index} className="skill-tag matched">
                                    {skill}
                                </span>
                            ))
                        ) : (
                            <p>No matched skills found.</p>
                        )}
                    </div>
                </div>

                {/* Missing Skills */}
                <div className="skill-column">
                    <h3 className="missing-title">
                        <XCircle size={20} />
                        Missing Skills
                    </h3>

                    <div className="skill-list">
                        {missingSkills.length > 0 ? (
                            missingSkills.map((skill, index) => (
                                <span key={index} className="skill-tag missing">
                                    {skill}
                                </span>
                            ))
                        ) : (
                            <p>No missing skills 🎉</p>
                        )}
                    </div>
                </div>

                {/* Additional Skills */}
                <div className="skill-column">
                    <h3 className="additional-title">
                        <PlusCircle size={20} />
                        Additional Skills
                    </h3>

                    <div className="skill-list">
                        {additionalSkills.length > 0 ? (
                            additionalSkills.map((skill, index) => (
                                <span key={index} className="skill-tag additional">
                                    {skill}
                                </span>
                            ))
                        ) : (
                            <p>No additional skills.</p>
                        )}
                    </div>
                </div>

            </div>
        </div>
    );
}

export default SkillsAnalysis;