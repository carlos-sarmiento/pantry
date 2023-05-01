import { useUIConfigurationContext } from "@/config/UIConfigContext";
import { PantryIcons, freeFontAwesomeMappings, proFontAwesomeMappings } from "@/layout/icons/iconMappings";
import React, { CSSProperties, useMemo } from "react";

type IconProps = {
    className?: string,
    style?: CSSProperties,
    icon: PantryIcons
}

function FontAwesomeFreeIcon(props: IconProps): JSX.Element {
    const finalClassName = useMemo(() => {
        const iconClass = freeFontAwesomeMappings[props.icon]

        console.log({icon: props.icon, iconClass, freeFontAwesomeMappings})

        return `fa-solid fa-${iconClass} ${props.className ?? ''}`;
    }, [props.className, props.icon])

    return <i className={finalClassName} style={props.style ?? {}} />
}

function FontAwesomeProIcon(props: IconProps): JSX.Element {
    const finalClassName = useMemo(() => {
        const iconClass = proFontAwesomeMappings[props.icon] != null
            ? proFontAwesomeMappings[props.icon]
            : freeFontAwesomeMappings[props.icon];

        return `fa-light fa-${iconClass} ${props.className ?? ''}`;
    }, [props.className, props.icon])

    return <i className={finalClassName} style={props.style ?? {}} />
}

export default function PantryIcon(props: IconProps): JSX.Element {
    const uiconfig = useUIConfigurationContext()

    if (uiconfig.iconSource === "fontawesome-pro") {
        return <FontAwesomeProIcon {...props} />
    }

    return <FontAwesomeFreeIcon {...props} />;
}