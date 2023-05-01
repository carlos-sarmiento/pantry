import React from 'react';

const verticalDividerStyle = {
    backgroundColor: "rgba(0, 0, 0, .1)",
    border: "solid rgba(0, 0, 0, .15)",
    borderWidth: "1px 0",
    boxShadow: "inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15)",
    flexShrink: 0,
    width: "1.5rem",
    height: "100vh"
}

export default function VerticalDivider(): JSX.Element {
    return <div style={verticalDividerStyle} />;
}
