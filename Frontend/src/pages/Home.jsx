import { useState } from "react";
import { Sparkles } from "lucide-react";

import UploadCard from "../components/UploadCard";
import ATSScoreCard from "../components/ATSScoreCard";
import SummaryCard from "../components/SummaryCard";
import SkillsAnalysis from "../components/SkillsAnalysis";
import CategoryScores from "../components/CategoryScores";
import ScoreBreakdown from "../components/ScoreBreakdown";
import ResumeQuality from "../components/ResumeQuality";
import ResumeSections from "../components/ResumeSections";
import StrengthWeakness from "../components/StrengthWeakness";
import Recommendations from "../components/Recommendations";


function Home() {

    const [analysis, setAnalysis] = useState(null);

    return (

        <>

            <section className="hero">

                <div className="hero-badge">

                    <Sparkles size={18} />

                    AI Powered Resume Intelligence

                </div>

                <h1>

                    Resume<span>IQ</span> AI

                </h1>

                <p>

                    Analyze your resume against any Job Description and receive
                    ATS Score, Skill Gap Analysis, Resume Quality Insights,
                    Interview Readiness and AI-powered Recommendations.

                </p>

            </section>

            <div className="container">

                <UploadCard setAnalysis={setAnalysis} />

                {
                    analysis && (
                        <div className="dashboard">

                            <div className="dashboard-full">
                                <ATSScoreCard analysis={analysis} />
                            </div>

                            <div className="dashboard-full">
                                <SummaryCard analysis={analysis} />
                            </div>

                            <div className="dashboard-grid">

                                <SkillsAnalysis analysis={analysis} />

                                <CategoryScores analysis={analysis} />

                                <ResumeQuality analysis={analysis} />

                                <ResumeSections analysis={analysis} />

                                <StrengthWeakness analysis={analysis} />

                                <Recommendations analysis={analysis} />

                            </div>

                        </div>
                    )
                }

            </div>

        </>

    );

}

export default Home;