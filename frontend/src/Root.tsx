import React from "react";
import {MantineProvider} from "@mantine/core";
import {Routing} from "./Routing";

export const Root = () => <MantineProvider>
    <Routing />
</MantineProvider>
