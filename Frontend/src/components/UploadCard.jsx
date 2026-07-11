import { useState, useRef } from "react";
import { Upload, Sparkles } from "lucide-react";
import API from "../services/api";

function UploadCard({ setAnalysis }) {

    const [resume, setResume] = useState(null);

    const fileInputRef = useRef(null);

    const [jobDescription, setJobDescription] = useState("");

    const [loading, setLoading] = useState(false);

    const [dragActive, setDragActive] = useState(false);

    // ===========================
    // AI Loading Animation
    // ===========================

    const loadingSteps = [

        "🧠 Reading Resume...",

        "🔍 Matching Skills with Job Description...",

        "📊 Calculating ATS Score...",

        "✨ Generating AI Insights..."

    ];

    const [loadingText, setLoadingText] = useState("");

    const [currentStep, setCurrentStep] = useState(0);

    // ===========================
    // Analyze Resume
    // ===========================

    const analyzeResume = async () => {

        if (!resume || !jobDescription) {

            alert("Please upload a resume and paste a Job Description.");

            return;

        }

        setLoading(true);

        setCurrentStep(0);

        setLoadingText(loadingSteps[0]);

        const formData = new FormData();

        formData.append("file", resume);

        formData.append("job_description", jobDescription);

        // Start backend request immediately

        const backendPromise = API.post(

            "/analyze",

            formData,

            {

                headers: {

                    "Content-Type": "multipart/form-data"

                }

            }

        );

        // Show all four AI stages

        for (let i = 0; i < loadingSteps.length; i++) {

            setCurrentStep(i);

            setLoadingText(loadingSteps[i]);

            await new Promise(resolve => setTimeout(resolve, 900));

        }

        try {

            const response = await backendPromise;

            setAnalysis(response.data.analysis);

        }

        catch (err) {

            console.error(err);

            alert("Analysis Failed");

        }

        finally {

            setLoading(false);

        }

    };

    // ===========================
    // Drag & Drop
    // ===========================

    const handleDrag = (e) => {

        e.preventDefault();

        e.stopPropagation();

        if (e.type === "dragenter" || e.type === "dragover") {

            setDragActive(true);

        }

        else {

            setDragActive(false);

        }

    };

    const handleDrop = (e) => {

        e.preventDefault();

        e.stopPropagation();

        setDragActive(false);

        if (e.dataTransfer.files && e.dataTransfer.files[0]) {

            setResume(e.dataTransfer.files[0]);

        }

    };
        return (

        <div className="upload-card">

            <div
                className={`upload-box ${dragActive ? "active" : ""}`}
                onDragEnter={handleDrag}
                onDragLeave={handleDrag}
                onDragOver={handleDrag}
                onDrop={handleDrop}
            >

                <Upload
                    size={60}
                    className="upload-icon"
                />

                <h3>

                    Drag & Drop Resume

                </h3>

                <p>

                    Only PDF is accepted

                </p>

                <input

                    ref={fileInputRef}

                    type="file"

                    accept=".pdf"

                    hidden

                    onChange={(e) =>

                        setResume(e.target.files[0])

                    }

                />

                <button

                    type="button"

                    className="upload-btn"

                    onClick={() =>

                        fileInputRef.current.click()

                    }

                >

                    Choose Resume

                </button>

                {

                    resume && (

                        <div className="selected-file">

                            <div
                                style={{
                                    display: "flex",
                                    alignItems: "center",
                                    gap: "10px"
                                }}
                            >

                                📄

                                <span>

                                    {resume.name}

                                </span>

                            </div>

                            <button

                                className="remove-btn"

                                onClick={() =>

                                    setResume(null)

                                }

                            >

                                ✕

                            </button>

                        </div>

                    )

                }

            </div>

            <textarea

                rows="10"

                placeholder="Paste the complete Job Description here..."

                value={jobDescription}

                onChange={(e) =>

                    setJobDescription(e.target.value)

                }

            />

            <button

                className="primary-btn"

                onClick={analyzeResume}

                disabled={loading}

            >

                {

                    loading

                    ?

                    <>

                        <span className="thinking-dots">

                            <span></span>

                            <span></span>

                            <span></span>

                        </span>

                        {loadingText}

                    </>

                    :

                    <>

                        <Sparkles size={18} />

                        Analyze Resume

                    </>

                }

            </button>

        </div>

    );

}

export default UploadCard;