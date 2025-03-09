import React from "react";
import {MantineProvider} from "@mantine/core";
import {Routing} from "./Routing";

import '@mantine/core/styles/global.css';

export const Root = () => <MantineProvider>
    <Routing />
</MantineProvider>
