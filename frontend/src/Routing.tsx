import React from "react";
import {BrowserRouter, Route, Routes} from "react-router";
import {Hello} from "./Hello"

export const Routing = () =>
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Hello />} />
        </Routes>
    </BrowserRouter>
