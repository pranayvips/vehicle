// import React, { useContext, useRef, useState } from "react";
import {  Outlet,Link,useNavigate } from 'react-router-dom';
import "./navbar.css";
import 'boxicons/css/boxicons.min.css';

const Navbar = () => {
    const navigate = useNavigate();
    const current = window.location.pathname.replace("/","")
    console.log(current)
    //   const [theme, setTheme] = useState((localStorage.getItem("theme")==null || localStorage.getItem("theme") == "0") ? false : true);
    return (<>
        <header>
            <div className="header-title" onClick={()=>{navigate('/', { replace: true });}}>
                <img src="/icon.png" alt="" />
                <h1>Rushly</h1>
            </div> 
            <div className="header-links">
                <h2 className={current.includes("dashboard")?"active":null}><Link to="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</Link></h2>
                <h2 className={current.includes("features")?"active":null}><i class='bx bx-bong'></i>Features</h2>
                <h2 className={current.includes("liveTraffic")?"active":null}><Link to="/liveTraffic"><i class='bx bx-wifi'></i>Live Traffic</Link></h2>
                <h2 className={current.includes("checkTraffic")?"active":null}><Link to="/checkTraffic"><i class='bx bx-map-pin'></i>Check Traffic</Link></h2>
                <h2 className={current.includes("about")?"active":null}><i class='bx bx-user' ></i>About</h2>
                <h2 onClick={()=>{
                    document.getElementById("contact").scrollIntoView({
                        behavior: "smooth", // optional: "auto" or "smooth"
                        block: "start"      // optional: "start", "center", "end", "nearest"
                      });
                }}><i class='bx bx-phone-call' ></i>Contact</h2>
            </div>
            <button>Get Started</button>
        </header>
            <Outlet /></>
    )
}

export default Navbar;
