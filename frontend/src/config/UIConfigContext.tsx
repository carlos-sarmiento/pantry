import { createContext, useContext } from 'react';

export type UIConfigurationContextProps = {
    iconSource: "fontawesome-free" | "fontawesome-pro",
    debugModeOn: boolean
}

export type UIConfigurationContextUpdaterCallback = (updates: Partial<UIConfigurationContextProps>) => void;

export const UIConfigurationContextDefaultValues: Readonly<UIConfigurationContextProps> = {
    iconSource: "fontawesome-pro",
    debugModeOn: true,
}

export const UIConfigurationContext = createContext<UIConfigurationContextProps>(UIConfigurationContextDefaultValues);

export const UIConfigurationContextUpdater = createContext<UIConfigurationContextUpdaterCallback>(() => {});

export function useUIConfigurationContext(): UIConfigurationContextProps {
    return useContext(UIConfigurationContext);
}

export function useUIConfigurationContextUpdater(): UIConfigurationContextUpdaterCallback {
    return useContext(UIConfigurationContextUpdater);
}