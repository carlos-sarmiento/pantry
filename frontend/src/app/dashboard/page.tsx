'use client'

import React from 'react';
import DebuggingCard from '@/utilities/DebugWindow';
import {
  useSuspenseQuery_experimental as useSuspenseQuery,
  gql
} from "@apollo/client";
import Head from 'next/head';

const QUERY = gql`
  query MyQuery {
    productDefinitions {
      barcodes
      id
      name
      shoppingListItems {
        id
      }
    }
  }
`;

export default function Home() {
  const { data, error } = useSuspenseQuery(QUERY);

  return (
    <>
      <Head>
        <title>My page title</title>
      </Head>
      <h1>Dashboard</h1>
      <DebuggingCard value={{ data, error } } />
    </>
  )
}
