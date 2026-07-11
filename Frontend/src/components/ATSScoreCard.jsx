import { useEffect, useState } from "react";
import { Award, Briefcase, Users } from "lucide-react";
function ATSScoreCard({ analysis }) {

    if (!analysis) return null;

    const score = analysis.ats_score || 0;
    const [animatedScore, setAnimatedScore] = useState(0);

    useEffect(() => {

        let start = 0;

        const duration = 1200;

        const increment = score / (duration / 16);

        const timer = setInterval(() => {

            start += increment;

            if (start >= score) {

                setAnimatedScore(score);

                clearInterval(timer);

            } else {

                setAnimatedScore(start);

            }

        }, 16);

        return () => clearInterval(timer);

    }, [score]);

    const getColor = () => {
        if (score >= 80) return "#22c55e";
        if (score >= 60) return "#e2dc41";
        if (score >= 40) return "#f59e0b";
        return "#ef4444";
    };

    const radius = 90;
    const circumference = 2 * Math.PI * radius;

    return (

        <div className="ats-card">

            <h2 className="ats-title">
                ATS Resume Score
            </h2>

            <p className="ats-subtitle">
                Overall compatibility with the Job Description
            </p>

            <div className="ats-circle">

                <svg
                    width="220"
                    height="220"
                >

                    <circle
                        cx="110"
                        cy="110"
                        r={radius}
                        className="circle-bg"
                    />

                    <defs>

                        <linearGradient
                            id="scoreGradient"
                            x1="0%"
                            y1="0%"
                            x2="100%"
                            y2="0%"
                        >

                            <stop offset="0%" stopColor="#ef4444" />

                            <stop offset="45%" stopColor="#facc15" />

                            <stop offset="100%" stopColor="#22c55e" />

                        </linearGradient>

                    </defs>

                    <circle
                        cx="110"
                        cy="110"
                        r={radius}
                        className="circle-progress"
                        stroke="url(#scoreGradient)"
                        strokeDasharray={circumference}
                        strokeDashoffset={
                            circumference -
                            (circumference * score) / 100
                        }
                    />

                </svg>

                <div className="circle-content">

                    <h1>{Math.round(animatedScore)}</h1>
                    <span>/100</span>

                </div>

            </div>

            <h3 className="match-text">

                {score >= 80
                    ? "Excellent Match"
                    : score >= 60
                        ? "Good Match"
                        : score >= 40
                            ? "Average Match"
                            : "Needs Improvement"}

            </h3>

            <div className="ats-info">

                <div className="info-card">

                    <Award size={28} />

                    <small>Match Level</small>

                    <h4>{analysis.match_level}</h4>

                </div>

                <div className="info-card">

                    <Briefcase size={28} />

                    <small>Hiring Chance</small>

                    <h4>{analysis.hiring_chance}</h4>

                </div>

                <div className="info-card">

                    <Users size={28} />

                    <small>Interview Chance</small>

                    <h4>{analysis.interview_probability}</h4>

                </div>

            </div>

        </div>

    );

}

export default ATSScoreCard;