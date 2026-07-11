import { useEffect, useState } from "react";
import Home from "./pages/Home";
import { Moon, Sun } from "lucide-react";
import "./App.css";

function App() {

    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {

        const savedTheme = localStorage.getItem("theme");

        if (savedTheme === "dark") {

            setDarkMode(true);

            document.documentElement.classList.add("dark");

        }

    }, []);

    const toggleTheme = () => {

        const newTheme = !darkMode;

        setDarkMode(newTheme);

        if (newTheme) {

            document.documentElement.classList.add("dark");

            localStorage.setItem("theme", "dark");

        } else {

            document.documentElement.classList.remove("dark");

            localStorage.setItem("theme", "light");

        }

    };

    return (

        <div className="app">

            <button
                className="theme-toggle"
                onClick={toggleTheme}
            >

                {darkMode ? <Sun size={22} /> : <Moon size={22} />}

            </button>

            <Home />

        </div>

    );

}

export default App;