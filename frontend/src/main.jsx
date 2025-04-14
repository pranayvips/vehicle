import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { createRoot } from "react-dom/client";
import Navbar from "./navbar/navbar";
import "./index.css";
import Home from "./home/home";
import Footer from "./footer/footer";
import Dashboard from "./dashboard/dashboard";
import LiveTraffic from "./live/live";
import Checktraffic from "./checkTraffic/checktraffic";
import Vehicle from "./vehicle/vehicle";
// import App from './App.jsx'

createRoot(document.body).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navbar />}>
          <Route
            index
            element={
              <>
                <Home />
                <Footer />
              </>
            }
          />
        </Route>
        <Route path="/dashboard" element={<Dashboard />}></Route>
        <Route path="/liveTraffic" element={<Navbar />}>
          <Route
            index
            element={
              <>
                <LiveTraffic />
                <Footer />
              </>
            }
          />
        </Route>
        <Route path="/checkTraffic" element={<Navbar />}>
          <Route
            index
            element={
              <>
                <Checktraffic />
                <Footer />
              </>
            }
          />
        </Route>
        <Route path="/vehicle" element={<Navbar />}>
          <Route
            index
            element={
              <>
                <Vehicle />
                <Footer />
              </>
            }
          />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// integrate the weather menu button or like a small tabb



// https://www.carinfo.app/rc-details/DL14CD4007