import VerticalNavigationList, {
  NavigationListItem,
} from "@/layout/navigation/VerticalNavigationList";
import React, { useState } from "react";
import { usePathname, useRouter } from 'next/navigation';
import { DebuggingToggleLink } from "@/utilities/DebugWindow";


type NavigationSections =
  | "dashboard"
  | "products"
  | "shelves"
  | "shopping-lists"
  | "todos"
  | "packages";

export default function LayoutNavigationSidebar(): JSX.Element {
  const [selectedNav, setSelectedNav] =
    useState<NavigationSections>("dashboard");
  const router = useRouter()

  const pathname = usePathname().split('/').filter(Boolean);

  // @ts-ignore
  const section: NavigationSections = pathname[0] ?? 'dashboard';

  return (
    <div
      className="d-flex flex-column p-3 text-bg-dark"
      style={{ width: "280px", height: "100vh" }}>
      <a
        href="/"
        className="d-flex align-items-center text-white text-decoration-none">
        <div style={{ width: "40px", textAlign: "center" }}>
          <i className={`fa-solid fa-bowl-rice fa-xl`} />
        </div>
        <span className="fs-4">Pantry</span>
      </a>
      <hr />

      <VerticalNavigationList
        onClick={(option) => { router.push(`/${option}`) }}
        selectedValue={section}>
        <NavigationListItem
          label="Dashboard"
          icon="dashboard"
          value="dashboard"
        />
        <NavigationListItem
          label="Products"
          icon="product"
          value="products"
        />
        <NavigationListItem
          label="Shelves"
          icon="shelves"
          value="shelves"
        />
        <NavigationListItem
          label="Shopping Lists"
          icon="shoppingLists"
          value="shopping-lists"
        />
        <NavigationListItem
          label="To Dos"
          icon="todos"
          value="todos"
        />
        <NavigationListItem
          label="Packages"
          icon="packages"
          value="packages"
        />
      </VerticalNavigationList>

      <hr />
      <div className="dropdown">
        <DebuggingToggleLink
          className="d-flex align-items-center text-white text-decoration-none dropdown-toggle">
          <img
            src="https://github.com/mdo.png"
            alt=""
            width="32"
            height="32"
            className="rounded-circle me-2"
          />
          <strong>Toggle Debug</strong>
        </DebuggingToggleLink>

      </div>
    </div>
  );
}
