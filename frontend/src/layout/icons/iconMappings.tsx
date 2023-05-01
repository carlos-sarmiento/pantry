

export type PossibleIconMapping = {
    dashboard: string,
    product: string,
    shelves: string,
    shoppingLists: string,
    todos: string,
    packages: string,
    debug: string,
    xmark: string,
}

export type PantryIcons = keyof PossibleIconMapping;

export const freeFontAwesomeMappings: Readonly<PossibleIconMapping> = {
    dashboard: "chart-line",
    product: "object-group",
    shelves: "question",
    shoppingLists: "cart-shopping",
    todos: "list",
    packages: "box",
    debug: "bug",
    xmark: "xmark",
}

export const proFontAwesomeMappings: Readonly<Partial<PossibleIconMapping>> = {
    product: "can-food",
    shelves: "shelves",
    shoppingLists: "cash-register"
}