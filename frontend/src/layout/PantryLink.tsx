import { useUIConfigurationContext, useUIConfigurationContextUpdater } from "@/config/UIConfigContext";
import React, { CSSProperties, useMemo, useState } from "react";

type RequireAtLeastOne<T, Keys extends keyof T = keyof T> =
    Pick<T, Exclude<keyof T, Keys>>
    & {
        [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>
    }[Keys]

type Content = (string | JSX.Element)

type LinkPropsBase = {
    onClick?: () => void,
    className?: string,
    children: Content| Content[],
    href?: string,
    variant?: "primary" | "secondary" | "success" | "danger" | "warning" | "info" | "light" | "dark" | "body-emphasis",
    style? : CSSProperties,
}

type LinkProps = RequireAtLeastOne<LinkPropsBase, 'href' | 'onClick'>

export default function Link({ children, className, onClick, href, variant, style }: LinkProps): JSX.Element {
    const finalClassName = useMemo(() => {
        const variantClassname = `link-${variant != null ? variant : "primary"}`;
        return `${variantClassname} ${className ?? ''}`;
    }, [variant, className])

    return <a
        onClick={
            onClick != null ? (e) => {
                e.preventDefault();
                onClick();
            } : undefined
        }
        className={finalClassName}
        href={href != null ? href : ""}
        style={style}>
        {children}
    </a>;

}