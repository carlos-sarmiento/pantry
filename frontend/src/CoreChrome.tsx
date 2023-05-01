"use client";

import React, { useMemo, useState } from 'react';
import { UIConfigurationContext, UIConfigurationContextDefaultValues, UIConfigurationContextProps, UIConfigurationContextUpdater } from '@/config/UIConfigContext';
import VerticalDivider from '@/layout/VerticalDivider';
import LayoutNavigationSidebar from '@/layout/LayoutNavigationSidebar';
import { ApolloProvider, SuspenseCache } from "@apollo/client";
import client from "@/apollo-client";


const gridStyle = {
  height: "100vh",
  width: "100vw",
  display: "grid",
  gridTemplateColumns: "280px auto 1fr",
  gap: "0",
  gridTemplateRows: "1fr"
}

export default function CoreChrome({ children }: { children?: React.ReactNode | React.ReactNode[] }) {
  const [currentUIConfig, setCurrentUIConfig] = useState<UIConfigurationContextProps>(() => {
    return { ...UIConfigurationContextDefaultValues };
  });
  const suspenseCache = new SuspenseCache();

  window.document.getRootNode(undefined);

  return (
    <ApolloProvider client={client} suspenseCache={suspenseCache}>
      <UIConfigurationContext.Provider value={currentUIConfig}>
        <UIConfigurationContextUpdater.Provider value={(partials) => setCurrentUIConfig({ ...currentUIConfig, ...partials })}>
          <div style={gridStyle}>
            <div style={{ gridRow: "1", gridColumn: "1" }}>
              <LayoutNavigationSidebar />
            </div>
            <div style={{ gridRow: "1", gridColumn: "2" }}>
              <VerticalDivider />
            </div>
            <div style={{ gridRow: "1", gridColumn: "3", overflow: "scroll" }}>
              <div className='p-3'>
                <React.Suspense fallback={<h1>Loading</h1>} >
                  {children}
                </React.Suspense>
              </div>
            </div>
          </div>
        </UIConfigurationContextUpdater.Provider>
      </UIConfigurationContext.Provider>
    </ApolloProvider>
  )
}
