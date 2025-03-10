import React from "react";
import '@mantine/core/styles/Badge.css';
import { Badge } from "@mantine/core";
import {SignedOut, SignInButton, SignedIn, UserButton} from "@clerk/clerk-react";

export const Hello = () =>
    <div>
        <Badge color="blue">Hello in lunamor!</Badge>
        <SignedOut>
            <SignInButton />
        </SignedOut>
        <SignedIn>
            <UserButton />
        </SignedIn>

    </div>
