import PantryIcon from '@/layout/icons/Icon';
import { PantryIcons } from '@/layout/icons/iconMappings';
import React, { MouseEventHandler, createContext, useContext } from 'react';

const NavListContext = createContext<NavListContextType<any>>({});

type NavListContextType<T> = {
    selectedValue?: T,
    onClickHandler?: (option: T) => void
}

type VerticalNavigationListProps<T> = {
    children: JSX.Element[] | JSX.Element,
    onClick?: (option: T) => void,
    selectedValue?: T
}

export default function VerticalNavigationList<T>(props: VerticalNavigationListProps<T>): JSX.Element {
    return <ul className="nav nav-pills flex-column mb-auto">
        <NavListContext.Provider value={{ onClickHandler: props.onClick, selectedValue: props.selectedValue }}>
            {props.children}
        </NavListContext.Provider>
    </ul>;
}

type NavigationListItemProps = {
    label: string,
    isActive?: boolean,
    icon?: PantryIcons,
    value?: string,
    onClick?: MouseEventHandler<Element>,
    href?: string,
}

const iconStyle = {} //{ width: "16px", height: "16px" }

export function NavigationListItem({
    label,
    isActive,
    icon,
    value,
    onClick,
    href,
}: NavigationListItemProps): JSX.Element {
    const navContext = useContext(NavListContext);

    const finalValue = value != null ? value : label;
    const actualIsActive = isActive != null ? isActive : (navContext.selectedValue === finalValue);

    const classes = `nav-link text-white ${actualIsActive ? 'active' : ''}`;
    const onClickHandler = onClick;
    const contextClickHandler = navContext.onClickHandler ?? undefined;

    let iconComponent = icon != null
        ? <PantryIcon icon={icon} className='pe-none me-2' style={iconStyle} />
        : null;

    return (
        <li className="nav-item">
            <a
                onClick={
                    onClickHandler != null || contextClickHandler != null ? (e) => {
                        e.preventDefault();
                        if (onClickHandler != null) {
                            onClickHandler(e);
                        }
                        else if (contextClickHandler != null) {
                            contextClickHandler(finalValue)
                        }
                    } : undefined}
                className={classes}
                href={href != null ? href : ""}>
                <div className="d-flex align-items-center">
                    <div style={{ width: "40px", textAlign: "center" }}>
                        {iconComponent}
                    </div>
                    <span className="fs-7">{label}</span>
                </div>
            </a>
        </li>
    );
}
