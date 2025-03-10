import React from "react";
import {BrowserRouter, Route, Routes} from "react-router";
import {Hello} from "./Hello"
import {ClerkProvider} from "@clerk/clerk-react"

const key = process.env.CLERK_PUBLIC_KEY

export const Routing = () =>
    <ClerkProvider publishableKey={process.env.CLERK_PUBLIC_KEY} afterSignOutUrl="/">
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Hello />} />
        </Routes>
    </BrowserRouter>
    </ClerkProvider>
