import { useUIConfigurationContext, useUIConfigurationContextUpdater } from "@/config/UIConfigContext";
import PantryLink from "@/layout/PantryLink";
import PantryIcon from "@/layout/icons/Icon";
import React, { CSSProperties, Children, useState } from "react";

type DebuggingCardProps = {
    label?: string,
    value: any
}

const debugPreStyle = {
    margin: "0"
}

type DebuggingToggleLinkProps = {
    children: (string | JSX.Element) | (string | JSX.Element)[],
    className?: string,
    style?: CSSProperties,

}

export function DebuggingToggleLink({ className, style, children }: DebuggingToggleLinkProps): JSX.Element {
    const uiConfigUpdated = useUIConfigurationContextUpdater();
    const uiconfig = useUIConfigurationContext();

    return <PantryLink
        className={className ?? ''}
        onClick={() => uiConfigUpdated({ debugModeOn: !uiconfig.debugModeOn })} style={style ?? {}}>
        {children}
    </PantryLink>;
}

export default function DebuggingCard(props: DebuggingCardProps): JSX.Element {
    const uiconfig = useUIConfigurationContext();
    const [isVisible, setIsVisible] = useState(true);

    if (!uiconfig.debugModeOn || !isVisible) {
        return <></>;
    }

    return <div className="card border-warning" >
        <div className="card-header text-bg-warning">
            <div className="d-flex">
                <div className="flex-grow-1">
                 <PantryIcon icon="debug" className='me-2'  />

                    {props.label == null ? "Debugging View" : `Debug View: ${props.label}`}
                </div>
                <div className="">
                    <PantryLink onClick={() => setIsVisible(false)} variant="dark">
                        <PantryIcon icon="xmark" />
                    </PantryLink>
                </div>
            </div>
        </div>
        <div className="card-body">
            <pre style={debugPreStyle}>
                {JSON.stringify(props.value, null, 2)}
            </pre>
        </div>
    </div>;
}