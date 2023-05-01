"use client";

import { ApolloClient, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
    uri: window != null ? `${window.location.origin}/graphql` : "/graphql",
    cache: new InMemoryCache(),
});

export default client;