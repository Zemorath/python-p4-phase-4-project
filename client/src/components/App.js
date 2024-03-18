import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";
import SubscriptionList from "../pages/SubscriptionList";

function App() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        fetch("/check_session").then((r) => {
            if (r.ok) {
                r.json().then((user) => setUser(user));
            }
        });
    }, []);

    if (!user) return <Login onLogin={setUser} />;

    return (
        <>
            <NavBar/>
            <main>
                <SubscriptionList />
            </main>
        </>
    )
}

export default App